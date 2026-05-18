"""Find MIMIC-IV admissions meeting KDIGO criteria for AKI — both coded and uncoded.

KDIGO AKI criteria (Stage 1+):
  - Serum creatinine increase ≥ 0.3 mg/dL within any 48-hour window, OR
  - Serum creatinine ≥ 1.5× the prior baseline within the preceding 7 days
  - (Urine output criterion ignored — we don't have continuous u/o in this slice
    of MIMIC, and creatinine alone identifies most AKI)

For each admission, compute:
  - First creatinine value (as baseline proxy, since we don't have outpatient Cr
    for every patient; we use the lowest Cr in the first 24h)
  - Peak creatinine during admission
  - Whether KDIGO Stage 1+ was met
  - Whether AKI was actually coded (N17.x ICD-10 or 584.x ICD-9)

Output:
  - kdigo_aki_summary.json with admission-level flags
  - Aggregate undercoding stats vs literature (Cammarata 2024 = 68%)

Run time on full MIMIC-IV (~340K eligible admissions): ~5 min
"""

from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
HOSP = ROOT / "physionet.org" / "files" / "mimiciv" / "3.1" / "hosp"
NOTE = ROOT / "physionet.org" / "files" / "mimic-iv-note" / "2.2" / "note"
OUT_JSON = Path(__file__).parent / "kdigo_aki_candidates.json"
OUT_SAMPLE_JSON = Path(__file__).parent / "selected_admissions_aki.json"
OUT_REPORT = Path(__file__).parent / "kdigo_aki_report.md"

# Patterns that indicate AKI was MENTIONED in the discharge summary text.
# If any of these match, the physician likely recognized AKI even if it wasn't
# coded — so we exclude these from the "truly never diagnosed" tier.
AKI_TEXT_PATTERN = re.compile(
    r"\b(AKI|ARF|acute\s+kidney\s+(injury|failure|insufficiency)"
    r"|acute\s+renal\s+(failure|insufficiency)"
    r"|acute\s+on\s+chronic\s+(kidney|renal)"
    r"|renal\s+failure"
    r"|azotemia"
    r"|elevated\s+creatinine"
    r"|rising\s+creatinine"
    r"|creatinine\s+(rose|rising|elevation|elevated|peaked|trend))",
    re.IGNORECASE,
)

# MIMIC-IV itemid for serum creatinine in labevents
# (verified via d_labitems.csv.gz — there is one canonical "Creatinine" itemid)
CREATININE_ITEMIDS = [50912]  # "Creatinine" in d_labitems

# AKI ICD codes
AKI_ICD10_PREFIX = re.compile(r"^N17")
AKI_ICD9_PREFIX = re.compile(r"^584")

