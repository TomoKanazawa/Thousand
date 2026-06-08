"""Build batch 2 of the hide-one-dx pilot (5 more cases, different buckets).

Same output layout as batch 1 (pilot_hide_one/<hadm_id>/{chart.txt,
visible_dx.json, hidden_dx.json, scrub_log.txt}). The manifest.json is
EXTENDED to include the new cases (does not overwrite existing entries).

Existing batch-1 case dirs are NOT touched (preserves manual patches).
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path("/Users/tomohiro/Projects/Thousand/ml/prototype_b")
SRC = ROOT / "data"
OUT = ROOT / "pilot_hide_one"

CASES = [
    {
        "hadm_id": 21318246,
        "bucket": "endocrine_metab",
        "hidden_title": "Other severe protein-calorie malnutrition",
        "patterns": [
            r"malnutrition",
            r"malnourished",
            r"cachexia",
            r"cachectic",
            r"protein-?calorie",
            r"\bPCM\b",
        ],
        "notes": "Evidence kept: albumin, prealbumin, BMI, weight loss history, tube feed orders.",
    },
    {
        "hadm_id": 22669030,
        "bucket": "infectious",
        "hidden_title": "Other cholelithiasis without obstruction",
        "patterns": [
            r"cholelith",
            r"gallstone",
            r"gall stone",
            r"biliary stone",
            r"stones in.*gallbladder",
            r"calculi.*gallbladder",
            r"gallbladder.*calculi",
        ],
        "notes": "Evidence kept: gallbladder description, RUQ findings, biliary tree imaging, LFTs.",
    },
    {
        "hadm_id": 23793305,
        "bucket": "infectious",
        "hidden_title": "Infectious mononucleosis",
        "patterns": [
            r"mononucleosis",
            r"\bmono\b",  # standalone 'mono' — abbreviated dx form
            r"\bEBV\b",
            r"epstein[- ]?barr",
            r"monospot",
            r"heterophile",
        ],
        "notes": "Evidence kept: fever, sore throat, atypical lymphocytes, thrombocytopenia, viral prodrome.",
    },
    {
        "hadm_id": 26375598,
        "bucket": "neuro",
        "hidden_title": "Drug-induced myopathy",
        "patterns": [
            r"myopathy",
            r"rhabdomyolysis",
            r"\brhabdo\b",
            r"myositis",
            r"drug[- ]?induced muscle",
        ],
        "notes": "Evidence kept: CK levels, weakness on exam, statin/offending-drug history.",
    },
    {
        "hadm_id": 21452016,
        "bucket": "onc_hem",
        "hidden_title": "Syndrome of inappropriate secretion of antidiuretic hormone",
        "patterns": [
            r"\bSIADH\b",
            r"antidiuretic",
            r"syndrome of inappropriate",
            r"inappropriate ADH",
        ],
        "notes": "Evidence kept: serial Na (132→125), urine Na 89, urine osm 877, serum osm 273 — classic pattern.",
    },
]


def scrub_text(text: str, patterns: list[str]) -> tuple[str, list[str]]:
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
    # Load existing manifest (if any) so we extend, not replace
    manifest_path = OUT / "manifest.json"
    existing = json.loads(manifest_path.read_text()) if manifest_path.exists() else []
    existing_ids = {e["hadm_id"] for e in existing}
    new_entries = []

    for case in CASES:
        hadm_id = case["hadm_id"]
        if hadm_id in existing_ids:
            print(f"  [{hadm_id}] already in manifest — skip")
            continue

        src_dir = SRC / str(hadm_id)
        out_dir = OUT / str(hadm_id)
        out_dir.mkdir(exist_ok=True)

        chart = (src_dir / "pre_discharge.input.txt").read_text()
        gold = json.loads((src_dir / "gold.json").read_text())

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

        scrubbed, log = scrub_text(chart, case["patterns"])

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

        new_entries.append(
            {
                "hadm_id": hadm_id,
                "bucket": case["bucket"],
                "hidden_title": case["hidden_title"],
                "n_visible_dx": len(visible_records),
                "n_lines_redacted": len(log),
                "notes": case["notes"],
                "manual_patches": 0,
                "batch": 2,
            }
        )
        print(
            f"  [{hadm_id}] ({case['bucket']}): "
            f"hidden='{case['hidden_title']}', "
            f"n_visible={len(visible_records)}, redacted={len(log)} lines"
        )

    # Extend manifest
    manifest_path.write_text(json.dumps(existing + new_entries, indent=2))
    print(f"\nAdded {len(new_entries)} cases. Manifest now has {len(existing) + len(new_entries)} total.")


if __name__ == "__main__":
    main()
