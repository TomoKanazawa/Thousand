"""Prepare cases for DDx evaluation.

For each cases/NN_slug.txt:
  1. Extract the Keywords block as ground truth (MTSamples puts diagnoses there)
  2. Strip the Assessment/Impression/Plan section from the chart (so model can't read the dx)
  3. Strip the Keywords block from the chart (so model can't read the dx)
  4. Strip the Sample Name + Description blocks (those leak the diagnosis too)
  5. Strip the Educational Disclaimer

Writes:
  prepared/NN_slug.input.txt   — sanitized chart
  gold.json                    — ground-truth diagnoses per case
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
CASES_DIR = ROOT / "cases"
PREP_DIR = ROOT / "prepared"
GOLD_PATH = ROOT / "gold.json"

# Section headers that conclude / decide the diagnosis. The chart will be
# truncated at the first match. Matches "IMPRESSION" with or without colon.
ASSESSMENT_HEADER_RE = re.compile(
    r"(?im)^\s*(?:ASSESSMENT(?:\s+AND\s+PLAN|\s*/\s*PLAN)?"
    r"|IMPRESSION(?:\s+AND\s+PLAN|\s*/\s*PLAN)?"
    r"|DIAGNOS[EI]S"
    r"|FINAL\s+DIAGNOSIS"
    r"|DISCHARGE\s+DIAGNOSIS"
    r"|ADMITTING\s+DIAGNOSIS"
    r"|COURSE\s+IN\s+THE\s+ED"
    r"|ED\s+COURSE"
    r"|HOSPITAL\s+COURSE"
    r"|MEDICAL\s+DECISION\s+MAKING"
    r"|MDM"
    r"|CLINICAL\s+IMPRESSION"
    r"|PLAN(?!\s+(?:OF|FOR)))"  # bare "PLAN:" but not "PLAN OF CARE" sub-line
    r"\s*[:\-]?\s*$"
)

# Sections that signal a clinical narrative is present (used as content gate).
CLINICAL_NARRATIVE_HEADERS = re.compile(
    r"(?im)^\s*(CHIEF COMPLAINT|HISTORY OF PRESENT(?: ILLNESS)?|HPI|"
    r"PRESENT ILLNESS|REASON FOR (?:CONSULTATION|VISIT)|HISTORY)\s*:?\s*$"
)

# Header that marks the START of real clinical content. Used to strip any
# disclaimer / Sample Name / Description preamble before this point.
CLINICAL_START_RE = re.compile(
    r"(?im)^\s*(CHIEF COMPLAINT|HISTORY OF PRESENT(?: ILLNESS)?|HPI|"
    r"PRESENT ILLNESS|REASON FOR (?:CONSULTATION|VISIT)|HISTORY)\s*:?\s*$"
)

# Footer noise to strip after the [ASSESSMENT REMOVED] marker.
FOOTER_PATTERNS = [
    re.compile(r"\(Medical Transcription Sample Report\)[^\n]*\n?", re.IGNORECASE),
    re.compile(r"^Intended for:.*?(?=\n\S|\Z)", re.DOTALL | re.IGNORECASE | re.MULTILINE),
    re.compile(
        r"This\s*\n[^\n]+\nreport demonstrates.*?This is not medical advice\.",
        re.DOTALL | re.IGNORECASE,
    ),
    re.compile(r"About This Sample:.*", re.DOTALL | re.IGNORECASE),
    re.compile(r"Go Back to.*", re.DOTALL),
]


def strip_preamble(chart: str) -> str:
    """Drop everything before the first clinical-section header.

    MTSamples files start with Educational Disclaimer + Sample Name + Description
    blocks that frequently name the diagnosis verbatim. The cleanest fix is to
    delete everything up to the first real clinical section header.
    """
    m = CLINICAL_START_RE.search(chart)
    if m is None:
        return chart  # Will fail the has_clinical_narrative check downstream.
    return chart[m.start():]


def strip_footers(chart: str) -> str:
    out = chart
    for pat in FOOTER_PATTERNS:
        out = pat.sub("\n", out)
    return out


def strip_assessment(chart: str) -> str:
    """Truncate the chart at the first Assessment/Impression/Diagnosis header.

    Matches the header even without a trailing colon (MTSamples uses "IMPRESSION"
    on its own line sometimes). We don't preserve any trailing Plan — Plans
    re-state the diagnosis.
    """
    m = ASSESSMENT_HEADER_RE.search(chart)
    if m is None:
        return chart
    return chart[: m.start()].rstrip() + "\n\n[ASSESSMENT REMOVED]\n"


def has_clinical_narrative(chart: str) -> bool:
    """True if the chart contains an HPI / Chief Complaint / Reason for Consult."""
    return CLINICAL_NARRATIVE_HEADERS.search(chart) is not None


def extract_keywords(chart: str) -> tuple[str, list[str]]:
    """Pull the Keywords block; return (chart_without_keywords, keyword_list)."""
    m = re.search(r"\bKeywords:\s*\n(.+?)\Z", chart, re.DOTALL | re.IGNORECASE)
    if not m:
        return chart, []
    raw = m.group(1)
    chart_clean = chart[: m.start()].rstrip()
    # Keywords are comma- or newline-separated phrases.
    parts = re.split(r"[,\n]+", raw)
    kws = [p.strip(" \t,.;:") for p in parts]
    kws = [k for k in kws if k and len(k) > 2]
    return chart_clean, kws


def sanitize_chart(chart: str) -> str:
    """Apply the full sanitization pipeline: preamble → assessment → footers."""
    chart = strip_preamble(chart)
    chart = strip_assessment(chart)
    chart = strip_footers(chart)
    chart = re.sub(r"\n{3,}", "\n\n", chart)
    return chart.strip()


def select_gold_dx(keywords: list[str], specialty_terms: set[str]) -> list[str]:
    """Filter keywords down to plausible diagnoses (drop the specialty label noise)."""
    # First keyword is usually the specialty name (e.g., "general medicine") — drop it.
    out: list[str] = []
    for kw in keywords:
        low = kw.lower().strip()
        if low in specialty_terms:
            continue
        if len(low) < 3:
            continue
        out.append(kw)
    return out


SPECIALTY_NOISE = {
    "general medicine",
    "cardiovascular / pulmonary",
    "cardiovascular",
    "pulmonary",
    "endocrinology",
    "gastroenterology",
    "neurology",
    "consult",
    "history and physical",
    "soap note",
    "soap",
    "followup",
    "follow-up",
    "office visit",
    "er visit",
    "emergency room reports",
}


TARGET_CASES = 200  # harvest pool; prune at review time


def main() -> None:
    PREP_DIR.mkdir(parents=True, exist_ok=True)
    gold: dict[str, dict[str, object]] = {}

    files = sorted(CASES_DIR.glob("*.txt"))
    if not files:
        raise SystemExit(f"No cases in {CASES_DIR}. Run fetch_cases.py first.")

    surviving = 0
    for path in files:
        if surviving >= TARGET_CASES:
            break
        _orig_idx, _, slug = path.stem.partition("_")
        chart = path.read_text(encoding="utf-8")

        chart_no_kw, keywords = extract_keywords(chart)
        gold_terms = select_gold_dx(keywords, SPECIALTY_NOISE)

        # Add title-derived term (often names the primary dx or chief complaint).
        title_term = re.sub(
            r"\b(consult|followup|follow-up|er visit|office visit|h&p|history and physical)\b",
            "",
            slug.replace("_", " "),
            flags=re.IGNORECASE,
        ).strip()
        if title_term and title_term.lower() not in {t.lower() for t in gold_terms}:
            gold_terms.insert(0, title_term)

        if not gold_terms:
            print(f"[warn] {path.name}: no usable keywords — skipping")
            continue

        sanitized = sanitize_chart(chart_no_kw)

        # Gate 1: must contain a clinical narrative section (HPI / Chief Complaint /
        # Reason for Consult). Charts without one are administrative scraps and
        # produce nonsense DDx output.
        if not has_clinical_narrative(sanitized):
            print(f"[thin] {path.name}: no HPI/Chief Complaint/Reason for Consult — skipping")
            continue

        # Gate 2: minimum body length. Even with an HPI header, the body has to
        # have enough material for diagnostic reasoning.
        if len(sanitized) < 800:
            print(f"[thin] {path.name}: chart only {len(sanitized)} chars after sanitize — skipping")
            continue

        # Renumber sequentially across surviving cases (drops gaps from skipped ones).
        surviving += 1
        idx = f"{surviving:02d}"
        input_path = PREP_DIR / f"{idx}_{slug}.input.txt"
        input_path.write_text(sanitized, encoding="utf-8")

        gold[idx] = {
            "slug": slug,
            "gold_terms": gold_terms,
            "primary_dx": gold_terms[0],
            "input_path": str(input_path.relative_to(ROOT)),
        }
        preview = ", ".join(gold_terms[:4])
        print(f"[ok]   {idx} {slug[:40]} → {preview}")

    GOLD_PATH.write_text(json.dumps(gold, indent=2), encoding="utf-8")
    print(f"\n{len(gold)} cases prepared. Gold key: {GOLD_PATH}")


if __name__ == "__main__":
    main()
