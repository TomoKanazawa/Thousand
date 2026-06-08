"""Hide-one-dx pilot with self-reported confidence + threshold sweep.

Each candidate diagnosis now carries a `confidence` field (0-100) which the
LLM is asked to calibrate as "probability this diagnosis is actually
present given the chart evidence." We then sweep thresholds T and ask:

  At threshold T, of the candidates that the LLM would actually surface
  (confidence >= T), how often is the hidden dx among them, and how much
  "noise" (other above-threshold candidates per case) does that cost?

Trade-off captured:
  - Coverage (Hit@k@T): how many cases still catch the hidden dx
  - Noise budget: avg # non-hidden candidates >= T per case (proxy for alert load)
  - Surfacing rate (Surface@T): % of cases where ANYTHING is surfaced

Output:
  pilot_hide_one/results_haiku_confidence.json   — raw per-case + per-candidate scores
  pilot_hide_one/threshold_sweep.md              — summary table
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

Your job: identify any ADDITIONAL acute diagnoses present in this patient that the clinical team may have missed.

Do NOT re-list the documented diagnoses. Only list NEW conditions.

For EACH candidate, also report a **confidence** score (0-100) that represents your estimated PROBABILITY this diagnosis is actually present in this patient based on the chart evidence.

CALIBRATION GUIDE (be honest — clinicians will ignore your tool if you cry wolf):
- 90-100: textbook pattern, multiple corroborating findings, unambiguous
- 70-89: specific findings clearly support it, but not pathognomonic
- 50-69: evidence is suggestive but ambiguous; could go either way
- 30-49: weak signal; you'd mention it to be thorough but wouldn't bet on it
- Below 30: don't include it — too speculative to surface to a busy clinician

Return STRICT JSON only:

{
  "additional_diagnoses": [
    {"rank": 1, "diagnosis": "...", "confidence": 85, "reasoning": "specific chart evidence"},
    {"rank": 2, "diagnosis": "...", "confidence": 60, "reasoning": "..."}
  ]
}

Provide up to 10 additional diagnoses, ranked by likelihood. If nothing rises above ~30 confidence, return fewer or an empty list — DO NOT pad with low-confidence guesses.

CHART:
---
{CHART}
---
"""

JUDGE_PROMPT = """You judge whether the LLM's "additional diagnoses" caught the hidden diagnosis.

HIDDEN DIAGNOSIS (the patient actually has this, intentionally withheld from the LLM):
{HIDDEN}

LLM's ADDITIONAL DIAGNOSES (with rank):
{CAND_LIST}

Find the rank of the FIRST candidate that clinically refers to the same condition.
Synonyms count. More-specific forms count. Different organ systems / mechanisms do NOT count.

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
    parsed = extract_json(raw)
    candidates = parsed.get("additional_diagnoses", [])

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
    jparsed = extract_json(jresp.content[0].text)
    matched_rank = int(jparsed.get("matched_rank", -1))

    hit_conf = None
    if matched_rank > 0:
        # confidence of the matched candidate
        for c in candidates:
            if c.get("rank") == matched_rank:
                hit_conf = c.get("confidence")
                break

    return {
        "hadm_id": hadm_id,
        "hidden": hidden["title"],
        "visible": [d["title"] for d in visible],
        "candidates": candidates,
        "matched_rank": matched_rank,
        "matched_confidence": hit_conf,
    }


def sweep_thresholds(results: list[dict], top_k: int = 3) -> str:
    """Build a markdown table sweeping confidence thresholds."""
    thresholds = [0, 30, 40, 50, 60, 70, 75, 80, 85, 90]
    lines = [
        "# Confidence-threshold sweep — pilot_hide_one (Haiku)",
        "",
        f"Sweep at Hit@{top_k}. For each threshold T:",
        "- **Caught**: hidden dx is in top-K of candidates with confidence ≥ T",
        "- **Noise/case**: average # of NON-hidden candidates with confidence ≥ T per case (alert burden)",
        "- **Silent**: # of cases where NO candidate has confidence ≥ T (model 'declines to suggest')",
        "",
        f"| Threshold | Caught (Hit@{top_k}@T) | Hidden's confidence | Noise/case | Silent | Net signal |",
        "|---|---|---|---|---|---|",
    ]
    for T in thresholds:
        caught = 0
        noise_counts = []
        silent = 0
        hidden_confs = []
        for r in results:
            cands = r.get("candidates", [])
            above = [c for c in cands if (c.get("confidence") or 0) >= T]
            if not above:
                silent += 1
            # Hit@K@T: was the matched (hidden) dx in top-K AND above threshold?
            rank = r.get("matched_rank", -1)
            conf = r.get("matched_confidence") or 0
            if 1 <= rank <= top_k and conf >= T:
                caught += 1
                hidden_confs.append(conf)
            # noise = above-threshold candidates EXCLUDING the matched one
            noise = len([c for c in above if c.get("rank") != rank])
            noise_counts.append(noise)
        avg_noise = sum(noise_counts) / len(noise_counts) if noise_counts else 0
        conf_str = (
            f"{min(hidden_confs)}–{max(hidden_confs)}" if hidden_confs else "—"
        )
        # Net signal = catch rate / (1 + noise/case)
        catch_rate = caught / len(results)
        net = catch_rate / (1 + avg_noise)
        lines.append(
            f"| ≥{T} | {caught}/{len(results)} ({100*catch_rate:.0f}%) | {conf_str} | {avg_noise:.1f} | {silent}/{len(results)} | {net:.3f} |"
        )
    return "\n".join(lines)


def main() -> None:
    load_dotenv(ROOT.parent / "prototype_a" / ".env", override=True)
    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")
    client = Anthropic()

    manifest = json.loads((PILOT / "manifest.json").read_text())
    results = []
    for entry in manifest:
        try:
            results.append(run_case(client, str(entry["hadm_id"])))
        except Exception as e:
            print(f"  [{entry['hadm_id']}] ERROR: {e}")

    (PILOT / "results_haiku_confidence.json").write_text(json.dumps(results, indent=2))

    sweep_md = sweep_thresholds(results, top_k=3)
    (PILOT / "threshold_sweep.md").write_text(sweep_md)
    print()
    print(sweep_md)


if __name__ == "__main__":
    main()
