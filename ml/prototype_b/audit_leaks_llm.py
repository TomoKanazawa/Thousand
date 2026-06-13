"""LLM-based leak audit for the hide-one-dx pilot.

For each case, runs a stronger LLM (Sonnet) over the scrubbed chart to find
diagnostic leakage that the regex scrub missed. Two-stage protocol:

  Stage 1 (explicit): direct mentions, synonyms, abbreviations, staging
    language, dangling sentence stubs adjacent to [REDACTED-DX].
  Stage 2 (semantic): disease-specific treatment, pathognomonic findings,
    imaging conclusions, specialty consults, treatment indications.

Decoy calibration: same prompts run with a DIFFERENT diagnosis that the
patient doesn't have. The auditor should return ~0 leaks; any flagged
'leaks' against the decoy quantify the auditor's own false-positive rate.

Net leak score per case = real_leak_count - decoy_leak_count.
Cases with net score >= 1 (or any high-severity hit) get flagged for review.

Outputs (gitignored under pilot_hide_one/):
  leak_audit_sonnet.json   — per-case full audit results
  leak_audit_summary.csv   — one row per case with totals + flags

Usage:
  python3 audit_leaks_llm.py                  # all cases in manifest
  python3 audit_leaks_llm.py --limit 10       # first 10 only (smoke test)
  python3 audit_leaks_llm.py --model haiku    # cheaper auditor (not recommended)
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import random
import re
import sys
import time
from pathlib import Path

from anthropic import APIError, Anthropic
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
PILOT = ROOT / "pilot_hide_one"
MODELS = {
    "haiku": "claude-haiku-4-5",
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-7",
}
SEED = 42

# Decoy diagnoses — picked to be plausible-but-uncommon acute conditions a
# random inpatient is unlikely to also have. Per case, we filter against the
# patient's visible+hidden dx list so we never accidentally pick a real one.
DECOY_POOL = [
    "Acute appendicitis",
    "Bacterial meningitis",
    "Acute pulmonary embolism",
    "Subarachnoid hemorrhage",
    "Acute pancreatitis",
    "Diabetic ketoacidosis",
    "Infective endocarditis",
    "Acute mesenteric ischemia",
    "Aortic dissection",
    "Necrotizing fasciitis",
    "Acute appendicitis",
    "Pheochromocytoma",
    "Tetanus",
    "Hereditary angioedema",
]


STAGE1_PROMPT = """You are auditing a clinical chart for diagnostic leakage. The chart was scrubbed to hide one diagnosis from a downstream reader. Your job: find any EXPLICIT textual leak.

HIDDEN DIAGNOSIS: {target}

Find every passage in the chart that:
- Explicitly NAMES this diagnosis (or a more-specific form of it)
- Uses a standard ABBREVIATION (e.g., PNA, UTI, CHF) for it
- Uses a common SYNONYM
- Uses STAGING/GRADING language specific to it (e.g., "Stage 2 AKI" → AKI)
- Is a TRUNCATION STUB adjacent to [REDACTED-DX] that telegraphs the diagnosis
  (e.g., "CXR shows left lower lobe [REDACTED-DX]" telegraphs pneumonia)

For each finding return:
- line_number (1-indexed, approximate)
- snippet (the exact text from the chart, ≤120 chars)
- leak_type: one of "name", "synonym", "abbreviation", "stage", "truncation_stub"
- severity (0-100): 100 = diagnosis is essentially named outright; 50 = strong but indirect; 20 = weak

If you find no leaks, return an empty list.

Return STRICT JSON only — no commentary, no markdown fences:
{{"leaks": [{{"line_number": int, "snippet": "...", "leak_type": "...", "severity": int}}]}}

CHART:
---
{chart}
---
"""


STAGE2_PROMPT = """You are auditing a clinical chart for SEMANTIC diagnostic leakage. The diagnosis name has already been scrubbed. Your job: find passages that effectively REVEAL the diagnosis without naming it.

HIDDEN DIAGNOSIS: {target}

