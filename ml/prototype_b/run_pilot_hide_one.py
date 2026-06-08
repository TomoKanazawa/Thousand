"""Run the 5-patient hide-one-dx pilot through Claude Haiku.

For each case:
  - Chart with the hidden dx scrubbed (chart.txt)
  - Visible dx list as the "team's working diagnoses" (visible_dx.json)
  - Ask Haiku for top-10 additional dx the team may have missed
  - Use Haiku as a judge for semantic match against hidden_dx.json
  - Report Hit@1 and Hit@3

Outputs:
  pilot_hide_one/results_haiku.json   (per-case raw output + match decisions)
  Prints a summary table to stdout.
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

ROOT = Path(__file__).resolve().parent
PILOT = ROOT / "pilot_hide_one"
MODEL = "claude-haiku-4-5"

ASSIST_PROMPT = """You are a senior internal medicine physician reviewing a patient's chart as a SAFETY-NET CHECK.

The primary clinical team has already documented the following diagnoses for this patient (these are KNOWN — the team has already identified them):

DOCUMENTED DIAGNOSES:
{KNOWN_LIST}

Your job: review the chart and identify any ADDITIONAL acute diagnoses present in this patient that the clinical team may have missed or not yet documented. These would be the diagnoses where a second-opinion copilot adds value.

Do NOT re-list the documented diagnoses. Only list NEW conditions.

Look for evidence of:
- Conditions implied by medications ordered
- Lab abnormalities not yet named
- Imaging findings stated in radiology reports but not in the documented list
- Conditions in PMH that may be active during this admission
- Subtle complications

Return STRICT JSON only:

{
  "additional_diagnoses": [
    {"rank": 1, "diagnosis": "...", "reasoning": "specific chart evidence"},
    {"rank": 2, "diagnosis": "...", "reasoning": "..."}
  ]
}

Provide up to 10 additional diagnoses, ranked by likelihood.

CHART:
---
{CHART}
---
"""

JUDGE_PROMPT = """You judge whether the LLM's "additional diagnoses" caught the hidden diagnosis.

HIDDEN DIAGNOSIS (the patient actually has this, but it was intentionally withheld from the LLM):
{HIDDEN}

LLM's ADDITIONAL DIAGNOSES (ranked):
{CAND_LIST}

Find the rank of the FIRST candidate that clinically refers to the same condition.
Synonyms count. More-specific forms of the same condition count. Different organ systems / different mechanisms do NOT count.

Return STRICT JSON only:
{"matched_rank": <int>}
Use -1 if no candidate matches.
"""


def call_with_retry(fn, max_retries=5, initial_delay=4.0):
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


def run_case(client, hadm_id: str) -> dict:
    case_dir = PILOT / hadm_id
    chart = (case_dir / "chart.txt").read_text()
    visible = json.loads((case_dir / "visible_dx.json").read_text())
    hidden = json.loads((case_dir / "hidden_dx.json").read_text())

    known_list = "\n".join(f"- {d['title']}" for d in visible)

    prompt = ASSIST_PROMPT.replace("{KNOWN_LIST}", known_list).replace(
        "{CHART}", chart
    )

    print(f"  [{hadm_id}] generating differential …")
    resp = call_with_retry(
        lambda: client.messages.create(
            model=MODEL,
            max_tokens=3500,
            messages=[{"role": "user", "content": prompt}],
        )
    )
    raw = resp.content[0].text
    try:
        parsed = extract_json(raw)
    except Exception as e:
        return {
            "hadm_id": hadm_id,
            "hidden": hidden["title"],
            "error": f"parse: {e}",
            "raw": raw,
        }
    candidates = parsed.get("additional_diagnoses", [])

    # Judge
    cand_list = "\n".join(
        f"  {c.get('rank','?')}. {c.get('diagnosis','')}" for c in candidates
    )
    judge_prompt = JUDGE_PROMPT.replace("{HIDDEN}", hidden["title"]).replace(
        "{CAND_LIST}", cand_list
    )
    print(f"  [{hadm_id}] judging match …")
    jresp = call_with_retry(
        lambda: client.messages.create(
            model=MODEL,
            max_tokens=500,
            messages=[{"role": "user", "content": judge_prompt}],
        )
    )
    try:
        jparsed = extract_json(jresp.content[0].text)
        matched_rank = int(jparsed.get("matched_rank", -1))
    except Exception as e:
        matched_rank = -1
        print(f"    judge parse fail: {e}")

    return {
        "hadm_id": hadm_id,
        "hidden": hidden["title"],
        "visible": [d["title"] for d in visible],
        "candidates": candidates,
        "matched_rank": matched_rank,
        "hit_at_1": matched_rank == 1,
        "hit_at_3": 1 <= matched_rank <= 3,
        "hit_at_5": 1 <= matched_rank <= 5,
        "hit_at_10": 1 <= matched_rank <= 10,
    }


def main() -> None:
    load_dotenv(ROOT.parent / "prototype_a" / ".env", override=True)
    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")
    client = Anthropic()

    manifest = json.loads((PILOT / "manifest.json").read_text())
    results = []
    for entry in manifest:
        try:
            result = run_case(client, str(entry["hadm_id"]))
            results.append(result)
        except Exception as e:
            print(f"  [{entry['hadm_id']}] ERROR: {e}")
            results.append({"hadm_id": entry["hadm_id"], "error": str(e)})

    out = PILOT / "results_haiku.json"
    out.write_text(json.dumps(results, indent=2))
    print(f"\nWrote {out}\n")

    # Summary
    print(f"{'hadm_id':<11} {'hidden':<55} {'rank':>5} h@1 h@3 h@5 h@10")
    print("-" * 95)
    hits = {"h1": 0, "h3": 0, "h5": 0, "h10": 0}
    for r in results:
        if "error" in r and "hidden" not in r:
            print(f"{r['hadm_id']:<11} ERROR: {r['error']}")
            continue
        rank = r.get("matched_rank", -1)
        rank_s = str(rank) if rank > 0 else "-"
        h1 = "✓" if r.get("hit_at_1") else " "
        h3 = "✓" if r.get("hit_at_3") else " "
        h5 = "✓" if r.get("hit_at_5") else " "
        h10 = "✓" if r.get("hit_at_10") else " "
        hits["h1"] += int(r.get("hit_at_1", False))
        hits["h3"] += int(r.get("hit_at_3", False))
        hits["h5"] += int(r.get("hit_at_5", False))
        hits["h10"] += int(r.get("hit_at_10", False))
        print(
            f"{r['hadm_id']:<11} {r['hidden'][:55]:<55} {rank_s:>5}  {h1}   {h3}   {h5}   {h10}"
        )
    n = sum(1 for r in results if "hidden" in r)
    print("-" * 95)
    print(f"Hit@1: {hits['h1']}/{n}   Hit@3: {hits['h3']}/{n}   Hit@5: {hits['h5']}/{n}   Hit@10: {hits['h10']}/{n}")


if __name__ == "__main__":
    main()
