"""Batch 3 of the hide-one-dx pilot: extend from 9 to 100 cases (fresh MIMIC).

Stricter filters vs. the first iteration:
  - SOURCE: only data/ (general-medicine cohort from cherry_pick); skips data_aki/
    to avoid AKI-cohort bias.
  - LOS >= 2 days (rejects short observation stays).
  - Excludes in-hospital deaths.
  - Hidden dx must be "acutely relevant" — not a symptom code, not chronic, and
    not on a hardcoded PMH-style exclusion list. Re-picks within the patient's
    other acute dxs if the random one is chronic/PMH-style.

For each accepted case:
  - Randomly picks an acute, hide-worthy dx
  - Auto-derives scrub patterns from the dx title (SYNONYMS map; fallback to
    title's core noun phrase)
  - Scrubs pre_discharge.input.txt
  - First-pass audits for residual mentions of derived patterns

Outputs to pilot_hide_one/<hadm_id>/ (gitignored, DUA-protected).
Extends the manifest with batch=3, tagged with source='data' for every case.
"""

from __future__ import annotations

import json
import random
import re
from pathlib import Path

import pandas as pd

ROOT = Path("/Users/tomohiro/Projects/Thousand/ml/prototype_b")
DATA = ROOT / "data"
OUT = ROOT / "pilot_hide_one"
MIMIC_HOSP = ROOT.parents[1] / "physionet.org" / "files" / "mimiciv" / "3.1" / "hosp"
TARGET_TOTAL = 100
SEED = 20260606
LOS_MIN_DAYS = 2.0

