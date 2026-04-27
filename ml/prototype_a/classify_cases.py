"""Use Haiku to classify each prepared case as a fair DDx test or not.

For each case in gold.json:
  - Send the chart + criteria to Haiku
  - Get verdict: GOOD / ACCEPTABLE / BAD
  - Get short reasoning

Output: classification.json + classification.md
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

ROOT = Path(__file__).parent
GOLD_PATH = ROOT / "gold.json"
OUT_JSON = ROOT / "classification.json"
OUT_MD = ROOT / "classification.md"
MODEL = "claude-haiku-4-5"

PROMPT = """You are screening clinical case charts for use as differential diagnosis (DDx) test cases.

Classify the chart below as one of:

GOOD — Real ambulatory diagnostic encounter. Multiple plausible diagnoses are reasonable given the findings. The diagnosis is NOT explicitly stated in the chart. The chart has enough clinical detail (HPI, exam, sometimes labs) to reason from. Adult patient (>18). Not a procedure/imaging note.

ACCEPTABLE — Fair test but with one minor issue: e.g., one mention of the likely diagnosis in body but DDx still meaningful, OR multi-issue chart with unfocused complaint, OR known chronic condition pre-stated but acute change is ambiguous.

BAD — Fails as DDx test: diagnosis explicitly stated as the consult reason / final dx in body, OR pediatric (<18yo), OR pure trauma case with obvious mechanism, OR procedural/management note (Foley placement, planned surgery, post-op), OR chart too thin (no real HPI), OR purely counseling visit.

Output ONLY valid JSON, no prose:

{
  "verdict": "GOOD" | "ACCEPTABLE" | "BAD",
  "primary_chief_complaint": "...",
  "leak_concern": "none" | "minor" | "major",
  "ddx_breadth": "narrow" | "moderate" | "broad",
  "reason": "one sentence"
}

CHART:
---
{CHART}
---
"""


def classify(client: Anthropic, chart: str) -> dict:
    prompt = PROMPT.replace("{CHART}", chart)
    resp = client.messages.create(
        model=MODEL,
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}],
    )
    text = resp.content[0].text.strip()
    # Strip code fences if any
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()
    return json.loads(text), resp.usage.input_tokens, resp.usage.output_tokens


def main() -> None:
    load_dotenv(ROOT / ".env", override=True)
    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")

    gold = json.loads(GOLD_PATH.read_text())
    client = Anthropic()

    results: dict[str, dict] = {}
    in_total = out_total = 0
    counts = {"GOOD": 0, "ACCEPTABLE": 0, "BAD": 0, "ERROR": 0}

    items = sorted(gold.items())
    for idx, meta in items:
        chart = (ROOT / meta["input_path"]).read_text()
        try:
            verdict, in_t, out_t = classify(client, chart)
            in_total += in_t
            out_total += out_t
            v = verdict.get("verdict", "ERROR")
            counts[v] = counts.get(v, 0) + 1
            results[idx] = {
                "slug": meta["slug"],
                **verdict,
            }
            tag = {"GOOD": "✅", "ACCEPTABLE": "⚠️ ", "BAD": "❌", "ERROR": "??"}.get(v, "??")
            print(f"  {tag} {idx} {meta['slug'][:40]:40s} | {verdict.get('reason', '')[:80]}")
        except Exception as e:
            counts["ERROR"] += 1
            results[idx] = {"slug": meta["slug"], "verdict": "ERROR", "error": str(e)}
            print(f"  ?? {idx} {meta['slug'][:40]:40s} | ERROR: {e}")

    OUT_JSON.write_text(json.dumps(results, indent=2))

    # Render markdown
    lines = ["# Case Classification (Haiku-judged)", ""]
    lines.append(f"**Total cases:** {len(results)}")
    lines.append("")
    lines.append("| Verdict | Count |")
    lines.append("|---|---|")
    for v in ["GOOD", "ACCEPTABLE", "BAD", "ERROR"]:
        lines.append(f"| {v} | {counts.get(v, 0)} |")
    lines.append("")
    lines.append(f"**Tokens** — in: {in_total:,} · out: {out_total:,}")
    lines.append("")
    for v_target, header in [("GOOD", "## ✅ GOOD"), ("ACCEPTABLE", "## ⚠️ ACCEPTABLE"), ("BAD", "## ❌ BAD"), ("ERROR", "## ?? ERROR")]:
        rows = [(idx, r) for idx, r in sorted(results.items()) if r.get("verdict") == v_target]
        if not rows:
            continue
        lines.append(header)
        lines.append("")
        lines.append("| # | Slug | CC | Leak | Breadth | Reason |")
        lines.append("|---|---|---|---|---|---|")
        for idx, r in rows:
            lines.append(
                f"| {idx} | {r.get('slug', '')[:35]} | "
                f"{r.get('primary_chief_complaint', '')[:35]} | "
                f"{r.get('leak_concern', '')} | "
                f"{r.get('ddx_breadth', '')} | "
                f"{r.get('reason', '').replace('|', '/')[:90]} |"
            )
        lines.append("")

    OUT_MD.write_text("\n".join(lines))

    print(f"\nDone. {counts['GOOD']} GOOD · {counts['ACCEPTABLE']} ACCEPTABLE · {counts['BAD']} BAD · {counts['ERROR']} ERROR")
    print(f"Tokens: in={in_total:,} out={out_total:,}")
    print(f"Results: {OUT_JSON} and {OUT_MD}")


if __name__ == "__main__":
    main()
