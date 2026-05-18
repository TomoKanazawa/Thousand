"""Run the LLM DDx benchmark across MIMIC cases at multiple cutoffs.

For each admission in data/<hadm_id>/:
  - For each cutoff (admit / plus24h / plus48h / pre_discharge):
    - Send input.txt to the model, ask for ranked top-15 DDx
    - Score against gold.json's acute_diagnoses
    - Compute recall@5, recall@10, recall@15

Output: results_<model>.md with the recall curve.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

from anthropic import Anthropic
from dotenv import load_dotenv

ROOT = Path(__file__).parent
DATA = ROOT / "data"

MODELS = {
    "haiku": "claude-haiku-4-5",
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-7",
}

CUTOFFS = ["admit", "plus24h", "plus48h", "pre_discharge"]

# High-stakes diagnostic categories — the conditions that drive
# diagnostic-error harm in the Dalal/Newman-Toker literature and that the
# copilot exists to surface early. ICD prefix → label.
HIGH_STAKES_ICD10 = [
    ("A40", "sepsis"),
    ("A41", "sepsis"),
    ("B37", "candidiasis"),
    ("C", "malignancy"),                 # any cancer
    ("D62", "acute blood loss anemia"),
    ("D63", "anemia of chronic disease (often missed)"),
    ("D69", "thrombocytopenia"),
    ("E87", "electrolyte / fluid"),
    ("G93", "encephalopathy"),
    ("F05", "delirium"),
    ("I21", "MI"),
    ("I22", "MI"),
    ("I26", "PE"),
    ("I46", "cardiac arrest"),
    ("I50", "heart failure"),
    ("I63", "ischemic stroke"),
    ("I61", "hemorrhagic stroke"),
    ("J12", "pneumonia"), ("J13", "pneumonia"), ("J14", "pneumonia"),
    ("J15", "pneumonia"), ("J16", "pneumonia"), ("J17", "pneumonia"), ("J18", "pneumonia"),
    ("J93", "pneumothorax"),
    ("J96", "respiratory failure"),
    ("K56", "obstruction / ileus"),
    ("K70", "alcoholic liver disease (acute)"),
    ("K72", "hepatic failure"),
    ("K85", "pancreatitis"),
    ("K92", "GI bleeding"),
    ("N17", "AKI"),
    ("N39", "UTI"),
    ("R57", "shock"),
    ("R65", "SIRS / sepsis billing"),  # already in exclude, but if it slips through
]
HIGH_STAKES_ICD9 = [
    ("038", "sepsis"),
    ("995.91", "sepsis"), ("995.92", "severe sepsis"),
    ("99591", "sepsis"), ("99592", "severe sepsis"),
    ("584", "AKI"),
    ("428", "heart failure"),
    ("410", "MI"),
    ("411", "unstable angina"),
    ("415.1", "PE"), ("4151", "PE"),
    ("433", "stroke"), ("434", "stroke"),
    ("431", "hemorrhagic stroke"),
    ("480", "pneumonia"), ("481", "pneumonia"), ("482", "pneumonia"),
    ("483", "pneumonia"), ("484", "pneumonia"), ("485", "pneumonia"), ("486", "pneumonia"),
    ("507", "aspiration pneumonia"),
    ("491.21", "COPD exacerbation"),
    ("518.81", "respiratory failure"), ("51881", "respiratory failure"),
    ("518.82", "respiratory failure"), ("51882", "respiratory failure"),
    ("518.4", "pulmonary edema"),
    ("578", "GI bleeding"),
    ("577.0", "pancreatitis"),
    ("572.2", "hepatic encephalopathy"),
    ("293", "delirium"),
    ("348", "encephalopathy"),
    ("042", "HIV"),
    ("250.1", "DKA"), ("2501", "DKA"),
    ("250.2", "HHS"), ("2502", "HHS"),
    ("042", "HIV"),
    ("112.0", "candidiasis"),
    ("042", "HIV"),
    ("140", "cancer"), ("141", "cancer"), ("142", "cancer"), ("143", "cancer"),
    ("144", "cancer"), ("145", "cancer"), ("146", "cancer"), ("147", "cancer"),
    ("148", "cancer"), ("149", "cancer"), ("150", "cancer"), ("151", "cancer"),
    ("152", "cancer"), ("153", "cancer"), ("154", "cancer"), ("155", "cancer"),
    ("156", "cancer"), ("157", "cancer"), ("158", "cancer"), ("159", "cancer"),
    ("160", "cancer"), ("161", "cancer"), ("162", "cancer"), ("163", "cancer"),
    ("164", "cancer"), ("165", "cancer"), ("170", "cancer"), ("171", "cancer"),
    ("172", "cancer"), ("174", "cancer"), ("175", "cancer"), ("176", "cancer"),
    ("179", "cancer"), ("180", "cancer"), ("181", "cancer"), ("182", "cancer"),
    ("183", "cancer"), ("184", "cancer"), ("185", "cancer"), ("186", "cancer"),
    ("187", "cancer"), ("188", "cancer"), ("189", "cancer"), ("190", "cancer"),
    ("191", "cancer"), ("192", "cancer"), ("193", "cancer"), ("194", "cancer"),
    ("195", "cancer"), ("196", "cancer"), ("197", "cancer"), ("198", "cancer"),
    ("199", "cancer"), ("200", "cancer"), ("201", "cancer"), ("202", "cancer"),
    ("203", "cancer"), ("204", "cancer"), ("205", "cancer"), ("206", "cancer"),
    ("207", "cancer"), ("208", "cancer"), ("209", "cancer"),
    ("285.1", "anemia (acute)"),
    ("286", "coagulopathy"),
    ("287", "thrombocytopenia / hemorrhagic"),
    ("288", "neutropenia / leukocyte disorder"),
    ("276", "electrolyte / acid-base disorder"),
    ("783.7", "failure to thrive"),
    ("783.21", "abnormal weight loss"),  # often missed malnutrition
    ("260", "kwashiorkor"),
    ("261", "marasmus"),
    ("262", "severe malnutrition"),
    ("263", "other malnutrition"),
    ("570", "acute liver necrosis"),
    ("571.5", "cirrhosis"), ("5715", "cirrhosis"),
    ("572", "hepatic complications"),
    ("562.13", "diverticulitis with hemorrhage"),
]


def high_stakes_label(icd_code: str, icd_version: int) -> str | None:
    """Return a label if this code is a high-stakes condition, else None."""
    code = str(icd_code).strip()
    if not code:
        return None
    table = HIGH_STAKES_ICD9 if icd_version == 9 else HIGH_STAKES_ICD10
    for prefix, label in table:
        if code.startswith(prefix):
            return label
    return None

DDX_PROMPT = """You are a senior internal medicine physician.