Flag passages that EFFECTIVELY DECLARE this diagnosis through:
- TREATMENT specific to this diagnosis (e.g., insulin → diabetes; tPA → stroke; RRT/dialysis → AKI/CKD; thrombolytics → PE; vancomycin specifically for MRSA cellulitis)
- PATHOGNOMONIC finding stated as a conclusion (e.g., "CT shows filling defect in pulmonary artery" → PE; "MRI shows leptomeningeal enhancement" → leptomeningeal carcinomatosis)
- IMAGING REPORT CONCLUSION naming an adjacent/related condition that strongly implies the hidden one
- SPECIALTY CONSULT clearly targeting the hidden diagnosis (e.g., "nephrology consult" when hiding AKI)
- TREATMENT INDICATION naming the condition (e.g., "KCl for hypokalemia replacement")
- DISEASE-SPECIFIC MONITORING (e.g., q4h finger sticks → diabetes; serial troponins → MI)
- POST-PROCEDURE CONFIRMATION (e.g., "biopsy showed adenocarcinoma" → cancer)

Do NOT flag:
- Raw lab values, vitals, generic findings — these are normal evidence the downstream LLM should reason from
- Broad-spectrum treatments with many indications (vanc+zosyn is NOT a leak)
- Patient comorbidities/PMH unrelated to the hidden diagnosis
- Symptom descriptions

For each finding return:
- line_number (1-indexed, approximate)
- snippet (≤120 chars)
- leak_type: one of "treatment", "imaging_conclusion", "consult", "indication", "monitoring", "post_procedure"
- severity (0-100): 100 = essentially equivalent to naming the diagnosis; 50 = strong implication; 20 = mild hint

If no semantic leaks, return an empty list.

Return STRICT JSON only:
{{"leaks": [{{"line_number": int, "snippet": "...", "leak_type": "...", "severity": int}}]}}

CHART:
---
{chart}
---
"""


def call_with_retry(fn, max_retries=4, initial_delay=4.0):
    delay = initial_delay
    for attempt in range(max_retries):
        try:
            return fn()
        except APIError as e:
            if attempt == max_retries - 1:
                raise
            wait = delay * (2 ** attempt)
            print(f"    retry after {wait:.0f}s ({type(e).__name__})", file=sys.stderr)
            time.sleep(wait)


def extract_json(text: str) -> dict:
    text = text.strip()
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.MULTILINE).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    if start == -1:
        raise ValueError(f"no JSON: {text[:200]}")
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
    if end == -1:
        raise ValueError("unbalanced braces")
    return json.loads(text[start:end])


def run_stage(client, model: str, chart: str, target: str, stage: int) -> list[dict]:
    prompt = (STAGE1_PROMPT if stage == 1 else STAGE2_PROMPT).format(
        target=target, chart=chart
    )
    resp = call_with_retry(
        lambda: client.messages.create(
            model=model,
            max_tokens=2500,
            messages=[{"role": "user", "content": prompt}],
        )
    )
    try:
        parsed = extract_json(resp.content[0].text)
    except Exception as e:
        return [{"error": f"parse: {e}", "raw": resp.content[0].text[:400]}]
    leaks = parsed.get("leaks", [])
    if not isinstance(leaks, list):
        return []
    return leaks


def pick_decoy(visible_titles: list[str], hidden_title: str, rng: random.Random) -> str:
    """Pick a decoy not present in this patient's known dx list."""
    in_chart = {hidden_title.lower()} | {t.lower() for t in visible_titles}
    options = [d for d in DECOY_POOL if d.lower() not in in_chart and
               not any(d.lower() in t.lower() or t.lower() in d.lower() for t in in_chart)]
    if not options:
        options = DECOY_POOL  # fallback
    return rng.choice(options)


