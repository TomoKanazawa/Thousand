"""Assist-mode benchmark: simulate the realistic copilot scenario.

Setup:
  - The physician has already identified most diagnoses (we GIVE these to the LLM)
  - The LLM's job is to surface the few diagnoses the physician would have MISSED
  - This is the realistic use of a missed-diagnosis copilot

For each case:
  1. Load the gold acute diagnoses
  2. Randomly select K diagnoses to HIDE (simulate physician misses)
  3. Show LLM: chart + the REMAINING gold dx ("physician's working diagnosis list")
  4. Ask LLM: what other diagnoses are present that the team may have missed?
  5. Score: did the LLM surface the hidden ones?

This is the metric that maps directly to product value: "given what the
physician already knows, what does the copilot add?"

Defaults: hide K=2 random gold dx per case, ask LLM for top 10 additions,
score recall on the hidden subset.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import time
from pathlib import Path

from anthropic import APIError, Anthropic
from dotenv import load_dotenv

ROOT = Path(__file__).parent
DATA = ROOT / "data"

MODELS = {
    "haiku": "claude-haiku-4-5",
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-7",
}

CUTOFFS = ["admit", "plus24h", "plus48h", "pre_discharge"]

# High-stakes ICD prefixes
HIGH_STAKES_ICD10 = [
    "A40", "A41", "B37", "C", "D62", "D63", "D69", "E87",
    "G93", "F05", "I21", "I22", "I26", "I46", "I50", "I63",
    "I61", "J12", "J13", "J14", "J15", "J16", "J17", "J18",
    "J93", "J96", "K56", "K70", "K72", "K85", "K92", "N17",
    "N39", "R57",
]
HIGH_STAKES_ICD9 = [
    "038", "584", "428", "410", "411", "415", "433", "434",
    "431", "480", "481", "482", "483", "484", "485", "486",
    "507", "518", "578", "577", "572.2", "293", "348", "042",
    "112", "250.1", "250.2", "260", "261", "262", "263",
    "276", "278", "285", "286", "287", "288",
]
HIGH_STAKES_ICD9 += [str(c) for c in range(140, 210)]


def is_high_stakes(icd: str, ver: int) -> bool:
    code = str(icd).strip()
    table = HIGH_STAKES_ICD9 if ver == 9 else HIGH_STAKES_ICD10
    return any(code.startswith(p) for p in table)


ASSIST_PROMPT = """You are a senior internal medicine physician reviewing a patient's chart as a SAFETY-NET CHECK.

The primary clinical team has already documented the following diagnoses for this patient (these are KNOWN — the team has already identified them):

DOCUMENTED DIAGNOSES:
{KNOWN_LIST}

Your job: review the chart and identify any ADDITIONAL acute diagnoses present in this patient that the clinical team may have missed or not yet documented. These would be the diagnoses where a second-opinion copilot adds value.

Do NOT re-list the documented diagnoses. Only list NEW conditions.

Look for evidence of:
- Conditions implied by medications ordered (laxatives → constipation; antipsychotics → psych dx; insulin → diabetic complications)
- Lab abnormalities not yet named (specific electrolytes; cytopenias; rising creatinine → AKI)
- Imaging findings stated in radiology reports but not in the documented list
- Conditions in PMH that may be active during this admission
- Subtle complications (mild thrombocytopenia, hypovolemia, vitamin deficiency, mild encephalopathy)

Return STRICT JSON only:

{
  "additional_diagnoses": [
    {"rank": 1, "diagnosis": "...", "reasoning": "specific chart evidence"},
    {"rank": 2, "diagnosis": "...", "reasoning": "..."},
    ...
  ]
}

Provide up to 10 additional diagnoses, ranked by likelihood. If the team's list seems complete, return fewer or an empty list.

CHART:
---
{CHART}
---
"""

JUDGE_PROMPT = """You judge whether the LLM's "additional diagnoses" caught the diagnoses that were hidden from it.

HIDDEN DIAGNOSES (the patient actually has these, but they were intentionally withheld from the LLM):
{HIDDEN_LIST}

LLM's ADDITIONAL DIAGNOSES (the dx the LLM surfaced as "team may have missed"):
{CAND_LIST}