# ---------------------------------------------------------------------------
# Synonym / abbreviation map — keyword (substring) -> regex patterns to scrub.
# ---------------------------------------------------------------------------
SYNONYMS: dict[str, list[str]] = {
    # Infectious
    "pneumonia": [r"pneumonia", r"\bpna\b", r"pneumonic"],
    "urinary tract infection": [r"\buti\b", r"urinary tract infect", r"cystitis", r"pyelonephritis"],
    "cellulitis": [r"cellulitis"],
    "sepsis": [r"sepsis", r"septic shock", r"\bsirs\b"],
    "bacteremia": [r"bacteremia", r"bacteraemia"],
    "endocarditis": [r"endocarditis"],
    "mononucleosis": [r"mononucleosis", r"\bmono\b", r"\bebv\b", r"epstein.?barr", r"monospot"],
    "abscess": [r"abscess"],
    "meningitis": [r"meningitis"],
    "encephalitis": [r"encephalitis"],
    "osteomyelitis": [r"osteomyelitis"],
    "hepatitis": [r"hepatitis"],
    "lymphadenitis": [r"lymphadenitis"],
    # Cardiac
    "heart failure": [r"heart failure", r"\bchf\b", r"decompensat", r"congestive", r"\bhf[pr]?ef\b"],
    "atrial fibrillation": [r"atrial fibrillation", r"\bafib\b", r"a[- ]?fib"],
    "atrial flutter": [r"atrial flutter", r"a[- ]?flutter"],
    "myocardial infarction": [r"myocardial infarction", r"\bstemi\b", r"\bnstemi\b"],
    "angina": [r"angina"],
    "pericarditis": [r"pericarditis"],
    "av block": [r"\bav block\b", r"atrioventricular block"],
    "sick sinus": [r"sick sinus"],
    # Pulm / vascular
    "embolism": [r"embolism", r"embolus", r"embolic"],
    "pneumothorax": [r"pneumothorax"],
    "pleural effusion": [r"pleural effusion"],
    "pulmonary edema": [r"pulmonary edema"],
    "asthma": [r"asthma"],
    "copd": [r"\bcopd\b", r"chronic obstructive"],
    "atelectasis": [r"atelectasis"],
    # Renal / GU
    "kidney injury": [r"kidney injury", r"\baki\b", r"renal failure", r"kidney failure", r"renal insufficiency"],
    "kidney disease": [r"kidney disease", r"\bckd\b", r"chronic kidney"],
    "hematuria": [r"hematuria"],
    # GI
    "cholelithiasis": [r"cholelith", r"gallstone"],
    "cholecystitis": [r"cholecystitis"],
    "pancreatitis": [r"pancreatitis"],
    "gastroenteritis": [r"gastroenteritis"],
    "colitis": [r"\bcolitis\b"],
    "gastritis": [r"\bgastritis\b"],
    "diverticulitis": [r"diverticulitis"],
    "appendicitis": [r"appendicitis"],
    "ileus": [r"\bileus\b"],
    "obstruction": [r"obstruction"],
    "gi bleed": [r"gi bleed", r"gastrointestinal hemorrhage", r"hematemesis", r"melena"],
    "ulcer": [r"\bulcer\b"],
    "ascites": [r"ascites"],
    "cirrhosis": [r"cirrhosis", r"hepatic fibrosis"],
    # Neuro
    "stroke": [r"\bstroke\b", r"cerebrovascular accident", r"\bcva\b", r"cerebral infarction"],
    "seizure": [r"seizure"],
    "encephalopathy": [r"encephalopath"],
    "delirium": [r"delirium"],
    "intracerebral hemorrhage": [r"intracerebral hemorrhage", r"\bich\b"],
    "subdural": [r"subdural"],
    "epilepsy": [r"epilepsy"],
    "dementia": [r"dementia"],
    # Endocrine / metabolic
    "diabetes": [r"\bdiabetes\b", r"diabetic", r"\bdka\b"],
    "hypoglycemia": [r"hypoglycemi"],
    "hyperglycemia": [r"hyperglycemi"],
    "hypothyroid": [r"hypothyroid"],
    "hyperthyroid": [r"hyperthyroid"],
    "hyponatremia": [r"hyponatremi"],
    "hypernatremia": [r"hypernatremi"],
    "hypokalemia": [r"hypokalemi"],
    "hyperkalemia": [r"hyperkalemi"],
    "hypomagnesemia": [r"hypomagnesemi"],
    "hypocalcemia": [r"hypocalcemi"],
    "hypercalcemia": [r"hypercalcemi"],
    "malnutrition": [r"malnutrition", r"malnourished", r"cachexia", r"cachectic"],
    "antidiuretic": [r"\bsiadh\b", r"antidiuretic", r"syndrome of inappropriate"],
    # Heme
    "anemia": [r"\banemia\b", r"\banaemia\b", r"\banaemic\b"],
    "thrombocytopenia": [r"thrombocytopenia"],
    "leukopenia": [r"leukopen"],
    "neutropenia": [r"neutropen"],
    "thrombocytosis": [r"thrombocytosis"],
    "leukemia": [r"leukemia"],
    "lymphoma": [r"lymphoma"],
    # Onc
    "neoplasm": [r"neoplasm", r"\btumou?r\b", r"malignant", r"\bcancer\b", r"carcinoma", r"metastat"],
    "melanoma": [r"melanoma"],
    # Skin
    "rash": [r"\brash\b"],
    "dermatitis": [r"dermatitis"],
    "pressure ulcer": [r"pressure ulcer", r"decubitus"],
    # Other
    "rhabdomyolysis": [r"rhabdomyolysis", r"\brhabdo\b"],
    "myopathy": [r"myopathy", r"myositis"],
    "fracture": [r"fracture"],
    "foreign body": [r"foreign body", r"foreign object", r"ingest"],
    "venous insufficiency": [r"venous insufficiency"],
}

# Common qualifying phrases to strip when falling back to the title's core
QUALIFIERS = re.compile(
    r"\b(unspecified|not elsewhere classified|nec|other\s+specified|other|"
    r"site\s+not\s+specified|without\s+(?:obstruction|complication|mention|status\s+migrainosus)|"
    r"with\s+(?:intoxication|tophus|tophi)|initial\s+encounter|chronic|acute|severe|moderate|mild|"
    r"primary|secondary|recurrent|unstable|stable)\b",
    re.IGNORECASE,
)

# Hide-worthiness filters — reject the hidden dx if it's any of these.
# These are common comorbid/PMH-style codes that aren't really "missed in a busy
# inpatient workflow" but rather chronic problem-list items.
PMH_STYLE_TITLE_SUBSTRINGS = [
    "constipation",
    "essential (primary) hypertension",
    "primary hypertension",
    "hyperlipidemia",
    "hypothyroid",  # very common chronic, would be on med list
    "tobacco",
    "nicotine",
    "alcohol use",
    "personal history",
    "long term",
    "long-term",
    "history of",
    "screening for",
    "obesity",
    "overweight",
    "gerd",
    "gastro-esophageal reflux",
    "depressive disorder",  # chronic outpatient psych
    "anxiety disorder",
    "ptsd",
    "post-traumatic stress",
    "schizophrenia",  # chronic outpatient
    "bipolar",
    "personality disorder",
    "attention-deficit",
    "migraine",  # chronic outpatient
    "fall on stairs",  # mechanism code, not dx
    "fall on",
    "allergic rhinitis",
    "seasonal allergic",
    "dorsalgia",
    "spondylosis",
    "internal derangement",
    "chronic pain",
    "vitamin d deficiency",
    "gout",  # chronic
    "iron deficiency anemia",  # often chronic outpatient
    "atherosclerotic heart disease of native coronary artery without",
    "old myocardial infarction",
    "varicose veins",
    "venous insufficiency",
    "essential thrombocythemia",
    "morbid (severe) obesity",
    "obstructive sleep apnea",
    "benign prostatic hyperplasia",
    "deformities of",
    "internal derangement",
    "screening",
]