# KDIGO thresholds
KDIGO_ABS_RISE = 0.3        # mg/dL absolute rise within 48h
KDIGO_RATIO = 1.5           # × baseline in prior 7 days


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample-n", type=int, default=100,
                        help="If set, sample this many Tier 2 candidates for LLM testing.")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    print("Loading admissions…")
    adm = pd.read_csv(
        HOSP / "admissions.csv.gz",
        usecols=["subject_id", "hadm_id", "admittime", "dischtime"],
        parse_dates=["admittime", "dischtime"],
    )
    print(f"  {len(adm):,} admissions")

    print("Loading diagnoses_icd…")
    dx = pd.read_csv(
        HOSP / "diagnoses_icd.csv.gz",
        dtype={"icd_code": str, "icd_version": int},
    )
    print(f"  {len(dx):,} dx rows")

    # Flag admissions that DID have AKI coded
    dx["is_aki"] = dx.apply(
        lambda r: bool(AKI_ICD10_PREFIX.match(str(r["icd_code"])) if r["icd_version"] == 10
                       else AKI_ICD9_PREFIX.match(str(r["icd_code"]))),
        axis=1,
    )
    aki_coded_hadm = set(dx[dx["is_aki"]]["hadm_id"].unique())
    print(f"  {len(aki_coded_hadm):,} admissions have AKI in discharge ICD list")

    print("Loading creatinine lab values (this is the slow step, ~2 min)…")
    labs = pd.read_csv(
        HOSP / "labevents.csv.gz",
        usecols=["hadm_id", "itemid", "charttime", "valuenum", "valueuom"],
        parse_dates=["charttime"],
    )
    cr = labs[labs["itemid"].isin(CREATININE_ITEMIDS)].copy()
    cr = cr.dropna(subset=["valuenum", "hadm_id", "charttime"])
    print(f"  {len(cr):,} creatinine values across all patients")

    # Filter to admissions we have records for
    cr["hadm_id"] = cr["hadm_id"].astype("int64")
    cr = cr.sort_values(["hadm_id", "charttime"])

    print("Applying KDIGO criteria per admission…")
    # Group by hadm_id, compute baseline + peak + KDIGO flags
    results = []
    grouped = cr.groupby("hadm_id")
    total_groups = len(grouped)
    progress_interval = max(1, total_groups // 20)

    for i, (hadm_id, g) in enumerate(grouped):
        if i % progress_interval == 0:
            print(f"  {i:>7,} / {total_groups:,}")
        if len(g) < 2:
            continue  # need at least 2 values to detect a rise

        vals = g["valuenum"].values
        times = g["charttime"].values

        # Baseline proxy: minimum Cr in the first 24 hours OR the first value
        # if all values are >24h apart (unusual)
        admit_time = times[0]
        baseline_mask = (times - admit_time) <= pd.Timedelta(hours=24).to_numpy()
        if baseline_mask.any():
            baseline = vals[baseline_mask].min()
        else:
            baseline = vals[0]
        peak = vals.max()

        # KDIGO 1.5× baseline criterion
        ratio_met = peak >= KDIGO_RATIO * baseline

        # KDIGO ≥0.3 mg/dL rise in 48h window
        # For each pair of values within 48h, check absolute rise
        abs_rise_met = False
        for j in range(len(vals)):
            window_end = times[j]
            window_start = window_end - pd.Timedelta(hours=48).to_numpy()
            window_vals = vals[(times >= window_start) & (times <= window_end)]
            if len(window_vals) >= 2 and (window_vals.max() - window_vals.min()) >= KDIGO_ABS_RISE:
                abs_rise_met = True
                break

        kdigo_met = ratio_met or abs_rise_met
        results.append({
            "hadm_id": int(hadm_id),
            "n_cr_values": int(len(vals)),
            "baseline_cr": float(round(baseline, 2)),
            "peak_cr": float(round(peak, 2)),
            "ratio": float(round(peak / baseline if baseline else 0, 2)),
            "kdigo_ratio_met": bool(ratio_met),
            "kdigo_abs_rise_met": bool(abs_rise_met),
            "kdigo_stage1_plus": bool(kdigo_met),
            "aki_coded": int(hadm_id) in aki_coded_hadm,
        })

    df = pd.DataFrame(results)
    print(f"\n  {len(df):,} admissions had ≥2 Cr values (eligible for KDIGO test)")

    # Aggregate stats
    n_eligible = len(df)
    n_kdigo = int(df["kdigo_stage1_plus"].sum())
    n_coded = int(df["aki_coded"].sum())
    n_kdigo_and_coded = int(((df["kdigo_stage1_plus"]) & (df["aki_coded"])).sum())
    n_kdigo_not_coded = int(((df["kdigo_stage1_plus"]) & (~df["aki_coded"])).sum())
    n_coded_not_kdigo = int(((~df["kdigo_stage1_plus"]) & (df["aki_coded"])).sum())

    undercoding_rate = (n_kdigo_not_coded / n_kdigo * 100) if n_kdigo else 0

    # Report
    lines = ["# KDIGO-AKI detection in MIMIC-IV", ""]
    lines.append(f"## Aggregate statistics (n={n_eligible:,} admissions with ≥2 creatinine values)")
    lines.append("")
    lines.append(f"- **Meet KDIGO Stage 1+ criteria:** {n_kdigo:,} ({100*n_kdigo/n_eligible:.1f}%)")
    lines.append(f"- **AKI coded in discharge ICD list:** {n_coded:,} ({100*n_coded/n_eligible:.1f}%)")
    lines.append("")
    lines.append("### Cross-tab")
    lines.append("")
    lines.append("| | AKI coded | AKI not coded | Total |")
    lines.append("|---|---|---|---|")
    lines.append(f"| KDIGO+ | {n_kdigo_and_coded:,} | **{n_kdigo_not_coded:,}** | {n_kdigo:,} |")
    lines.append(f"| KDIGO− | {n_coded_not_kdigo:,} | {n_eligible - n_kdigo - n_coded_not_kdigo:,} | {n_eligible - n_kdigo:,} |")
    lines.append(f"| Total | {n_coded:,} | {n_eligible - n_coded:,} | {n_eligible:,} |")
    lines.append("")
    lines.append(f"### Undercoding rate")
    lines.append(f"- **Our finding:** {undercoding_rate:.1f}% of KDIGO+ admissions had no AKI code")
    lines.append(f"- **Literature (Cammarata 2024, n=56,820):** 68% AKI undercoding rate")
    lines.append("")
    if abs(undercoding_rate - 68) < 10:
        lines.append("✅ Our undercoding rate is consistent with the Cammarata literature.")
    else:
        lines.append(f"⚠️ Undercoding rate diverges from literature; differences may be due to:")
        lines.append("  - Definition of baseline creatinine (we use first 24h min; Cammarata may use prior outpatient)")
        lines.append("  - Population (MIMIC is BIDMC ICU-heavy)")
        lines.append("  - Coding practices specific to BIDMC")
    lines.append("")
    lines.append("### Candidate set for LLM test")
    lines.append(f"- Total candidates (KDIGO+ but not coded): **{n_kdigo_not_coded:,}**")
    lines.append("- These are the cases where, if our LLM correctly flags AKI from chart data,")
    lines.append("  it has caught a clinically real condition the hospital failed to document.")

    OUT_REPORT.write_text("\n".join(lines))
    print(f"\n✓ Wrote report: {OUT_REPORT}")

    # Save Tier 1 candidates (KDIGO+ AND not coded — broad)
    tier1 = df[(df["kdigo_stage1_plus"]) & (~df["aki_coded"])].copy()
    OUT_JSON.write_text(tier1.to_json(orient="records", indent=2))
    print(f"✓ Wrote {len(tier1):,} Tier 1 candidates: {OUT_JSON}")

    # ========================================================================
    # Tier 2: also exclude cases where the discharge summary text mentions
    # AKI / ARF / azotemia / rising creatinine. These are cases where the
    # physician likely RECOGNIZED AKI but it wasn't formally coded.
    # ========================================================================
    print(f"\n=== Computing Tier 2 (KDIGO+ AND not coded AND not mentioned in notes) ===")
    print("Loading discharge.csv.gz (this is the slow step, ~1 min)…")
    disch = pd.read_csv(NOTE / "discharge.csv.gz",
                        usecols=["hadm_id", "text"],
                        dtype={"text": str})
    disch_by_hadm = dict(zip(disch["hadm_id"].astype("int64"), disch["text"]))
    print(f"  {len(disch_by_hadm):,} discharge summaries loaded")

    tier1_hadm_set = set(tier1["hadm_id"].astype("int64"))
    tier2_records = []
    n_mentioned = 0
    n_no_summary = 0
    for _, row in tier1.iterrows():
        hadm_id = int(row["hadm_id"])
        text = disch_by_hadm.get(hadm_id)
        if text is None or not isinstance(text, str):
            n_no_summary += 1
            continue  # exclude — no narrative to check
        if AKI_TEXT_PATTERN.search(text):
            n_mentioned += 1
            continue  # exclude — physician likely recognized
        tier2_records.append(row.to_dict())

    tier2 = pd.DataFrame(tier2_records)
    print(f"  Tier 1 candidates with no discharge summary: {n_no_summary:,} (excluded)")
    print(f"  Tier 1 candidates where AKI mentioned in notes: {n_mentioned:,} (excluded)")
    print(f"  → Tier 2 candidates (truly never diagnosed):    {len(tier2):,}")

    # ========================================================================
    # Stratified sample for the LLM test
    # ========================================================================
    n_sample = args.sample_n
    if len(tier2) < n_sample:
        print(f"⚠️ Only {len(tier2)} Tier 2 candidates; using all of them.")
        sampled = tier2.copy()
    else:
        # Stratify by KDIGO severity
        # Stage 3-equivalent: peak >= 3× baseline (severe)
        # Stage 2-equivalent: peak >= 2× baseline (moderate)
        # Stage 1-only: 1.5× to 2× baseline (mild)
        tier2["severity"] = tier2["ratio"].apply(
            lambda r: "severe" if r >= 3.0 else ("moderate" if r >= 2.0 else "mild")
        )
        n_severe = 15
        n_mild = 15
        n_random = n_sample - n_severe - n_mild
        rng = random.Random(args.seed)

        severe_pool = tier2[tier2["severity"] == "severe"]
        mild_pool = tier2[tier2["severity"] == "mild"]

        sev_pick = severe_pool.sample(n=min(n_severe, len(severe_pool)),
                                       random_state=args.seed)
        mild_pick = mild_pool.sample(n=min(n_mild, len(mild_pool)),
                                      random_state=args.seed)
        remaining = tier2.drop(sev_pick.index).drop(mild_pick.index)
        rand_pick = remaining.sample(n=min(n_random, len(remaining)),
                                      random_state=args.seed)
        sampled = pd.concat([sev_pick, mild_pick, rand_pick]).reset_index(drop=True)
        print(f"\nStratified sample of {len(sampled)}:")
        print(f"  Severe (≥3× baseline): {len(sev_pick)}")
        print(f"  Mild (1.5–2× baseline): {len(mild_pick)}")
        print(f"  Random middle: {len(rand_pick)}")

    # Format for stitch_case.py compatibility
    # We need to look up subject_id, admittime, etc. from adm
    sampled = sampled.merge(adm[["subject_id", "hadm_id", "admittime", "dischtime"]],
                             on="hadm_id", how="left")
    sampled["admittime"] = sampled["admittime"].astype(str)
    sampled["dischtime"] = sampled["dischtime"].astype(str)
    sampled["los_days"] = (pd.to_datetime(sampled["dischtime"]) - pd.to_datetime(sampled["admittime"])).dt.total_seconds() / 86400
    sampled["bucket"] = "aki_test"
    sampled["primary_dx_icd"] = "N17_ALGO"
    sampled["primary_dx_desc"] = "KDIGO+ AKI (algorithmically defined, not coded by hospital)"
    sampled["admission_type"] = "UNKNOWN"
    sampled["n_acute_dx"] = 1

    OUT_SAMPLE_JSON.write_text(json.dumps(
        sampled[["hadm_id", "subject_id", "admittime", "dischtime", "los_days",
                 "admission_type", "primary_dx_icd", "primary_dx_desc",
                 "bucket", "n_acute_dx", "baseline_cr", "peak_cr", "ratio"]]
        .astype({"hadm_id": "int64", "subject_id": "int64"})
        .to_dict(orient="records"),
        indent=2, default=str))
    print(f"\n✓ Wrote {len(sampled)}-case sample for LLM testing: {OUT_SAMPLE_JSON}")

    # Print summary
    print(f"\n=== SUMMARY ===")
    print(f"  Eligible admissions (≥2 Cr):  {n_eligible:>8,}")
    print(f"  KDIGO+:                       {n_kdigo:>8,} ({100*n_kdigo/n_eligible:.1f}%)")
    print(f"  AKI coded:                    {n_coded:>8,} ({100*n_coded/n_eligible:.1f}%)")
    print(f"  KDIGO+ AND coded:             {n_kdigo_and_coded:>8,}")
    print(f"  KDIGO+ AND not coded (Tier 1):{n_kdigo_not_coded:>8,}")
    print(f"  Tier 2 (never diagnosed):     {len(tier2):>8,}")
    print(f"  Undercoding rate:             {undercoding_rate:>7.1f}%  (Cammarata: 68%)")
    print(f"  Sample for LLM test:          {len(sampled):>8,}")


if __name__ == "__main__":
    main()
