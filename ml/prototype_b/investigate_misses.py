"""For each missed gold diagnosis, ask Claude: 'Is there enough evidence in the
chart to reasonably predict this diagnosis?'

This separates two failure modes:
  - DATA_MISSING:  chart lacks the signals needed → not the model's fault
  - MODEL_FAILURE: chart contains evidence but model didn't surface it → model issue

Output: investigate_report.md with per-miss categorization.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

from anthropic import APIError, Anthropic
from dotenv import load_dotenv

ROOT = Path(__file__).parent
DATA = ROOT / "data"
RESULTS = ROOT / "results_haiku.json"
OUT = ROOT / "investigate_report.md"

MODEL = "claude-sonnet-4-6"   # use Sonnet for judging — better at clinical reasoning

JUDGE_PROMPT = """You are a senior internal medicine physician auditing whether a clinical chart contains enough evidence to reasonably predict a specific diagnosis.

GOLD DIAGNOSIS (this is the eventual confirmed diagnosis at discharge):
  ICD code: {ICD_CODE}
  Title: {GOLD_TITLE}

THE CHART AVAILABLE TO A PHYSICIAN AT THIS POINT (everything written, ordered, or resulted up to pre-discharge — but NO discharge summary Assessment/Plan, NO Discharge Diagnoses):
---
{CHART}
---

Question: based ONLY on the chart above, is there enough clinical evidence to reasonably suspect, work up for, or diagnose the GOLD DIAGNOSIS?

Evaluate honestly:
- EVIDENCE_SUFFICIENT: chart contains specific findings (lab values, imaging findings, symptoms, exam findings, prior history) that point to this diagnosis. A reasonable physician would have considered this dx.
- EVIDENCE_PARTIAL: chart contains some hint or risk factor, but not enough to confidently raise this dx. A physician might or might not consider it.
- EVIDENCE_ABSENT: chart contains no real signal for this diagnosis. Predicting it would require external context (prior records, EKG not in chart, outpatient workup, etc.) or pure guessing.