For EACH hidden diagnosis, find the rank of the FIRST candidate that clinically refers to the same condition (synonyms count; more-specific forms count). Use -1 if no candidate matches.

Be reasonably lenient on synonyms but strict on different organ systems / different mechanisms.

Return STRICT JSON only:
{"matches": [{"hidden_idx": 0, "matched_rank": 3}, {"hidden_idx": 1, "matched_rank": -1}, ...]}
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
    if start == -1:
        raise ValueError("no JSON")
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


def run_assist(client, model, chart, known_dx):
    known_list = "\n".join(f"  - {d['title']}" for d in known_dx) if known_dx else "  (none yet documented)"
    prompt = (ASSIST_PROMPT
              .replace("{KNOWN_LIST}", known_list)
              .replace("{CHART}", chart))
    def call():
        return client.messages.create(model=model, max_tokens=3500,
                                       messages=[{"role": "user", "content": prompt}])
    resp = call_with_retry(client, call)
    parsed = extract_json(resp.content[0].text)
    return parsed.get("additional_diagnoses", []), {
        "input_tokens": resp.usage.input_tokens,
        "output_tokens": resp.usage.output_tokens,
    }


def score_hidden(client, judge_model, candidates, hidden_dx):
    n_hidden = len(hidden_dx)
    if n_hidden == 0:
        return {"n_hidden": 0, "matched_ranks": []}
    hidden_list = "\n".join(f"  [{i}] {h['icd_code']} — {h['title']}" for i, h in enumerate(hidden_dx))
    cand_list = "\n".join(f"  Rank {c.get('rank', '?')}: {c.get('diagnosis', '')}" for c in candidates) or "  (none)"
    prompt = (JUDGE_PROMPT.replace("{HIDDEN_LIST}", hidden_list).replace("{CAND_LIST}", cand_list))
    def call():
        return client.messages.create(model=judge_model, max_tokens=1500,
                                       messages=[{"role": "user", "content": prompt}])
    resp = call_with_retry(client, call)
    try:
        parsed = extract_json(resp.content[0].text)
        matches = parsed.get("matches", [])
    except Exception:
        matches = []
    ranks = [None] * n_hidden
    for m in matches:
        i = m.get("hidden_idx")
        r = m.get("matched_rank")
        if isinstance(i, int) and 0 <= i < n_hidden:
            ranks[i] = r if (isinstance(r, int) and r > 0) else None
    return {"n_hidden": n_hidden, "matched_ranks": ranks}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="haiku", choices=list(MODELS.keys()))
    parser.add_argument("--judge", default="haiku", choices=list(MODELS.keys()))
    parser.add_argument("--n", type=int, default=10)
    parser.add_argument("--hide-k", type=int, default=2,
                        help="Hide this many random gold dx per case (default 2)")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--cutoff", default="pre_discharge",
                        choices=CUTOFFS + ["all"],
                        help="Which cutoff to use (default pre_discharge; 'all' runs all)")
    args = parser.parse_args()

    random.seed(args.seed)
    load_dotenv(ROOT.parent / "prototype_a" / ".env", override=True)
    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")

    client = Anthropic()
    model_id = MODELS[args.model]
    judge_id = MODELS[args.judge]

    cutoffs_to_run = CUTOFFS if args.cutoff == "all" else [args.cutoff]
    case_dirs = sorted(d for d in DATA.iterdir() if d.is_dir())[:args.n]
    print(f"Assist mode: {len(case_dirs)} cases × {len(cutoffs_to_run)} cutoff(s) with {args.model}")
    print(f"Hiding K={args.hide_k} random gold dx per case (seed={args.seed})\n")

    results = {c: {} for c in cutoffs_to_run}
    in_total = out_total = 0
    overall = {c: {"n_hidden": 0, "hits_5": 0, "hits_10": 0,
                    "n_hidden_hs": 0, "hits_hs_5": 0, "hits_hs_10": 0}
               for c in cutoffs_to_run}

    for case_dir in case_dirs:
        hadm_id = case_dir.name
        gold = json.loads((case_dir / "gold.json").read_text())["acute_diagnoses"]
        n_gold = len(gold)
        if n_gold < args.hide_k + 1:
            print(f"=== {hadm_id}  SKIPPED (n_gold={n_gold} < hide_k+1={args.hide_k+1}) ===")
            continue

        # Select which to hide — use seed for reproducibility per case
        rng = random.Random(args.seed + int(hadm_id) % 10_000)
        hide_indices = sorted(rng.sample(range(n_gold), args.hide_k))
        hidden_dx = [gold[i] for i in hide_indices]
        known_dx = [gold[i] for i in range(n_gold) if i not in hide_indices]

        # Identify high-stakes among hidden
        hidden_hs_flags = [is_high_stakes(d["icd_code"], d["icd_version"]) for d in hidden_dx]

        print(f"=== {hadm_id}  n_gold={n_gold}  hidden={args.hide_k} "
              f"(HS:{sum(hidden_hs_flags)})  hidden=[{', '.join(h['icd_code'] for h in hidden_dx)}] ===")

        for cutoff in cutoffs_to_run:
            chart = (case_dir / f"{cutoff}.input.txt").read_text()
            try:
                candidates, usage = run_assist(client, model_id, chart, known_dx)
                in_total += usage["input_tokens"]
                out_total += usage["output_tokens"]
                score_res = score_hidden(client, judge_id, candidates, hidden_dx)
            except Exception as e:
                print(f"  {cutoff:<15s} ERROR: {e}")
                results[cutoff][hadm_id] = {"error": str(e)}
                continue

            ranks = score_res["matched_ranks"]
            hits_5 = sum(1 for r in ranks if r is not None and r <= 5)
            hits_10 = sum(1 for r in ranks if r is not None and r <= 10)
            # High-stakes restricted
            hs_hits_5 = sum(1 for r, is_hs in zip(ranks, hidden_hs_flags)
                            if is_hs and r is not None and r <= 5)
            hs_hits_10 = sum(1 for r, is_hs in zip(ranks, hidden_hs_flags)
                             if is_hs and r is not None and r <= 10)
            n_hs = sum(hidden_hs_flags)

            print(f"  {cutoff:<15s} "
                  f"hits@5={hits_5}/{args.hide_k}  hits@10={hits_10}/{args.hide_k}  "
                  f"hs@10={hs_hits_10}/{n_hs}  "
                  f"in:{usage['input_tokens']} out:{usage['output_tokens']}  "
                  f"({len(candidates)} additional dx returned)")

            results[cutoff][hadm_id] = {
                "hidden": hidden_dx,
                "known_count": len(known_dx),
                "candidates": candidates,
                "matched_ranks": ranks,
            }
            overall[cutoff]["n_hidden"] += args.hide_k
            overall[cutoff]["hits_5"] += hits_5
            overall[cutoff]["hits_10"] += hits_10
            overall[cutoff]["n_hidden_hs"] += n_hs
            overall[cutoff]["hits_hs_5"] += hs_hits_5
            overall[cutoff]["hits_hs_10"] += hs_hits_10

    # Aggregate
    print(f"\n=== AGGREGATE (n={len(case_dirs)}, hide_k={args.hide_k}) ===")
    print(f"{'Cutoff':<15s}  {'recall@5':>15s}  {'recall@10':>15s}  {'HS recall@10':>18s}")
    for cutoff in cutoffs_to_run:
        o = overall[cutoff]
        if o["n_hidden"] == 0:
            continue
        r5 = o["hits_5"] / o["n_hidden"]
        r10 = o["hits_10"] / o["n_hidden"]
        hs10 = o["hits_hs_10"] / o["n_hidden_hs"] if o["n_hidden_hs"] else 0
        print(f"  {cutoff:<13s}  "
              f"{o['hits_5']}/{o['n_hidden']} ({r5:.0%})        "
              f"{o['hits_10']}/{o['n_hidden']} ({r10:.0%})        "
              f"{o['hits_hs_10']}/{o['n_hidden_hs']} ({hs10:.0%})")

    print(f"\nTokens: in={in_total:,}  out={out_total:,}")
    out_path = ROOT / f"results_assist_{args.model}.json"
    out_path.write_text(json.dumps(results, indent=2, default=str))
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
