"""Verify Tier 2 status of the 100 selected AKI cases using an LLM.

The regex filter in kdigo_aki_finder.py catches obvious AKI mentions, but may
miss subtle phrasings ("worsening renal function", "renal insufficiency",
etc.). This script re-checks the 100 sampled discharge summaries with Sonnet
to confirm AKI is truly never mentioned.

Output:
  - tier2_verification.json — per-case verdict from Sonnet
  - tier2_verification_report.md — summary + cleaned hit rate

Cost: ~$0.05/case × 100 = ~$5 total with Sonnet 4.6.

Does NOT modify existing scripts or results. Adds a verification layer on top.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import pandas as pd
from anthropic import APIError, Anthropic
from dotenv import load_dotenv

ROOT = Path(__file__).parent
MIMIC_ROOT = ROOT.parent.parent
NOTE = MIMIC_ROOT / "physionet.org" / "files" / "mimic-iv-note" / "2.2" / "note"

MODELS = {
    "haiku": "claude-haiku-4-5",
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-7",
}

VERIFY_PROMPT = """You are a senior internal medicine physician auditing a discharge summary.

Read the discharge summary below and decide: does it mention OR clinically imply that the patient had acute kidney injury (AKI) during this admission? Include any of:
- Explicit terms: AKI, ARF, acute kidney/renal injury/failure/insufficiency, acute on chronic kidney disease
- Implicit mentions: rising/elevated/worsening creatinine, azotemia, decreased GFR/eGFR during stay, oliguria attributed to renal cause, contrast-induced nephropathy, ATN, prerenal/intrinsic/postrenal renal failure
- Treatment indicating recognition: nephrology consult during admission, dialysis initiated for new renal dysfunction, fluid resuscitation for renal causes

Return STRICT JSON only, no prose:

{
  "verdict": "MENTIONED" | "IMPLIED" | "NOT_MENTIONED",
  "evidence": "short quote or phrase from the summary (≤20 words), or 'none' if NOT_MENTIONED",
  "reasoning": "one short sentence"
}

