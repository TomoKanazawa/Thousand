"""Build the 5-patient 'hide-one-diagnosis' pilot dataset.

For each case: take pre_discharge.input.txt and scrub all mentions of the
ONE target diagnosis we want to hide. Keep all other clinical data + all
other diagnoses intact.

Output:
    pilot_hide_one/<hadm_id>/
        chart.txt           — scrubbed chart
        visible_dx.json     — the OTHER acute dxs the LLM is told the team already has
        hidden_dx.json      — the dx we hid (ground truth)
        scrub_log.txt       — lines removed/redacted, for review
    pilot_hide_one/manifest.json — list of all 5 cases + hidden dx
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path("/Users/tomohiro/Projects/Thousand/ml/prototype_b")
SRC = ROOT / "data"
OUT = ROOT / "pilot_hide_one"

# (hadm_id, hidden_dx_title_from_gold, scrub_patterns, notes)
# scrub_patterns: case-insensitive regex patterns matched per-line.
# A line where ANY pattern matches → entirely redacted as [REDACTED-DX].
# Keep raw clinical evidence; remove narrative naming of the condition.

CASES = [
    {
        "hadm_id": 20514903,
        "bucket": "pulm",
        "hidden_title": "Pneumonia, unspecified organism",
        "patterns": [
            r"\bpneumonia\b",
            r"\bpna\b",
            r"\bpneumonic\b",
            r"\bpneumon",            # pneumon-itis, pneumon-iae
            r"consolidation",         # CXR finding language that often names PNA
            r"infiltrate",            # same — leaves vitals/labs/structured findings intact
        ],
        "notes": "Primary dx. Evidence trail: WBC, fever in vitals, sputum, CXR raw findings.",
    },
    {
        "hadm_id": 28898389,
        "bucket": "renal_gu",
        "hidden_title": "Urinary tract infection, site not specified",
        "patterns": [
            r"\buti\b",
            r"urinary tract infect",
            r"cystitis",
            r"pyelonephritis",
        ],
        "notes": "Primary dx. Evidence: UA, urine culture, dysuria, leukocytosis.",
    },
    {
        "hadm_id": 22501264,
        "bucket": "derm",
        "hidden_title": "Cellulitis of abdominal wall",
        "patterns": [
            r"\bcellulitis\b",
        ],
        "notes": "Co-occurs with abscess (kept). Test: does LLM surface surrounding cellulitis?",
    },
    {
        "hadm_id": 24420954,
        "bucket": "cardiac",
        "hidden_title": "Acute diastolic (congestive) heart failure",
        "patterns": [
            r"heart failure",
            r"\bchf\b",
            r"decompensat",
            r"\bhf[pr]?ef\b",
            r"congestive",
        ],
        "notes": "Secondary dx. Evidence kept: pulmonary edema on CXR, cardiac enlargement, BNP, JVP, dyspnea history.",
    },
    {
        "hadm_id": 28255293,
        "bucket": "gi",
        "hidden_title": "Noninfective gastroenteritis and colitis, unspecified",
        "patterns": [
            r"gastroenteritis",
            r"\bcolitis\b",
            r"\bgastritis\b",
        ],
        "notes": "Primary dx. Evidence: vomiting/diarrhea, electrolyte abnormalities.",
    },
]


def scrub_text(text: str, patterns: list[str]) -> tuple[str, list[str]]:
    """Line-level redaction. Any line matching ANY pattern → [REDACTED-DX].

    Returns (scrubbed_text, log_of_redacted_lines).
    """
    compiled = [re.compile(p, re.IGNORECASE) for p in patterns]
    out_lines: list[str] = []
    log: list[str] = []
    for i, line in enumerate(text.splitlines(), 1):
        if any(rx.search(line) for rx in compiled):
            log.append(f"L{i}: {line.rstrip()}")
            out_lines.append("[REDACTED-DX]")
        else:
            out_lines.append(line)
    return "\n".join(out_lines), log


def main() -> None:
    OUT.mkdir(exist_ok=True)
    manifest = []

    for case in CASES:
        hadm_id = case["hadm_id"]
        src_dir = SRC / str(hadm_id)
        out_dir = OUT / str(hadm_id)
        out_dir.mkdir(exist_ok=True)

        # Load source chart and gold
        chart = (src_dir / "pre_discharge.input.txt").read_text()
        gold = json.loads((src_dir / "gold.json").read_text())

        # Identify the hidden dx record from gold
        hidden_record = None
        visible_records = []
        for dx in gold["acute_diagnoses"]:
            if dx.get("is_excluded"):
                continue
            if dx["title"] == case["hidden_title"]:
                hidden_record = dx
            else:
                visible_records.append(dx)
        if hidden_record is None:
            raise SystemExit(f"hadm_id={hadm_id}: hidden_title not found in gold")

        # Scrub
        scrubbed, log = scrub_text(chart, case["patterns"])

        # Write outputs
        (out_dir / "chart.txt").write_text(scrubbed)
        (out_dir / "visible_dx.json").write_text(
            json.dumps(
                [{"icd": d["icd_code"], "title": d["title"]} for d in visible_records],
                indent=2,
            )
        )
        (out_dir / "hidden_dx.json").write_text(
            json.dumps(
                {
                    "icd": hidden_record["icd_code"],
                    "title": hidden_record["title"],
                    "icd_version": hidden_record.get("icd_version"),
                },
                indent=2,
            )
        )
        (out_dir / "scrub_log.txt").write_text(
            "\n".join([f"Patterns: {case['patterns']}", "", *log])
        )

        manifest.append(
            {
                "hadm_id": hadm_id,
                "bucket": case["bucket"],
                "hidden_title": case["hidden_title"],
                "n_visible_dx": len(visible_records),
                "n_lines_redacted": len(log),
                "notes": case["notes"],
            }
        )

        print(
            f"hadm_id={hadm_id} ({case['bucket']}): "
            f"hidden='{case['hidden_title']}', "
            f"n_visible={len(visible_records)}, "
            f"redacted={len(log)} lines"
        )

    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print(f"\nWrote {len(manifest)} cases to {OUT}/")


if __name__ == "__main__":
    main()
