"""Bias-free variant of aki_test.py.

Identical to aki_test.py except the DDx prompt does NOT mention AKI as an
example diagnosis. The original prompt included "e.g., AKI, electrolyte
derangements, complications" — which primes the model to look for AKI.
This script removes that priming so the AKI hit rate reflects truly
unprompted discovery.

Outputs to results_aki_{model}_clean.json so the original 94% result file
is preserved for reproducibility.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

from anthropic import APIError, Anthropic
from dotenv import load_dotenv

ROOT = Path(__file__).parent
DATA = ROOT / "data_aki"

MODELS = {
    "haiku": "claude-haiku-4-5",
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-7",
}

# AKI detection patterns
AKI_DETECT_PATTERN = re.compile(
    r"\b(AKI|ARF"
    r"|acute\s+kidney\s+(injury|failure|insufficiency)"
    r"|acute\s+renal\s+(failure|insufficiency)"
    r"|acute\s+on\s+chronic\s+(kidney|renal)\s+(disease|failure|injury))",
    re.IGNORECASE,
)

DDX_PROMPT = """You are a senior nephrologist consulting on this patient.

Below is a patient chart, including admission notes, exam, and any available labs/imaging/medications up to a specified cutoff time.

Your task: produce a ranked list of the TOP 30 most likely diagnoses that this patient has (or will be found to have) during this hospitalization. Include:
- The principal/primary admitting diagnosis (most likely cause for hospitalization)
- Any secondary acute diagnoses that the workup suggests or that you would expect to be confirmed during the stay

Return STRICT JSON only, no prose:

{
  "differential": [
    {"rank": 1, "diagnosis": "...", "reasoning": "one short sentence"},
    {"rank": 2, "diagnosis": "...", "reasoning": "..."},
    ...
    {"rank": 30, "diagnosis": "...", "reasoning": "..."}
  ]
}

Be specific (e.g., "septic shock due to UTI" not just "infection"). Use standard medical terminology that would map to ICD codes.

CHART:
---
{CHART}
---
"""


def call_with_retry(client, fn, max_retries=6, initial_delay=4.0):
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


def run_ddx(client, model, chart):
    prompt = DDX_PROMPT.replace("{CHART}", chart)
    def call():
        return client.messages.create(model=model, max_tokens=8000,
                                       messages=[{"role": "user", "content": prompt}])
    resp = call_with_retry(client, call)
    parsed = extract_json(resp.content[0].text)
    return parsed.get("differential", []), {
        "input_tokens": resp.usage.input_tokens,
        "output_tokens": resp.usage.output_tokens,
    }


def detects_aki(ddx, k=15):
    """Return (rank_or_None, matched_dx_string) for first AKI mention in top-k."""
    for entry in ddx[:k]:
        dx_text = entry.get("diagnosis", "")
        if AKI_DETECT_PATTERN.search(dx_text):
            return entry.get("rank"), dx_text
    return None, None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="haiku", choices=list(MODELS.keys()))
    parser.add_argument("--cutoffs", nargs="+", default=["admit", "plus24h"],
                        choices=["admit", "plus24h", "plus48h", "pre_discharge"])
    args = parser.parse_args()

    load_dotenv(ROOT.parent / "prototype_a" / ".env", override=True)
    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")

    client = Anthropic()
    model_id = MODELS[args.model]

    case_dirs = sorted(d for d in DATA.iterdir() if d.is_dir())
    print(f"AKI detection test: {len(case_dirs)} cases × {len(args.cutoffs)} cutoff(s) with {args.model}\n")

    # Per-case severity tracking (from selected_admissions_aki.json metadata)
    sel = json.loads((ROOT / "selected_admissions_aki.json").read_text())
    severity_by_hadm = {str(s["hadm_id"]): (
        "severe" if s.get("ratio", 0) >= 3.0 else
        "moderate" if s.get("ratio", 0) >= 2.0 else
        "mild"
    ) for s in sel}

    results = {c: {} for c in args.cutoffs}
    in_total = out_total = 0

    for case_dir in case_dirs:
        hadm_id = case_dir.name
        sev = severity_by_hadm.get(hadm_id, "?")
        print(f"=== {hadm_id} [severity={sev}] ===")

        for cutoff in args.cutoffs:
            chart_path = case_dir / f"{cutoff}.input.txt"
            if not chart_path.exists():
                continue
            chart = chart_path.read_text()
            try:
                ddx, usage = run_ddx(client, model_id, chart)
                in_total += usage["input_tokens"]
                out_total += usage["output_tokens"]
            except Exception as e:
                print(f"  {cutoff:<12s} ERROR: {e}")
                continue

            rank_30, dx_text_30 = detects_aki(ddx, k=30)
            rank_15, _ = detects_aki(ddx, k=15)
            rank_5, _ = detects_aki(ddx, k=5)

            results[cutoff][hadm_id] = {
                "severity": sev,
                "ddx_top5": [{"rank": e.get("rank"), "diagnosis": e.get("diagnosis", "")} for e in ddx[:5]],
                "aki_rank": rank_30,
                "aki_dx_text": dx_text_30,
                "hit@5": rank_5 is not None,
                "hit@15": rank_15 is not None,
                "hit@30": rank_30 is not None,
            }

            verdict = "✓ caught" if rank_30 else "✗ missed"
            print(f"  {cutoff:<12s} {verdict}  rank={rank_30}  dx={dx_text_30[:60] if dx_text_30 else '—'}")

    # Aggregate
    print(f"\n=== AGGREGATE (model: {args.model}) ===")
    print(f"{'Cutoff':<15s}  {'hit@5':>10s}  {'hit@15':>10s}  {'hit@30':>10s}")
    for cutoff in args.cutoffs:
        rows = list(results[cutoff].values())
        if not rows:
            continue
        h5 = sum(r["hit@5"] for r in rows)
        h15 = sum(r["hit@15"] for r in rows)
        h30 = sum(r["hit@30"] for r in rows)
        n = len(rows)
        print(f"  {cutoff:<13s}  {h5}/{n} ({h5/n:.0%})  {h15}/{n} ({h15/n:.0%})  {h30}/{n} ({h30/n:.0%})")

    # By severity
    print(f"\n=== By severity (hit@30) ===")
    for cutoff in args.cutoffs:
        for sev in ["severe", "moderate", "mild"]:
            sev_rows = [r for r in results[cutoff].values() if r["severity"] == sev]
            if not sev_rows:
                continue
            h = sum(r["hit@30"] for r in sev_rows)
            n = len(sev_rows)
            print(f"  {cutoff:<13s}  {sev:<10s}  {h}/{n} ({h/n:.0%})")

    print(f"\nTokens: in={in_total:,}  out={out_total:,}")
    out_path = ROOT / f"results_aki_{args.model}_nephro_top30.json"
    out_path.write_text(json.dumps(results, indent=2, default=str))
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
