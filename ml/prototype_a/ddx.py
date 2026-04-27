"""Run the DDx loop over prepared cases.

For each case in gold.json:
  1. Read the input chart
  2. Call Claude with the DDx prompt
  3. Parse JSON output
  4. Score: did the gold diagnosis appear in top 1 / 3 / 5? (LLM-judged for synonym tolerance)
  5. Write results.md

Usage:
    python ddx.py                  # all cases, default model
    python ddx.py --model haiku    # explicit model
    python ddx.py --case 03        # single case
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from anthropic import Anthropic
from dotenv import load_dotenv

ROOT = Path(__file__).parent
PROMPTS_DIR = ROOT / "prompts"
GOLD_PATH = ROOT / "gold.json"
RESULTS_PATH = ROOT / "results.md"

MODELS = {
    "haiku": "claude-haiku-4-5",
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-7",
}


def load_prompt(chart: str) -> str:
    template = (PROMPTS_DIR / "ddx_v1.txt").read_text(encoding="utf-8")
    return template.replace("{CHART}", chart)


def _extract_json(text: str) -> dict[str, Any]:
    """Best-effort JSON extraction from a model response.

    Handles: code fences, leading/trailing prose, the model adding extra commas
    or missing them. Falls back to grabbing the first {...} block.
    """
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.MULTILINE).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Find the outermost {...} block by brace counting.
    start = text.find("{")
    if start == -1:
        raise ValueError("no JSON object in model response")
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
        raise ValueError("unbalanced braces in model response")
    block = text[start:end]
    try:
        return json.loads(block)
    except json.JSONDecodeError:
        # Last resort: strip trailing commas before } or ].
        block = re.sub(r",(\s*[}\]])", r"\1", block)
        return json.loads(block)


def run_ddx(client: Anthropic, model: str, chart: str) -> tuple[dict[str, Any], dict[str, int]]:
    prompt = load_prompt(chart)
    resp = client.messages.create(
        model=model,
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}],
    )
    text = resp.content[0].text.strip()
    parsed = _extract_json(text)
    usage = {
        "input_tokens": resp.usage.input_tokens,
        "output_tokens": resp.usage.output_tokens,
    }
    return parsed, usage


def judge_match(
    client: Anthropic, model: str, gold_terms: list[str], candidate: str
) -> bool:
    """Ask the judge whether candidate matches any of the gold terms.

    Gold terms are extracted from MTSamples title + keywords, so they're a mix
    of diagnoses, chief complaints, and anatomy. Match if the candidate is a
    clinically reasonable diagnosis for any one of them.
    """
    terms_block = "\n".join(f"- {t}" for t in gold_terms)
    prompt = (
        f"Gold reference (any of these — diagnosis, complaint, or related anatomy):\n"
        f"{terms_block}\n\n"
        f"Candidate diagnosis: {candidate}\n\n"
        "Is the candidate a clinically reasonable diagnosis that explains, "
        "is equivalent to, or is a specific form of any term in the gold list? "
        "Answer with a single word: YES or NO."
    )
    resp = client.messages.create(
        model=model,
        max_tokens=10,
        messages=[{"role": "user", "content": prompt}],
    )
    answer = resp.content[0].text.strip().upper()
    return answer.startswith("YES")


def score(
    client: Anthropic,
    judge_model: str,
    gold_terms: list[str],
    differential: list[dict[str, Any]],
) -> dict[str, Any]:
    hit_rank: int | None = None
    for entry in differential:
        rank = entry.get("rank")
        candidate = entry.get("diagnosis", "")
        if judge_match(client, judge_model, gold_terms, candidate):
            hit_rank = rank
            break
    return {
        "hit_rank": hit_rank,
        "hit_at_1": hit_rank is not None and hit_rank == 1,
        "hit_at_3": hit_rank is not None and hit_rank <= 3,
        "hit_at_5": hit_rank is not None and hit_rank <= 5,
    }


def render_results(rows: list[dict[str, Any]], model: str, totals: dict[str, int]) -> str:
    n = len(rows)
    h1 = sum(r["score"]["hit_at_1"] for r in rows)
    h3 = sum(r["score"]["hit_at_3"] for r in rows)
    h5 = sum(r["score"]["hit_at_5"] for r in rows)

    lines: list[str] = []
    lines.append(f"# DDx Results — model: `{model}`")
    lines.append("")
    lines.append(f"**Cases scored:** {n}")
    lines.append("")
    lines.append("| Metric | Hits | Rate |")
    lines.append("|---|---|---|")
    lines.append(f"| hit@1 | {h1}/{n} | {h1/n:.0%} |")
    lines.append(f"| hit@3 | {h3}/{n} | {h3/n:.0%} |")
    lines.append(f"| hit@5 | {h5}/{n} | {h5/n:.0%} |")
    lines.append("")
    lines.append(
        f"**Tokens** — input: {totals['input_tokens']:,} · output: {totals['output_tokens']:,}"
    )
    lines.append("")
    lines.append("## Per-case detail")
    lines.append("")

    for r in rows:
        lines.append(f"### Case {r['idx']} — {r['slug']}")
        lines.append("")
        gold_str = ", ".join(r["gold_terms"][:6])
        lines.append(f"**Gold terms:** {gold_str}")
        lines.append("")
        hit_str = (
            f"hit at rank **{r['score']['hit_rank']}**"
            if r["score"]["hit_rank"] is not None
            else "**MISS**"
        )
        lines.append(f"**Result:** {hit_str}")
        lines.append("")
        lines.append("| Rank | Diagnosis | Reasoning |")
        lines.append("|---|---|---|")
        for entry in r["differential"]:
            d = entry.get("diagnosis", "").replace("|", "/")
            why = entry.get("reasoning", "").replace("|", "/")
            lines.append(f"| {entry.get('rank', '?')} | {d} | {why} |")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="haiku", choices=list(MODELS.keys()))
    parser.add_argument(
        "--judge",
        default="haiku",
        choices=list(MODELS.keys()),
        help="model for synonym judging (default haiku — cheap)",
    )
    parser.add_argument("--case", default=None, help="run a single case id, e.g. 03")
    args = parser.parse_args()

    load_dotenv(ROOT / ".env", override=True)
    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set. Copy .env.example to .env and fill it in.")

    if not GOLD_PATH.exists():
        sys.exit(f"{GOLD_PATH} missing. Run prepare_cases.py first.")

    gold = json.loads(GOLD_PATH.read_text(encoding="utf-8"))
    items = sorted(gold.items())
    if args.case:
        items = [(k, v) for k, v in items if k == args.case]
        if not items:
            sys.exit(f"Case id '{args.case}' not in gold.json")

    client = Anthropic()
    model_id = MODELS[args.model]
    judge_id = MODELS[args.judge]

    totals = {"input_tokens": 0, "output_tokens": 0}
    rows: list[dict[str, Any]] = []

    for idx, meta in items:
        chart_path = ROOT / meta["input_path"]
        chart = chart_path.read_text(encoding="utf-8")
        print(f"[ddx ] case {idx} ({meta['slug']})")

        try:
            parsed, usage = run_ddx(client, model_id, chart)
        except Exception as e:
            print(f"  ERROR: {e}")
            continue

        totals["input_tokens"] += usage["input_tokens"]
        totals["output_tokens"] += usage["output_tokens"]

        differential = parsed.get("differential", [])
        gold_terms = meta.get("gold_terms") or [meta.get("primary_dx", "")]
        s = score(client, judge_id, gold_terms, differential)
        print(
            f"  hit_rank={s['hit_rank']}  "
            f"in: {usage['input_tokens']}  out: {usage['output_tokens']}"
        )

        rows.append(
            {
                "idx": idx,
                "slug": meta["slug"],
                "gold_terms": gold_terms,
                "primary_dx": meta.get("primary_dx", gold_terms[0]),
                "differential": differential,
                "score": s,
            }
        )

    out = render_results(rows, args.model, totals)
    RESULTS_PATH.write_text(out, encoding="utf-8")
    print(f"\nResults written to {RESULTS_PATH}")


if __name__ == "__main__":
    main()