# Symptom (R-code) ICD prefixes — codes that describe symptoms not diseases
SYMPTOM_PREFIXES = ("R",)


def is_hide_worthy(icd: str, title: str) -> bool:
    """True if this dx makes sense as a 'missed diagnosis' to hide."""
    if not icd or not title:
        return False
    if icd.startswith(SYMPTOM_PREFIXES):
        return False
    title_low = title.lower()
    for sub in PMH_STYLE_TITLE_SUBSTRINGS:
        if sub in title_low:
            return False
    return True


def derive_patterns(dx_title: str) -> list[str]:
    low = dx_title.lower()
    matched: list[str] = []
    for kw, pats in SYNONYMS.items():
        if kw in low:
            matched.extend(pats)
    if matched:
        seen = set()
        out = []
        for p in matched:
            if p not in seen:
                out.append(p)
                seen.add(p)
        return out

    core = re.split(r"[,(]", dx_title, maxsplit=1)[0]
    core = QUALIFIERS.sub("", core)
    core = re.sub(r"\s+", " ", core).strip(" -")
    if core and len(core) >= 4:
        return [re.escape(core)]
    return []


def scrub_text(text: str, patterns: list[str]) -> tuple[str, list[str]]:
    compiled = [re.compile(p, re.IGNORECASE) for p in patterns]
    out: list[str] = []
    log: list[str] = []
    for i, line in enumerate(text.splitlines(), 1):
        if any(rx.search(line) for rx in compiled):
            log.append(f"L{i}: {line.rstrip()[:160]}")
            out.append("[REDACTED-DX]")
        else:
            out.append(line)
    return "\n".join(out), log


def audit_residual(chart: str, patterns: list[str]) -> int:
    return sum(len(re.findall(p, chart, re.IGNORECASE)) for p in patterns)


def load_admission_metadata(hadm_ids: set[int]) -> dict[int, dict]:
    """Pull LOS + death status for the given hadm_ids straight from MIMIC."""
    print(f"  Loading admissions.csv.gz for LOS + death filter on {len(hadm_ids)} candidates…")
    adm = pd.read_csv(
        MIMIC_HOSP / "admissions.csv.gz",
        usecols=["hadm_id", "admittime", "dischtime", "deathtime"],
        parse_dates=["admittime", "dischtime", "deathtime"],
    )
    adm = adm[adm["hadm_id"].isin(hadm_ids)].copy()
    adm["los_days"] = (adm["dischtime"] - adm["admittime"]).dt.total_seconds() / 86400
    adm["died_in_hospital"] = adm["deathtime"].notna() & (
        adm["deathtime"] >= adm["admittime"]
    ) & (adm["deathtime"] <= adm["dischtime"])
    out = {}
    for _, row in adm.iterrows():
        out[int(row["hadm_id"])] = {
            "los_days": float(row["los_days"]),
            "died_in_hospital": bool(row["died_in_hospital"]),
        }
    return out


