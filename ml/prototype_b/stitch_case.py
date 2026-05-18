"""Build leak-safe MIMIC-IV case files for the DDx benchmark.

For each admission in selected_admissions.json, writes:
    data/<hadm_id>/admit.input.txt          — HPI + ED triage at admission only
    data/<hadm_id>/plus24h.input.txt        — + labs/micro/imaging/meds up to admit+24h
    data/<hadm_id>/plus48h.input.txt        — + up to admit+48h
    data/<hadm_id>/pre_discharge.input.txt  — full chart minus Hospital Course / Discharge Dx
    data/<hadm_id>/gold.json                — acute discharge diagnoses (answer key)

LEAK SAFETY:
  - The discharge summary is parsed and only the HPI / PMH / SH / Allergies /
    Admission Meds sections are kept. Brief Hospital Course, Discharge
    Diagnosis, Discharge Medications, Discharge Disposition, Discharge
    Condition, Discharge Instructions, Followup Instructions are stripped.
  - Lab values, micro, radiology, and prescriptions are filtered by storetime
    or starttime against the cutoff.
  - The gold answer (discharge ICD codes) is written to a SEPARATE file
    (gold.json) and never appears in any input.txt.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]
HOSP = ROOT / "physionet.org" / "files" / "mimiciv" / "3.1" / "hosp"
NOTE = ROOT / "physionet.org" / "files" / "mimic-iv-note" / "2.2" / "note"
ED = ROOT / "physionet.org" / "files" / "mimic-iv-ed" / "2.2" / "ed"

import argparse
_argp = argparse.ArgumentParser(add_help=False)
_argp.add_argument("--selected", default=str(Path(__file__).parent / "selected_admissions.json"))
_argp.add_argument("--out-dir", default=str(Path(__file__).parent / "data"))
_args, _ = _argp.parse_known_args()

SELECTED = Path(_args.selected)
OUT_DIR = Path(_args.out_dir)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

# Codes to EXCLUDE from the gold set.
#
# Business alignment: the product is a pre-visit copilot that surfaces NEW
# acute diagnoses the physician should act on. It should NOT be evaluated on
# its ability to re-state pre-existing chronic conditions, symptom codes
# (those are the complaints), post-procedure complications (unpredictable
# from admission), or hospital-acquired conditions.
#
# Three filter buckets:
#   1. Chronic comorbidities (already in PMH — physician knows)
#   2. Symptom / sign codes (those are the complaints, not the answer)
#   3. Status / external-cause / billing-only codes

ICD10_EXCLUDE = re.compile(
    r"^("
    # === Chronic comorbidities — already in PMH ===
    r"I10|I11|I12|I13|I15"            # essential / other hypertension
    r"|E78|E11|E03|E66"                # lipid / T2DM / hypothyroid / obesity
    r"|F17|F31|F32|F33|F41|F84"        # tobacco, bipolar, depression, anxiety, PDD
    r"|F70|F71|F72|F73|F79"            # intellectual disabilities (chronic)
    r"|N18"                             # CKD
    r"|G47"                             # sleep disorders
    r"|M81"                             # osteoporosis (chronic state)
    r"|M85"                             # other bone density disorders (chronic)
    r"|M06"                             # other rheumatoid arthritis
    r"|J45"                             # asthma
    r"|J44"                             # COPD (chronic — though acute exacerbation IS J44.1)
    r"|K21"                             # GERD
    r"|D649"                            # anemia, unspecified — too generic
    r"|E04"                             # nontoxic goiter (chronic)

    # === Symptom / sign codes (R-chapter) ===
    # These are the things the physician is investigating, not the diagnoses
    # the workup should reveal. Catches abdominal pain, syncope, nausea,
    # malaise, dyspnea, etc.
    r"|R0"                              # R00-R09 circulatory/respiratory symptoms
    r"|R1"                              # R10-R19 digestive symptoms
    r"|R2"                              # R20-R29 skin/nervous symptoms
    r"|R3"                              # R30-R39 GU symptoms
    r"|R4"                              # R40-R49 cognition/perception/speech
    r"|R5"                              # R50-R59 general symptoms (fever, syncope)
    r"|R6"                              # R60-R69 general signs (edema, cachexia, SIRS)
    r"|R7"                              # R70-R79 abnormal blood findings
    r"|R8"                              # R80-R89 abnormal urine findings
    r"|R9"                              # R90-R99 abnormal imaging findings

    # === Status, history, external-cause codes ===
    r"|Z"                               # status / history of / encounter for
    r"|H"                               # eye/ear (usually incidental)
    r"|V|W|X|Y"                         # external-cause codes (V/W/X/Y)
    r")"
)

ICD9_EXCLUDE = re.compile(
    r"^("
    # === ICD-9 chronic comorbidities ===
    r"401|402|403|404|405"             # hypertension
    r"|272"                             # lipid disorders
    r"|250"                             # diabetes mellitus
    r"|244"                             # acquired hypothyroidism
    r"|245"                             # other thyroiditis (chronic)
    r"|241"                             # nontoxic goiter
    r"|242"                             # thyrotoxicosis
    r"|278"                             # obesity
    r"|305"                             # nondependent abuse
    r"|303|304"                         # alcohol / drug dependence (chronic)
    r"|296|300|311"                     # bipolar / anxiety / depression
    r"|295|297|298|299"                 # schizophrenia / psych (chronic)
    r"|317|318|319"                     # intellectual disabilities
    r"|309"                             # adjustment reactions
    r"|585"                             # chronic kidney disease
    r"|327"                             # sleep disorders
    r"|733"                             # osteoporosis & disorders of bone
    r"|530"                             # GERD / esophageal disorders
    r"|493"                             # asthma
    r"|496"                             # chronic airway obstruction NEC
    r"|492"                             # emphysema
    r"|428"                             # heart failure (chronic — Note: keep individual subcodes?)

    # === ICD-9 symptom codes (chapter 780-799) ===
    r"|78[0-9]"                         # 780-789 general symptoms
    r"|79[0-9]"                         # 790-799 ill-defined / abnormal findings

    # === ICD-9 external causes (E codes) and status (V codes) ===
    r"|E[0-9]"                          # E000-E999 external causes
    r"|V[0-9]"                          # V01-V91 supplementary status

    # === ICD-9 complications of care (996-999) ===
    r"|99[6-9]"

    # === ICD-9 SIRS / non-specific ===
    r"|9959"                            # 99591-99594 SIRS / sepsis billing nuances
    r")"
)


def is_excluded(icd_code: str, icd_version: int) -> bool:
    """Return True if this ICD code should be filtered out of the gold set."""
    code = str(icd_code).strip()
    if not code:
        return True
    if icd_version == 9:
        return bool(ICD9_EXCLUDE.match(code))
    # default to ICD-10
    return bool(ICD10_EXCLUDE.match(code))


# Old single-regex variable kept for backwards-compat with cherry_pick.py
# which is still ICD-10-only at the moment.
CHRONIC_ICD_PATTERNS = ICD10_EXCLUDE


# Sections of the discharge summary to KEEP (admission-time content)
# and STOP at (anything after this point is post-admission / answer-bearing).
KEEP_SECTIONS = [
    "Service",
    "Allergies",
    "Chief Complaint",
    "Major Surgical or Invasive Procedure",
    "History of Present Illness",
    "Past Medical History",
    "Social History",
    "Family History",
    "Physical Exam",
    "Medications on Admission",
]

STOP_SECTIONS = [
    "Pertinent Results",
    "Brief Hospital Course",
    "Hospital Course",
    "Discharge Medications",
    "Discharge Disposition",
    "Discharge Diagnosis",
    "Discharge Diagnoses",
    "Discharge Condition",
    "Discharge Instructions",
    "Followup Instructions",
    "Follow-up Instructions",
]


# ---------------------------------------------------------------------------
# Discharge summary section extraction
# ---------------------------------------------------------------------------

def extract_admission_sections(discharge_text: str) -> str:
    """Return only the admission-relevant sections from a discharge summary.

    Strategy: walk through lines, identify section headers, keep content
    under KEEP_SECTIONS, stop entirely once we hit any STOP_SECTIONS.
    """
    keep_set = {s.lower() for s in KEEP_SECTIONS}
    stop_set = {s.lower() for s in STOP_SECTIONS}

    # Regex for "Section Name:" at start of line (case-insensitive)
    header_re = re.compile(r"^\s*([A-Z][A-Za-z /\-&]+):\s*$", re.MULTILINE)

    # Find all section header positions
    headers = []
    for m in header_re.finditer(discharge_text):
        name = m.group(1).strip().lower()
        headers.append((m.start(), m.end(), name))

    if not headers:
        # Couldn't find structured sections — return the first 4000 chars
        # as a fallback, with a warning marker
        return "[chart preamble — section parsing failed]\n" + discharge_text[:4000]

    out_parts = []
    for i, (start, end, name) in enumerate(headers):
        if name in stop_set:
            # Stop here — everything after this header is post-admission / answer
            break
        # Determine end of this section's body: next header start, or end of text
        body_start = end
        body_end = headers[i + 1][0] if i + 1 < len(headers) else len(discharge_text)
        if name in keep_set:
            body = discharge_text[body_start:body_end].strip()
            section_name = discharge_text[start:end].strip()
            out_parts.append(f"{section_name}\n{body}")

    return "\n\n".join(out_parts)


# ---------------------------------------------------------------------------
# Lab / micro / radiology / prescription formatters
# ---------------------------------------------------------------------------

def format_labs(df: pd.DataFrame, lab_dict: dict) -> str:
    if df.empty:
        return "(no lab results)"
    lines = []
    # Group by storetime hour for readability
    df = df.sort_values("storetime").copy()
    df["item"] = df["itemid"].map(lab_dict).fillna("?")
    for _, r in df.iterrows():
        flag = f" [{r['flag']}]" if pd.notna(r.get("flag")) and r["flag"] not in (None, "", " ") else ""
        units = f" {r['valueuom']}" if pd.notna(r.get("valueuom")) else ""
        val = r.get("value") or ""
        time_str = pd.to_datetime(r["storetime"]).strftime("%Y-%m-%d %H:%M")
        lines.append(f"  {time_str}  {r['item']:<35s} {val}{units}{flag}")
    return "\n".join(lines)


def format_micro(df: pd.DataFrame) -> str:
    if df.empty:
        return "(no microbiology results)"
    df = df.sort_values("storetime").copy()
    lines = []
    def _s(v):
        return str(v) if pd.notna(v) and v != "" else ""
    for _, r in df.iterrows():
        time_str = pd.to_datetime(r["storetime"]).strftime("%Y-%m-%d %H:%M")
        parts = [_s(r.get("spec_type_desc")), _s(r.get("org_name")), _s(r.get("ab_name"))]
        result = " | ".join(p for p in parts if p)
        lines.append(f"  {time_str}  {result}")
    return "\n".join(lines)


def format_prescriptions(df: pd.DataFrame) -> str:
    if df.empty:
        return "(no prescriptions)"
    df = df.sort_values("starttime").copy()
    lines = []
    for _, r in df.iterrows():
        time_str = pd.to_datetime(r["starttime"]).strftime("%Y-%m-%d %H:%M")
        drug = r.get("drug") or ""
        dose = f"{r.get('dose_val_rx', '')} {r.get('dose_unit_rx', '')}".strip()
        route = r.get("route") or ""
        lines.append(f"  {time_str}  {drug} {dose} {route}".rstrip())
    return "\n".join(lines)


def format_radiology(df: pd.DataFrame) -> str:
    if df.empty:
        return "(no radiology reports)"
    df = df.sort_values("storetime").copy()
    parts = []
    for _, r in df.iterrows():
        time_str = pd.to_datetime(r["storetime"]).strftime("%Y-%m-%d %H:%M")
        parts.append(f"### {time_str}\n{r['text']}")
    return "\n\n".join(parts)


def format_ed(triage_df: pd.DataFrame, vitals_df: pd.DataFrame) -> str:
    parts = []
    if not triage_df.empty:
        r = triage_df.iloc[0]
        parts.append("ED TRIAGE:")
        for col in ["temperature", "heartrate", "resprate", "o2sat", "sbp", "dbp",
                    "pain", "acuity", "chiefcomplaint"]:
            v = r.get(col)
            if pd.notna(v) and v != "":
                parts.append(f"  {col}: {v}")
    if not vitals_df.empty:
        parts.append("\nED VITALS:")
        vitals_df = vitals_df.sort_values("charttime")
        for _, r in vitals_df.iterrows():
            time_str = pd.to_datetime(r["charttime"]).strftime("%Y-%m-%d %H:%M")
            v_parts = [f"T={r.get('temperature')}", f"HR={r.get('heartrate')}",
                       f"RR={r.get('resprate')}", f"O2={r.get('o2sat')}",
                       f"BP={r.get('sbp')}/{r.get('dbp')}"]
            parts.append(f"  {time_str}  " + "  ".join(v_parts))
    return "\n".join(parts) if parts else "(no ED data)"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    selected = json.loads(SELECTED.read_text())
    hadm_ids = [int(r["hadm_id"]) for r in selected]
    subject_ids = [int(r["subject_id"]) for r in selected]
    print(f"Stitching {len(selected)} admissions")

    # ---- Load reference tables --------------------------------------------
    print("Loading dictionaries…")
    d_labitems = pd.read_csv(HOSP / "d_labitems.csv.gz", usecols=["itemid", "label"])
    lab_dict = dict(zip(d_labitems["itemid"], d_labitems["label"]))
    icd_dict = pd.read_csv(HOSP / "d_icd_diagnoses.csv.gz", usecols=["icd_code", "long_title"]).drop_duplicates("icd_code")
    icd_lookup = dict(zip(icd_dict["icd_code"], icd_dict["long_title"]))

    # ---- Filter big tables to just our patients ---------------------------
    print("Loading admissions, diagnoses, labs (this is the slow step)…")
    adm = pd.read_csv(HOSP / "admissions.csv.gz", parse_dates=["admittime", "dischtime"])
    adm = adm[adm["hadm_id"].isin(hadm_ids)]

    dx = pd.read_csv(HOSP / "diagnoses_icd.csv.gz",
                     dtype={"icd_code": str, "icd_version": int})
    dx = dx[dx["hadm_id"].isin(hadm_ids)]

    print("  labevents.csv.gz (2.4GB) …")
    labs = pd.read_csv(
        HOSP / "labevents.csv.gz",
        usecols=["subject_id", "hadm_id", "itemid", "charttime", "storetime",
                 "value", "valueuom", "flag"],
        parse_dates=["charttime", "storetime"],
        dtype={"value": str},
    )
    labs = labs[labs["hadm_id"].isin(hadm_ids)]
    print(f"    {len(labs):,} lab rows for selected admissions")

    print("  microbiologyevents.csv.gz …")
    micro = pd.read_csv(
        HOSP / "microbiologyevents.csv.gz",
        usecols=["hadm_id", "chartdate", "charttime", "storedate", "storetime",
                 "spec_type_desc", "org_name", "ab_name"],
        parse_dates=["charttime", "storetime"],
    )
    micro = micro[micro["hadm_id"].isin(hadm_ids)]

    print("  prescriptions.csv.gz …")
    rx = pd.read_csv(
        HOSP / "prescriptions.csv.gz",
        usecols=["hadm_id", "starttime", "stoptime", "drug",
                 "dose_val_rx", "dose_unit_rx", "route"],
        parse_dates=["starttime", "stoptime"],
        dtype={"dose_val_rx": str},
    )
    rx = rx[rx["hadm_id"].isin(hadm_ids)]

    print("  patients.csv.gz …")
    patients = pd.read_csv(HOSP / "patients.csv.gz",
                           usecols=["subject_id", "anchor_age", "gender"])

    print("  discharge.csv.gz …")
    disch = pd.read_csv(NOTE / "discharge.csv.gz",
                        usecols=["hadm_id", "subject_id", "charttime", "text"],
                        dtype={"text": str})
    disch = disch[disch["hadm_id"].isin(hadm_ids)]

    print("  radiology.csv.gz …")
    rad = pd.read_csv(NOTE / "radiology.csv.gz",
                      usecols=["hadm_id", "subject_id", "charttime", "storetime", "text"],
                      parse_dates=["charttime", "storetime"],
                      dtype={"text": str})
    rad = rad[rad["hadm_id"].isin(hadm_ids)]

    print("  edstays + triage + vitals (small)…")
    edstays = pd.read_csv(ED / "edstays.csv.gz", parse_dates=["intime", "outtime"])
    edstays = edstays[edstays["hadm_id"].isin(hadm_ids)]
    ed_stay_ids = set(edstays["stay_id"])
    triage = pd.read_csv(ED / "triage.csv.gz")
    triage = triage[triage["stay_id"].isin(ed_stay_ids)]
    ed_vitals = pd.read_csv(ED / "vitalsign.csv.gz", parse_dates=["charttime"])
    ed_vitals = ed_vitals[ed_vitals["stay_id"].isin(ed_stay_ids)]

    # ---- Per-admission stitching ------------------------------------------
    for sel in selected:
        hadm_id = int(sel["hadm_id"])
        subject_id = int(sel["subject_id"])
        print(f"\n--- {hadm_id} ({sel['bucket']}: {sel['primary_dx_desc'][:60]}) ---")

        adm_row = adm[adm["hadm_id"] == hadm_id].iloc[0]
        admittime = adm_row["admittime"]

        # Gold answer: acute discharge dx (version-aware exclusion)
        dx_rows = dx[dx["hadm_id"] == hadm_id].sort_values("seq_num").copy()
        gold = []
        for _, r in dx_rows.iterrows():
            excluded = is_excluded(r["icd_code"], int(r["icd_version"]))
            entry = {
                "seq_num": int(r["seq_num"]),
                "icd_code": str(r["icd_code"]),
                "icd_version": int(r["icd_version"]),
                "title": icd_lookup.get(str(r["icd_code"]), ""),
                "is_excluded": bool(excluded),
            }
            gold.append(entry)
        acute_gold = [g for g in gold if not g["is_excluded"]]

        case_dir = OUT_DIR / str(hadm_id)
        case_dir.mkdir(parents=True, exist_ok=True)
        (case_dir / "gold.json").write_text(json.dumps({
            "hadm_id": hadm_id,
            "subject_id": subject_id,
            "primary_dx_icd": sel["primary_dx_icd"],
            "primary_dx_desc": sel["primary_dx_desc"],
            "bucket": sel["bucket"],
            "acute_diagnoses": acute_gold,
            "all_diagnoses": gold,
        }, indent=2))

        # Patient header
        pt = patients[patients["subject_id"] == subject_id].iloc[0]
        header = (
            f"PATIENT HEADER\n"
            f"  Age at anchor: {pt['anchor_age']} · Sex: {pt['gender']}\n"
            f"  Admission: {sel['admission_type']}\n"
            f"  Admit time: {admittime}\n"
        )

        # Discharge summary admission sections (no leak)
        disch_rows = disch[disch["hadm_id"] == hadm_id]
        if len(disch_rows) == 0:
            disch_text = "(no discharge summary available)"
        else:
            full_text = disch_rows.iloc[0]["text"]
            disch_text = extract_admission_sections(full_text)

        # ED data — IMPORTANT: filter to THIS patient's ED stays only
        pt_ed_stay_ids = set(edstays[edstays["hadm_id"] == hadm_id]["stay_id"])
        pt_triage = triage[triage["stay_id"].isin(pt_ed_stay_ids)]
        pt_ed_vitals = ed_vitals[ed_vitals["stay_id"].isin(pt_ed_stay_ids)]
        ed_text = format_ed(pt_triage, pt_ed_vitals)

        # Build inputs at each cutoff
        cutoffs = {
            "admit": admittime,  # only header + HPI + ED triage
            "plus24h": admittime + pd.Timedelta(hours=24),
            "plus48h": admittime + pd.Timedelta(hours=48),
            "pre_discharge": adm_row["dischtime"] - pd.Timedelta(minutes=1),
        }

        for cutoff_name, cutoff_time in cutoffs.items():
            parts = [header, "═" * 60, "EMERGENCY DEPARTMENT", ed_text,
                     "═" * 60, "ADMISSION CHART NOTES (HPI, PMH, etc.)", disch_text]

            if cutoff_name != "admit":
                # Add time-filtered labs, micro, radiology, prescriptions
                pt_labs = labs[(labs["hadm_id"] == hadm_id) & (labs["storetime"] <= cutoff_time)]
                pt_micro = micro[(micro["hadm_id"] == hadm_id) & (micro["storetime"] <= cutoff_time)]
                pt_rad = rad[(rad["hadm_id"] == hadm_id) & (rad["storetime"] <= cutoff_time)]
                pt_rx = rx[(rx["hadm_id"] == hadm_id) & (rx["starttime"] <= cutoff_time)]

                parts.extend([
                    "═" * 60, f"LABS (through {cutoff_time})",
                    format_labs(pt_labs, lab_dict),
                    "═" * 60, f"MICROBIOLOGY (through {cutoff_time})",
                    format_micro(pt_micro),
                    "═" * 60, f"RADIOLOGY REPORTS (through {cutoff_time})",
                    format_radiology(pt_rad),
                    "═" * 60, f"MEDICATIONS ORDERED (through {cutoff_time})",
                    format_prescriptions(pt_rx),
                ])

            input_text = "\n".join(parts)
            (case_dir / f"{cutoff_name}.input.txt").write_text(input_text)

            # Compute approximate size
            print(f"  {cutoff_name:<15s}  {len(input_text):>7,} chars")

    print(f"\n✓ Stitched {len(selected)} admissions to {OUT_DIR}")


if __name__ == "__main__":
    main()