def audit_case(client, model: str, hadm_id: str, rng: random.Random) -> dict:
    case = PILOT / hadm_id
    chart = (case / "chart.txt").read_text()
    hidden = json.loads((case / "hidden_dx.json").read_text())
    visible = [v["title"] for v in json.loads((case / "visible_dx.json").read_text())]
    decoy = pick_decoy(visible, hidden["title"], rng)

    print(f"  [{hadm_id}] real='{hidden['title'][:40]}' decoy='{decoy[:30]}' …")
    real_s1 = run_stage(client, model, chart, hidden["title"], 1)
    real_s2 = run_stage(client, model, chart, hidden["title"], 2)
    decoy_s1 = run_stage(client, model, chart, decoy, 1)
    decoy_s2 = run_stage(client, model, chart, decoy, 2)

    real_leaks = real_s1 + real_s2
    decoy_leaks = decoy_s1 + decoy_s2
    max_real_sev = max((int(x.get("severity", 0)) for x in real_leaks if "severity" in x), default=0)
    max_decoy_sev = max((int(x.get("severity", 0)) for x in decoy_leaks if "severity" in x), default=0)

    flagged = (len(real_leaks) - len(decoy_leaks)) >= 1 or max_real_sev >= 70

    return {
        "hadm_id": hadm_id,
        "hidden_title": hidden["title"],
        "decoy_title": decoy,
        "real_stage1_leaks": real_s1,
        "real_stage2_leaks": real_s2,
        "decoy_stage1_leaks": decoy_s1,
        "decoy_stage2_leaks": decoy_s2,
        "n_real_leaks": len(real_leaks),
        "n_decoy_leaks": len(decoy_leaks),
        "net_leaks": len(real_leaks) - len(decoy_leaks),
        "max_real_severity": max_real_sev,
        "max_decoy_severity": max_decoy_sev,
        "flagged": flagged,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="sonnet", choices=list(MODELS.keys()))
    parser.add_argument("--limit", type=int, default=None,
                        help="Only audit the first N cases (smoke test).")
    parser.add_argument("--out", default="leak_audit_sonnet.json",
                        help="Output JSON filename (under pilot_hide_one/).")
    args = parser.parse_args()

    load_dotenv(ROOT.parent / "prototype_a" / ".env", override=True)
    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")

    rng = random.Random(SEED)
    client = Anthropic()
    manifest = json.loads((PILOT / "manifest.json").read_text())
    if args.limit:
        manifest = manifest[: args.limit]

    # Resume from checkpoint if it exists
    out_path = PILOT / args.out
    results: list[dict] = []
    done_ids: set[str] = set()
    if out_path.exists():
        try:
            results = json.loads(out_path.read_text())
            done_ids = {str(r.get("hadm_id")) for r in results if "hadm_id" in r and "error" not in r}
            print(f"Resuming: {len(done_ids)} cases already audited; skipping them.")
        except Exception:
            print("(could not parse existing output; starting fresh)")
            results = []

    print(f"Auditing {len(manifest)} cases ({len(manifest) - len(done_ids)} remaining) with {MODELS[args.model]} …")

    for i, entry in enumerate(manifest, 1):
        hadm = str(entry["hadm_id"])
        if hadm in done_ids:
            continue
        try:
            results.append(audit_case(client, MODELS[args.model], hadm, rng))
        except BaseException as e:
            # Catch EVERYTHING (incl. KeyboardInterrupt, SystemExit, APIError) so we can checkpoint.
            err_msg = f"{type(e).__name__}: {e}"
            print(f"  [{hadm}] ERROR: {err_msg}", flush=True)
            results.append({"hadm_id": entry["hadm_id"], "error": err_msg})
            if isinstance(e, KeyboardInterrupt):
                out_path.write_text(json.dumps(results, indent=2))
                raise
        # Checkpoint after each case
        out_path.write_text(json.dumps(results, indent=2))
        print(f"  [{i}/{len(manifest)}] checkpoint saved ({len(results)} entries)", flush=True)

    # Summary CSV
    csv_path = PILOT / args.out.replace(".json", "_summary.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["hadm_id", "hidden_title", "decoy_title",
                    "n_real_leaks", "n_decoy_leaks", "net_leaks",
                    "max_real_severity", "max_decoy_severity", "flagged"])
        for r in results:
            if "error" in r and "hidden_title" not in r:
                w.writerow([r["hadm_id"], "ERROR", "", "", "", "", "", "", ""])
                continue
            w.writerow([r["hadm_id"], r["hidden_title"], r["decoy_title"],
                        r["n_real_leaks"], r["n_decoy_leaks"], r["net_leaks"],
                        r["max_real_severity"], r["max_decoy_severity"], r["flagged"]])

    # Headline
    n = sum(1 for r in results if "hidden_title" in r)
    flagged = sum(1 for r in results if r.get("flagged"))
    avg_real = sum(r.get("n_real_leaks", 0) for r in results if "hidden_title" in r) / max(n, 1)
    avg_decoy = sum(r.get("n_decoy_leaks", 0) for r in results if "hidden_title" in r) / max(n, 1)
    print(f"\nAudited {n} cases.")
    print(f"  avg real leaks/case:  {avg_real:.2f}")
    print(f"  avg decoy leaks/case: {avg_decoy:.2f}  (auditor false-positive baseline)")
    print(f"  flagged cases: {flagged}/{n}")
    print(f"\nWrote {PILOT / args.out}")
    print(f"Wrote {csv_path}")


if __name__ == "__main__":
    main()