def build_case(hadm_id: int, src_dir: Path, out_dir: Path, rng: random.Random) -> dict | None:
    gold_path = src_dir / "gold.json"
    chart_path = src_dir / "pre_discharge.input.txt"
    if not gold_path.exists() or not chart_path.exists():
        return None

    gold = json.loads(gold_path.read_text())
    acute = [d for d in gold.get("acute_diagnoses", []) if not d.get("is_excluded")]
    if len(acute) < 2:
        return None

    # Try multiple candidates in random order, keeping the first hide-worthy + scrubbable one
    candidates = list(acute)
    rng.shuffle(candidates)
    chosen = None
    chosen_patterns: list[str] = []
    for c in candidates:
        if not is_hide_worthy(c["icd_code"], c["title"]):
            continue
        pats = derive_patterns(c["title"])
        if pats:
            chosen = c
            chosen_patterns = pats
            break
    if chosen is None:
        return None

    visible = [d for d in acute if d["icd_code"] != chosen["icd_code"]]
    chart_text = chart_path.read_text()
    scrubbed, log = scrub_text(chart_text, chosen_patterns)
    residual = audit_residual(scrubbed, chosen_patterns)

    out_dir.mkdir(exist_ok=True)
    (out_dir / "chart.txt").write_text(scrubbed)
    (out_dir / "visible_dx.json").write_text(json.dumps(
        [{"icd": d["icd_code"], "title": d["title"]} for d in visible], indent=2))
    (out_dir / "hidden_dx.json").write_text(json.dumps({
        "icd": chosen["icd_code"],
        "title": chosen["title"],
        "icd_version": chosen.get("icd_version"),
    }, indent=2))
    (out_dir / "scrub_log.txt").write_text(
        "\n".join([f"Patterns: {chosen_patterns}", "Source: data", "", *log])
    )

    return {
        "hadm_id": hadm_id,
        "bucket": gold.get("bucket"),
        "hidden_title": chosen["title"],
        "n_visible_dx": len(visible),
        "n_lines_redacted": len(log),
        "patterns_used": chosen_patterns,
        "residual_hits": residual,
        "source": "data",
        "batch": 3,
        "auto_built": True,
    }


def main() -> None:
    rng = random.Random(SEED)
    OUT.mkdir(exist_ok=True)

    manifest_path = OUT / "manifest.json"
    existing = json.loads(manifest_path.read_text()) if manifest_path.exists() else []
    existing_ids = {int(e["hadm_id"]) for e in existing}
    need = TARGET_TOTAL - len(existing)
    print(f"Have {len(existing)} cases; need {need} more.")

    # Pool: data/ only (no data_aki/), excluding existing
    pool_ids = sorted(
        int(d.name) for d in DATA.iterdir()
        if d.is_dir() and d.name.isdigit() and int(d.name) not in existing_ids
    )
    print(f"data/ unused candidates: {len(pool_ids)}")

    # Apply LOS + death filter
    meta = load_admission_metadata(set(pool_ids))
    eligible = [
        h for h in pool_ids
        if h in meta and meta[h]["los_days"] >= LOS_MIN_DAYS and not meta[h]["died_in_hospital"]
    ]
    n_short = sum(1 for h in pool_ids if h in meta and meta[h]["los_days"] < LOS_MIN_DAYS)
    n_died  = sum(1 for h in pool_ids if h in meta and meta[h]["died_in_hospital"])
    print(f"  rejected by LOS<{LOS_MIN_DAYS}d: {n_short}")
    print(f"  rejected by in-hospital death:  {n_died}")
    print(f"  eligible after filters:         {len(eligible)}")

    rng.shuffle(eligible)

    new_entries = []
    flagged: list[dict] = []
    rejected_no_hideworthy_dx = 0
    for hadm_id in eligible:
        if len(new_entries) >= need:
            break
        entry = build_case(hadm_id, DATA / str(hadm_id), OUT / str(hadm_id), rng)
        if entry is None:
            rejected_no_hideworthy_dx += 1
            continue
        new_entries.append(entry)
        if entry["residual_hits"] > 0:
            flagged.append(entry)

    manifest_path.write_text(json.dumps(existing + new_entries, indent=2))
    (OUT / "manifest_batch3_audit.json").write_text(json.dumps({
        "total_built": len(new_entries),
        "rejected_no_hideworthy_dx": rejected_no_hideworthy_dx,
        "with_residual_leak": len(flagged),
        "flagged_cases": flagged,
        "seed": SEED,
        "los_min_days": LOS_MIN_DAYS,
    }, indent=2))

    avg_redactions = (sum(e["n_lines_redacted"] for e in new_entries) / len(new_entries)
                      if new_entries else 0)
    print(f"\nBuilt {len(new_entries)} new cases.")
    print(f"  rejected (no hide-worthy dx):    {rejected_no_hideworthy_dx}")
    print(f"  avg lines redacted per case:     {avg_redactions:.1f}")
    print(f"  cases with first-pass leak:      {len(flagged)}")
    print(f"Manifest now has {len(existing) + len(new_entries)} cases total.")


if __name__ == "__main__":
    main()