Below is a patient chart, including admission notes, exam, and any available labs/imaging/medications up to a specified cutoff time.

Your task: produce a ranked list of the TOP 15 most likely diagnoses that this patient has (or will be found to have) during this hospitalization. Include:
- The principal/primary admitting diagnosis (most likely cause for hospitalization)
- Any secondary acute diagnoses that the workup suggests or that you would expect to be confirmed during the stay (e.g., AKI, electrolyte derangements, complications)

Return STRICT JSON only, no prose:

{
  "differential": [
    {"rank": 1, "diagnosis": "...", "reasoning": "one short sentence"},
    {"rank": 2, "diagnosis": "...", "reasoning": "..."},
    ...
    {"rank": 15, "diagnosis": "...", "reasoning": "..."}
  ]
}

Be specific (e.g., "septic shock due to UTI" not just "infection"). Use standard medical terminology that would map to ICD codes.

CHART:
---
{CHART}
---
"""

JUDGE_PROMPT = """You match each gold diagnosis to the first clinically equivalent candidate in a ranked differential diagnosis list.

GOLD diagnoses (the patient's actual final diagnoses):
{GOLD_LIST}

CANDIDATE ranked DDx (the LLM's predictions, ordered most-to-least likely):
{CAND_LIST}

For EACH gold diagnosis, find the rank of the FIRST candidate that clinically refers to the same condition (same ICD root, same disease, or candidate is a more-specific form). Use -1 if no candidate matches.

Be reasonably lenient on synonyms but strict on different organ systems / different mechanisms. "Sepsis" matches "septicemia" or "septic shock from X." "AKI" matches "acute renal failure." "Heart failure" does NOT match "ischemic heart disease."

Return STRICT JSON only:
{"matches": [{"gold_idx": 0, "matched_rank": 3}, {"gold_idx": 1, "matched_rank": -1}, ...]}
"""


def extract_json(text: str) -> dict:
    text = text.strip()
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.MULTILINE).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    if start == -1:
        raise ValueError("no JSON object in response")
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


def _call_with_retry(fn, *, max_retries: int = 6, initial_delay: float = 4.0):
    """Retry on OverloadedError / RateLimit / transient API errors."""
    from anthropic import APIError
    delay = initial_delay
    for attempt in range(max_retries):
        try:
            return fn()
        except APIError as e:
            # Catch any anthropic API-side error (overloaded, rate limit, 5xx, etc.)
            if attempt == max_retries - 1:
                raise
            wait = delay * (2 ** attempt)
            print(f"    retry {attempt+1}/{max_retries} after {wait:.0f}s ({type(e).__name__}: {str(e)[:80]})")
            time.sleep(wait)
    raise RuntimeError("unreachable")


def run_ddx(client: Anthropic, model: str, chart: str) -> tuple[list[dict], dict]:
    prompt = DDX_PROMPT.replace("{CHART}", chart)
    def call():
        return client.messages.create(
            model=model,
            max_tokens=4000,
            messages=[{"role": "user", "content": prompt}],
        )
    resp = _call_with_retry(call)
    text = resp.content[0].text
    parsed = extract_json(text)
    usage = {
        "input_tokens": resp.usage.input_tokens,
        "output_tokens": resp.usage.output_tokens,
    }
    diff = parsed.get("differential", [])
    return diff, usage


def score_recall(client: Anthropic, judge_model: str,
                 ddx: list[dict], gold: list[dict]) -> dict:
    """One judge call: match each gold dx to a rank in the DDx list (or -1)."""
    n_gold = len(gold)
    if n_gold == 0:
        return {
            "n_gold": 0,
            "hits_5": 0, "hits_10": 0, "hits_15": 0,
            "recall_5": 0, "recall_10": 0, "recall_15": 0,
            "hits_caseN": 0, "k_caseN": 0, "recall_caseN": 0,
            "n_high_stakes": 0,
            "hits_hs_5": 0, "hits_hs_10": 0, "hits_hs_15": 0,
            "recall_hs_5": None, "recall_hs_10": None, "recall_hs_15": None,
            "n_non_hs": 0,
            "hits_nhs_5": 0, "hits_nhs_10": 0, "hits_nhs_15": 0,
            "recall_nhs_5": None, "recall_nhs_10": None, "recall_nhs_15": None,
            "matched_ranks": [],
            "high_stakes_flags": [],
        }

    gold_list = "\n".join(
        f"  [{i}] {g['icd_code']} — {g['title']}" for i, g in enumerate(gold)
    )
    cand_list = "\n".join(
        f"  Rank {e.get('rank', '?')}: {e.get('diagnosis', '')}" for e in ddx
    )
    prompt = (JUDGE_PROMPT
              .replace("{GOLD_LIST}", gold_list)
              .replace("{CAND_LIST}", cand_list))

    def call():
        return client.messages.create(
            model=judge_model,
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}],
        )
    resp = _call_with_retry(call)
    try:
        parsed = extract_json(resp.content[0].text)
        matches = parsed.get("matches", [])
    except Exception:
        matches = []

    matched_ranks: list[int | None] = [None] * n_gold
    for m in matches:
        idx = m.get("gold_idx")
        rank = m.get("matched_rank")
        if isinstance(idx, int) and 0 <= idx < n_gold:
            matched_ranks[idx] = rank if (isinstance(rank, int) and rank > 0) else None

    # Tag each gold entry as high-stakes or not
    high_stakes_flags = [
        high_stakes_label(g["icd_code"], g["icd_version"]) is not None
        for g in gold
    ]

    def _hits_at(k: int, subset_mask: list[bool] | None = None) -> tuple[int, int]:
        """Return (hits_in_top_k, denominator) optionally restricted to a subset."""
        if subset_mask is None:
            subset_mask = [True] * n_gold
        denom = sum(subset_mask)
        hits = sum(
            1 for r, in_subset in zip(matched_ranks, subset_mask)
            if in_subset and r is not None and r <= k
        )
        return hits, denom

    # All-acute recall
    h5_all, d_all = _hits_at(5)
    h10_all, _ = _hits_at(10)
    h15_all, _ = _hits_at(15)
    # Case-normalized: k = n_gold for this case (or 15, whichever larger)
    k_caseN = max(n_gold, 1)
    h_caseN, _ = _hits_at(k_caseN)
    # High-stakes-only
    h5_hs, d_hs = _hits_at(5, high_stakes_flags)
    h10_hs, _ = _hits_at(10, high_stakes_flags)
    h15_hs, _ = _hits_at(15, high_stakes_flags)
    # Non-high-stakes
    non_hs = [not f for f in high_stakes_flags]
    h5_nhs, d_nhs = _hits_at(5, non_hs)
    h10_nhs, _ = _hits_at(10, non_hs)
    h15_nhs, _ = _hits_at(15, non_hs)

    return {
        "n_gold": n_gold,
        # all acute
        "hits_5": h5_all, "hits_10": h10_all, "hits_15": h15_all,
        "recall_5": h5_all / d_all if d_all else 0,
        "recall_10": h10_all / d_all if d_all else 0,
        "recall_15": h15_all / d_all if d_all else 0,
        # case-normalized (k = n_gold)
        "hits_caseN": h_caseN, "k_caseN": k_caseN,
        "recall_caseN": h_caseN / d_all if d_all else 0,
        # high-stakes only
        "n_high_stakes": d_hs,
        "hits_hs_5": h5_hs, "hits_hs_10": h10_hs, "hits_hs_15": h15_hs,
        "recall_hs_5": h5_hs / d_hs if d_hs else None,
        "recall_hs_10": h10_hs / d_hs if d_hs else None,
        "recall_hs_15": h15_hs / d_hs if d_hs else None,
        # non-high-stakes
        "n_non_hs": d_nhs,
        "hits_nhs_5": h5_nhs, "hits_nhs_10": h10_nhs, "hits_nhs_15": h15_nhs,
        "recall_nhs_5": h5_nhs / d_nhs if d_nhs else None,
        "recall_nhs_10": h10_nhs / d_nhs if d_nhs else None,
        "recall_nhs_15": h15_nhs / d_nhs if d_nhs else None,
        # ranks for inspection
        "matched_ranks": matched_ranks,
        "high_stakes_flags": high_stakes_flags,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="haiku", choices=list(MODELS.keys()))
    parser.add_argument("--judge", default="haiku", choices=list(MODELS.keys()))
    args = parser.parse_args()

    load_dotenv(ROOT.parent / "prototype_a" / ".env", override=True)
    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")

    client = Anthropic()
    model_id = MODELS[args.model]
    judge_id = MODELS[args.judge]

    case_dirs = sorted(d for d in DATA.iterdir() if d.is_dir())
    print(f"Running {len(case_dirs)} cases × {len(CUTOFFS)} cutoffs with {args.model}\n")

    # rows[cutoff][hadm_id] = {ddx, score, gold}
    all_results: dict[str, dict[str, dict]] = {c: {} for c in CUTOFFS}
    in_total = out_total = 0

    for case_dir in case_dirs:
        hadm_id = case_dir.name
        gold_data = json.loads((case_dir / "gold.json").read_text())
        gold_acute = gold_data["acute_diagnoses"]
        print(f"=== {hadm_id} [{gold_data['bucket']}] {len(gold_acute)} acute gold dx ===")

        for cutoff in CUTOFFS:
            chart_path = case_dir / f"{cutoff}.input.txt"
            chart = chart_path.read_text()
            try:
                ddx, usage = run_ddx(client, model_id, chart)
                in_total += usage["input_tokens"]
                out_total += usage["output_tokens"]
            except Exception as e:
                print(f"  {cutoff:<15s} ERROR: {e}")
                all_results[cutoff][hadm_id] = {"error": str(e)}
                continue

            score = score_recall(client, judge_id, ddx, gold_acute)
            n_hs = score.get('n_high_stakes', 0)
            hs_str = (f"hs@15={score.get('hits_hs_15', 0)}/{n_hs}"
                      if n_hs > 0 else "hs@15=—")
            print(f"  {cutoff:<15s} "
                  f"r@5={score['hits_5']}/{score['n_gold']} ({score['recall_5']:.0%})  "
                  f"r@10={score['hits_10']}/{score['n_gold']} ({score['recall_10']:.0%})  "
                  f"r@15={score['hits_15']}/{score['n_gold']} ({score['recall_15']:.0%})  "
                  f"r@N={score['hits_caseN']}/{score['n_gold']} ({score['recall_caseN']:.0%})  "
                  f"{hs_str}  "
                  f"in:{usage['input_tokens']} out:{usage['output_tokens']}")

            all_results[cutoff][hadm_id] = {
                "ddx": ddx,
                "score": score,
                "gold_acute": gold_acute,
                "bucket": gold_data["bucket"],
                "primary_dx": gold_data["primary_dx_desc"],
            }

    # Aggregate
    agg = {}
    for cutoff in CUTOFFS:
        rows = [r for r in all_results[cutoff].values() if "score" in r]
        if not rows:
            agg[cutoff] = None
            continue
        total_gold = sum(r["score"]["n_gold"] for r in rows)
        total_hs = sum(r["score"]["n_high_stakes"] for r in rows)
        total_nhs = sum(r["score"]["n_non_hs"] for r in rows)

        def sum_hits(key):
            return sum(r["score"][key] for r in rows)

        agg[cutoff] = {
            "n_cases": len(rows),
            "total_gold": total_gold,
            "total_high_stakes": total_hs,
            "total_non_hs": total_nhs,
            # All acute
            "hits_5": sum_hits("hits_5"),
            "hits_10": sum_hits("hits_10"),
            "hits_15": sum_hits("hits_15"),
            "recall_5": sum_hits("hits_5") / total_gold if total_gold else 0,
            "recall_10": sum_hits("hits_10") / total_gold if total_gold else 0,
            "recall_15": sum_hits("hits_15") / total_gold if total_gold else 0,
            # Case-normalized
            "hits_caseN": sum_hits("hits_caseN"),
            "recall_caseN": sum_hits("hits_caseN") / total_gold if total_gold else 0,
            # High-stakes
            "hits_hs_5": sum_hits("hits_hs_5"),
            "hits_hs_10": sum_hits("hits_hs_10"),
            "hits_hs_15": sum_hits("hits_hs_15"),
            "recall_hs_5": sum_hits("hits_hs_5") / total_hs if total_hs else 0,
            "recall_hs_10": sum_hits("hits_hs_10") / total_hs if total_hs else 0,
            "recall_hs_15": sum_hits("hits_hs_15") / total_hs if total_hs else 0,
            # Non-high-stakes
            "hits_nhs_5": sum_hits("hits_nhs_5"),
            "hits_nhs_10": sum_hits("hits_nhs_10"),
            "hits_nhs_15": sum_hits("hits_nhs_15"),
            "recall_nhs_5": sum_hits("hits_nhs_5") / total_nhs if total_nhs else 0,
            "recall_nhs_10": sum_hits("hits_nhs_10") / total_nhs if total_nhs else 0,
            "recall_nhs_15": sum_hits("hits_nhs_15") / total_nhs if total_nhs else 0,
        }

    # Render markdown
    lines = [f"# MIMIC-IV DDx Benchmark — model: `{args.model}`", ""]
    lines.append(f"**Cases:** {len(case_dirs)} · **Cutoffs:** {', '.join(CUTOFFS)}")
    lines.append(f"**Tokens:** input {in_total:,} · output {out_total:,}")
    lines.append("")

    lines.append("## All-acute recall (existing metric)")
    lines.append("")
    lines.append("| Cutoff | gold | r@5 | r@10 | r@15 | r@N (case-norm) |")
    lines.append("|---|---|---|---|---|---|")
    for cutoff in CUTOFFS:
        a = agg.get(cutoff)
        if a is None:
            lines.append(f"| {cutoff} | — | — | — | — | — |")
            continue
        lines.append(f"| {cutoff} | {a['total_gold']} | "
                     f"{a['hits_5']}/{a['total_gold']} ({a['recall_5']:.0%}) | "
                     f"{a['hits_10']}/{a['total_gold']} ({a['recall_10']:.0%}) | "
                     f"{a['hits_15']}/{a['total_gold']} ({a['recall_15']:.0%}) | "
                     f"{a['hits_caseN']}/{a['total_gold']} ({a['recall_caseN']:.0%}) |")
    lines.append("")
    lines.append("## High-stakes diagnoses only (Dalal/Newman-Toker target conditions)")
    lines.append("")
    lines.append("AKI · sepsis · pneumonia · respiratory failure · MI · PE · stroke · HF · GI bleed · encephalopathy · cancer · DKA · pancreatitis · hepatic failure · electrolyte derangement · acute anemia.")
    lines.append("")
    lines.append("| Cutoff | gold (hs) | r@5 | r@10 | r@15 |")
    lines.append("|---|---|---|---|---|")
    for cutoff in CUTOFFS:
        a = agg.get(cutoff)
        if a is None: continue
        lines.append(f"| {cutoff} | {a['total_high_stakes']} | "
                     f"{a['hits_hs_5']}/{a['total_high_stakes']} ({a['recall_hs_5']:.0%}) | "
                     f"{a['hits_hs_10']}/{a['total_high_stakes']} ({a['recall_hs_10']:.0%}) | "
                     f"{a['hits_hs_15']}/{a['total_high_stakes']} ({a['recall_hs_15']:.0%}) |")
    lines.append("")
    lines.append("## Non-high-stakes acute diagnoses")
    lines.append("")
    lines.append("| Cutoff | gold (non-hs) | r@5 | r@10 | r@15 |")
    lines.append("|---|---|---|---|---|")
    for cutoff in CUTOFFS:
        a = agg.get(cutoff)
        if a is None: continue
        lines.append(f"| {cutoff} | {a['total_non_hs']} | "
                     f"{a['hits_nhs_5']}/{a['total_non_hs']} ({a['recall_nhs_5']:.0%}) | "
                     f"{a['hits_nhs_10']}/{a['total_non_hs']} ({a['recall_nhs_10']:.0%}) | "
                     f"{a['hits_nhs_15']}/{a['total_non_hs']} ({a['recall_nhs_15']:.0%}) |")

    # Per-case detail
    lines.append("")
    lines.append("## Per-case detail")
    lines.append("")
    for hadm_id in [d.name for d in case_dirs]:
        first_cutoff_data = next((all_results[c].get(hadm_id) for c in CUTOFFS
                                  if "score" in all_results[c].get(hadm_id, {})), None)
        if first_cutoff_data is None:
            continue
        lines.append(f"### {hadm_id} · {first_cutoff_data['bucket']}")
        lines.append(f"**Primary dx:** {first_cutoff_data['primary_dx']}")
        gold = first_cutoff_data["gold_acute"]
        lines.append(f"**Acute gold dx ({len(gold)}):**")
        for g in gold[:15]:
            lines.append(f"  - {g['icd_code']} — {g['title']}")
        lines.append("")
        lines.append("| Cutoff | r@5 | r@10 | r@15 |")
        lines.append("|---|---|---|---|")
        for cutoff in CUTOFFS:
            r = all_results[cutoff].get(hadm_id, {})
            if "score" not in r:
                lines.append(f"| {cutoff} | — | — | — |")
                continue
            s = r["score"]
            lines.append(f"| {cutoff} | {s['hits_5']}/{s['n_gold']} | {s['hits_10']}/{s['n_gold']} | {s['hits_15']}/{s['n_gold']} |")
        lines.append("")

    out_path = ROOT / f"results_{args.model}.md"
    out_path.write_text("\n".join(lines))

    # Per-case JSON for inspection
    json_out = ROOT / f"results_{args.model}.json"
    json_out.write_text(json.dumps({
        "model": args.model,
        "in_tokens": in_total,
        "out_tokens": out_total,
        "agg": agg,
        "per_case": all_results,
    }, indent=2, default=str))

    print(f"\n=== AGGREGATE ===")
    print(f"{'Cutoff':<15s}  {'all r@15':>10s}  {'caseN':>10s}  {'hs r@15':>10s}  {'nhs r@15':>10s}")
    for cutoff in CUTOFFS:
        a = agg.get(cutoff)
        if a:
            print(f"  {cutoff:<13s}  "
                  f"{a['recall_15']:>9.0%}  "
                  f"{a['recall_caseN']:>9.0%}  "
                  f"{a['recall_hs_15']:>9.0%} ({a['hits_hs_15']}/{a['total_high_stakes']})  "
                  f"{a['recall_nhs_15']:>9.0%} ({a['hits_nhs_15']}/{a['total_non_hs']})")

    print(f"\nTotal tokens: in={in_total:,}  out={out_total:,}")
    print(f"Results: {out_path}")


if __name__ == "__main__":
    main()