Return STRICT JSON only:
{{
  "verdict": "EVIDENCE_SUFFICIENT" | "EVIDENCE_PARTIAL" | "EVIDENCE_ABSENT",
  "reason": "one-line citation of the specific finding(s) you used to decide, or what was missing"
}}
"""


def call_with_retry(client, fn, max_retries=5):
    delay = 4.0
    for attempt in range(max_retries):
        try:
            return fn()
        except APIError as e:
            if attempt == max_retries - 1:
                raise
            wait = delay * (2 ** attempt)
            print(f"    retry after {wait:.0f}s ({type(e).__name__})")
            time.sleep(wait)


def judge_evidence(client, chart: str, icd: str, title: str) -> dict:
    prompt = (JUDGE_PROMPT
              .replace("{ICD_CODE}", icd)
              .replace("{GOLD_TITLE}", title)
              .replace("{CHART}", chart))
    def call():
        return client.messages.create(
            model=MODEL,
            max_tokens=400,
            messages=[{"role": "user", "content": prompt}],
        )
    resp = call_with_retry(client, call)
    text = resp.content[0].text.strip()
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.MULTILINE).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Best-effort extract
        m = re.search(r'\{[^}]+\}', text, re.DOTALL)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                pass
        return {"verdict": "PARSE_ERROR", "reason": text[:200]}


def main() -> None:
    load_dotenv(ROOT.parent / "prototype_a" / ".env", override=True)
    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")

    results = json.loads(RESULTS.read_text())
    client = Anthropic()

    # Focus on pre_discharge cutoff (most data, fairest test)
    cutoff = "pre_discharge"
    per_case = results["per_case"][cutoff]

    findings = []
    for hadm_id, case in sorted(per_case.items()):
        if "score" not in case:
            continue
        chart_path = DATA / hadm_id / f"{cutoff}.input.txt"
        if not chart_path.exists():
            continue
        chart = chart_path.read_text()

        gold = case["gold_acute"]
        ranks = case["score"]["matched_ranks"]
        flags = case["score"].get("high_stakes_flags", [False] * len(gold))

        # Only investigate the MISSES (rank None or > 15)
        for g, rank, is_hs in zip(gold, ranks, flags):
            if rank is not None and rank <= 15:
                continue  # not a miss
            print(f"  judging miss: [{case['bucket']}/{hadm_id}] {g['icd_code']} {g['title'][:50]}")
            verdict = judge_evidence(client, chart, g["icd_code"], g["title"])
            findings.append({
                "hadm_id": hadm_id,
                "bucket": case["bucket"],
                "icd_code": g["icd_code"],
                "title": g["title"],
                "high_stakes": is_hs,
                "matched_rank": rank,
                "verdict": verdict.get("verdict", ""),
                "reason": verdict.get("reason", ""),
            })

    # Aggregate
    counts: dict[str, int] = {}
    counts_hs: dict[str, int] = {}
    for f in findings:
        counts[f["verdict"]] = counts.get(f["verdict"], 0) + 1
        if f["high_stakes"]:
            counts_hs[f["verdict"]] = counts_hs.get(f["verdict"], 0) + 1

    # Render
    lines = ["# Miss-evidence investigation — pre_discharge cutoff", ""]
    lines.append(f"**Total misses analyzed:** {len(findings)}")
    lines.append("")
    lines.append("## Aggregate verdicts (all misses)")
    lines.append("")
    lines.append("| Verdict | Count | %  |")
    lines.append("|---|---|---|")
    total = max(1, len(findings))
    for k in ["EVIDENCE_SUFFICIENT", "EVIDENCE_PARTIAL", "EVIDENCE_ABSENT", "PARSE_ERROR"]:
        n = counts.get(k, 0)
        lines.append(f"| {k} | {n} | {100*n/total:.0f}% |")
    lines.append("")
    lines.append("**Interpretation:**")
    lines.append("- EVIDENCE_SUFFICIENT misses ⇒ **model failure** (data was there, LLM didn't surface)")
    lines.append("- EVIDENCE_PARTIAL misses ⇒ borderline — LLM had hints but didn't act")
    lines.append("- EVIDENCE_ABSENT misses ⇒ **data limitation** — chart lacks the signal, not the model's fault")
    lines.append("")
    lines.append("## Aggregate verdicts (HIGH-STAKES misses only)")
    lines.append("")
    lines.append("| Verdict | Count | %  |")
    lines.append("|---|---|---|")
    n_hs = sum(1 for f in findings if f["high_stakes"])
    total_hs = max(1, n_hs)
    for k in ["EVIDENCE_SUFFICIENT", "EVIDENCE_PARTIAL", "EVIDENCE_ABSENT", "PARSE_ERROR"]:
        n = counts_hs.get(k, 0)
        lines.append(f"| {k} | {n} | {100*n/total_hs:.0f}% |")
    lines.append("")

    lines.append("## Per-miss detail")
    lines.append("")
    lines.append("| Bucket | ICD | Diagnosis | Verdict | Reason |")
    lines.append("|---|---|---|---|---|")
    for f in findings:
        marker = "🔴 " if f["high_stakes"] else ""
        verdict_emoji = {
            "EVIDENCE_SUFFICIENT": "❌ MODEL",
            "EVIDENCE_PARTIAL": "⚠️ PARTIAL",
            "EVIDENCE_ABSENT": "🔄 NO_DATA",
        }.get(f["verdict"], f["verdict"])
        title = f["title"][:60]
        reason = f["reason"].replace("|", "/")[:140]
        lines.append(f"| {marker}{f['bucket']} | {f['icd_code']} | {title} | {verdict_emoji} | {reason} |")

    OUT.write_text("\n".join(lines))
    print(f"\n✓ {len(findings)} misses analyzed")
    print(f"  EVIDENCE_SUFFICIENT (model failure): {counts.get('EVIDENCE_SUFFICIENT', 0)}")
    print(f"  EVIDENCE_PARTIAL: {counts.get('EVIDENCE_PARTIAL', 0)}")
    print(f"  EVIDENCE_ABSENT (data limit):       {counts.get('EVIDENCE_ABSENT', 0)}")
    print(f"  PARSE_ERROR: {counts.get('PARSE_ERROR', 0)}")
    print(f"\nReport: {OUT}")


if __name__ == "__main__":
    main()