DISCHARGE SUMMARY:
---
{TEXT}
---
"""


def call_with_retry(fn, max_retries: int = 6, initial_delay: float = 4.0):
    delay = initial_delay
    for attempt in range(max_retries):
        try:
            return fn()
        except APIError as e:
            if attempt == max_retries - 1:
                raise
            wait = delay * (2 ** attempt)
            print(f"    retry after {wait:.0f}s ({type(e).__name__})")
            time.sleep(wait)


def extract_json(text: str) -> dict:
    text = text.strip()
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.MULTILINE).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    depth = 0
    end = -1
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    block = text[start:end] if end > 0 else text[start:]
    try:
        return json.loads(block)
    except json.JSONDecodeError:
        block = re.sub(r",(\s*[}\]])", r"\1", block)
        return json.loads(block)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="sonnet", choices=list(MODELS.keys()))
    parser.add_argument("--selected", default=str(ROOT / "selected_admissions_aki.json"))
    parser.add_argument("--results", default=str(ROOT / "results_aki_haiku.json"),
                        help="Existing aki_test.py results to recompute hit rate on cleaned set")
    args = parser.parse_args()

    load_dotenv(ROOT.parent / "prototype_a" / ".env", override=True)
    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")

    selected_path = Path(args.selected)
    if not selected_path.exists():
        sys.exit(f"Missing {selected_path} — run kdigo_aki_finder.py first")
    selected = json.loads(selected_path.read_text())
    hadm_ids = [int(s["hadm_id"]) for s in selected]
    print(f"Verifying {len(hadm_ids)} cases with {args.model}\n")

    print("Loading discharge.csv.gz (~1 min)…")
    disch = pd.read_csv(NOTE / "discharge.csv.gz",
                        usecols=["hadm_id", "text"],
                        dtype={"text": str})
    disch_by_hadm = dict(zip(disch["hadm_id"].astype("int64"), disch["text"]))
    print(f"  {len(disch_by_hadm):,} summaries loaded\n")

    client = Anthropic()
    model_id = MODELS[args.model]
    verdicts = {}
    in_total = out_total = 0
    n_mentioned = n_implied = n_not = n_missing = 0

    for i, hadm_id in enumerate(hadm_ids, 1):
        text = disch_by_hadm.get(hadm_id)
        if text is None or not isinstance(text, str):
            n_missing += 1
            verdicts[str(hadm_id)] = {"verdict": "NO_SUMMARY", "evidence": "", "reasoning": "no discharge text"}
            print(f"  [{i:>3}/{len(hadm_ids)}] {hadm_id}  NO_SUMMARY")
            continue

        prompt = VERIFY_PROMPT.replace("{TEXT}", text[:30000])  # cap to avoid token blowup
        def call():
            return client.messages.create(model=model_id, max_tokens=500,
                                           messages=[{"role": "user", "content": prompt}])
        try:
            resp = call_with_retry(call)
            in_total += resp.usage.input_tokens
            out_total += resp.usage.output_tokens
            parsed = extract_json(resp.content[0].text)
            verdict = parsed.get("verdict", "PARSE_ERROR")
            verdicts[str(hadm_id)] = parsed
        except Exception as e:
            verdicts[str(hadm_id)] = {"verdict": "ERROR", "error": str(e)}
            print(f"  [{i:>3}/{len(hadm_ids)}] {hadm_id}  ERROR: {e}")
            continue

        if verdict == "MENTIONED":
            n_mentioned += 1
        elif verdict == "IMPLIED":
            n_implied += 1
        elif verdict == "NOT_MENTIONED":
            n_not += 1

        evidence = (parsed.get("evidence", "") or "")[:50]
        print(f"  [{i:>3}/{len(hadm_ids)}] {hadm_id}  {verdict:<14s}  {evidence}")

    # Save raw verdicts
    out_path = ROOT / "tier2_verification.json"
    out_path.write_text(json.dumps(verdicts, indent=2))
    print(f"\n✓ Wrote {out_path}")

    # ========================================================================
    # Cleaned subset = cases where Sonnet says NOT_MENTIONED
    # ========================================================================
    clean_ids = {hadm for hadm, v in verdicts.items()
                 if v.get("verdict") == "NOT_MENTIONED"}
    print(f"\n=== Verification summary ===")
    print(f"  Sonnet says MENTIONED:     {n_mentioned:>3}  (false-Tier-2, should be excluded)")
    print(f"  Sonnet says IMPLIED:       {n_implied:>3}  (borderline; recommend exclude)")
    print(f"  Sonnet says NOT_MENTIONED: {n_not:>3}  (true Tier 2 — clean subset)")
    print(f"  Missing summaries / errors:{n_missing:>3}")
    print(f"  Sonnet tokens: in={in_total:,}  out={out_total:,}")
    print(f"  Est cost (sonnet 4.6 @ $3/$15 per MTok): ~${(in_total*3 + out_total*15)/1_000_000:.2f}")

    # ========================================================================
    # Recompute hit rate on cleaned subset
    # ========================================================================
    results_path = Path(args.results)
    if not results_path.exists():
        print(f"\n(no {results_path.name} to clean — run aki_test.py first to get cleaned hit rate)")
        return

    results = json.loads(results_path.read_text())
    lines = ["# Tier 2 LLM Verification Report", ""]
    lines.append(f"**Verifier model:** {model_id}")
    lines.append(f"**N audited:** {len(hadm_ids)}")
    lines.append("")
    lines.append("| Verdict | Count | Action |")
    lines.append("|---|---|---|")
    lines.append(f"| MENTIONED (regex missed it) | {n_mentioned} | EXCLUDE from cleaned set |")
    lines.append(f"| IMPLIED (subtle reference) | {n_implied} | EXCLUDE from cleaned set |")
    lines.append(f"| NOT_MENTIONED (true Tier 2) | {n_not} | KEEP |")
    lines.append(f"| No summary / error | {n_missing} | EXCLUDE |")
    lines.append("")
    lines.append("## Cleaned hit rate (NOT_MENTIONED subset only)")
    lines.append("")
    lines.append("| Cutoff | n cleaned | hit@5 cleaned | hit@15 cleaned | original hit@15 |")
    lines.append("|---|---|---|---|---|")

    for cutoff, cases in results.items():
        if not isinstance(cases, dict):
            continue
        all_cases = [(h, c) for h, c in cases.items()]
        clean_cases = [(h, c) for h, c in all_cases if h in clean_ids]
        if not clean_cases:
            continue
        h5 = sum(c.get("hit@5", False) for _, c in clean_cases)
        h15 = sum(c.get("hit@15", False) for _, c in clean_cases)
        n_clean = len(clean_cases)
        orig_h15 = sum(c.get("hit@15", False) for _, c in all_cases)
        orig_n = len(all_cases)
        lines.append(f"| {cutoff} | {n_clean} | {h5}/{n_clean} ({h5/n_clean:.0%}) | "
                     f"{h15}/{n_clean} ({h15/n_clean:.0%}) | {orig_h15}/{orig_n} ({orig_h15/orig_n:.0%}) |")

    lines.append("")
    lines.append("## False-Tier-2 cases (flagged by Sonnet)")
    lines.append("")
    flagged = [(h, v) for h, v in verdicts.items()
               if v.get("verdict") in ("MENTIONED", "IMPLIED")]
    if flagged:
        lines.append("| hadm_id | Verdict | Evidence (Sonnet) |")
        lines.append("|---|---|---|")
        for h, v in flagged[:30]:
            ev = (v.get("evidence", "") or "").replace("|", "/")[:80]
            lines.append(f"| {h} | {v.get('verdict')} | {ev} |")
        if len(flagged) > 30:
            lines.append(f"| … | … | {len(flagged) - 30} more not shown |")
    else:
        lines.append("None — regex filter was clean.")

    report_path = ROOT / "tier2_verification_report.md"
    report_path.write_text("\n".join(lines))
    print(f"✓ Wrote {report_path}")


if __name__ == "__main__":
    main()
