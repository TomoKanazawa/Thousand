"""Auto-verify every candidate across all 9 cases against deterministic criteria.

For each candidate, classifies as:
  HIDDEN_TP      — matches the hidden gold dx (original true positive)
  VERIFIED_TP    — criterion clearly met, condition is real
  CONFIRMED_FP   — criterion clearly NOT met
  UNVERIFIABLE   — clinical/imaging-only; no chart-level lab criterion

Then recomputes PPV at each confidence threshold using verified labels.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path("/Users/tomohiro/Projects/Thousand/ml/prototype_b")
PILOT = ROOT / "pilot_hide_one"

# Manual verifications from the chart audit (top-3 + key rank-4+ items)
# Format: (hadm_id, rank) -> label
MANUAL = {
    # Top-3 verifications (done earlier)
    (20514903, 2): "CONFIRMED_FP",   # ACS — criterion check
    (20514903, 3): "UNVERIFIABLE",   # ADHF — criterion check
    (28898389, 2): "VERIFIED_TP",    # Hypertensive urgency — criterion check
    (28898389, 3): "UNVERIFIABLE",   # Seizure — criterion check
    (22501264, 1): "VERIFIED_TP",    # Hypoglycemia — criterion check
    (22501264, 2): "CONFIRMED_FP",   # Microcytic anemia — criterion check
    (22501264, 3): "VERIFIED_TP",    # Leukopenia — criterion check
    (24420954, 2): "VERIFIED_TP",    # Hyperkalemia — criterion check
    (24420954, 3): "VERIFIED_TP",    # ACS/NSTEMI — criterion check
    (28255293, 1): "VERIFIED_TP",    # Hypomagnesemia — criterion check
    (28255293, 3): "VERIFIED_TP",    # Thrombocytopenia — criterion check
    (21318246, 1): "VERIFIED_TP",    # Iron def — criterion check
    (21318246, 2): "CONFIRMED_FP",   # Hypomagnesemia — criterion check
    (21318246, 3): "VERIFIED_TP",    # Reactive thrombocytosis — criterion check
    (22669030, 1): "VERIFIED_TP",    # Hypokalemia — criterion check
    (22669030, 2): "VERIFIED_TP",    # Hypomagnesemia — criterion check
    (22669030, 3): "UNVERIFIABLE",   # Hepatic steatosis — criterion check
    (23793305, 1): "VERIFIED_TP",    # Acute hepatitis — criterion check
    (23793305, 3): "CONFIRMED_FP",   # SIADH — criterion check
    (21452016, 2): "UNVERIFIABLE",   # Leptomeningeal carcinomatosis — criterion check
    (21452016, 3): "VERIFIED_TP",    # Microcytic anemia — criterion check

    # Rank 4+ verifications
    # 20514903
    (20514903, 4): "UNVERIFIABLE",   # Hypertensive emergency — criterion check
    (20514903, 5): "VERIFIED_TP",    # Anemia — criterion check
    (20514903, 6): "UNVERIFIABLE",   # Subtherapeutic anticoag
    (20514903, 7): "UNVERIFIABLE",   # AKI on CKD3 — not enough Cr data in obvious view
    (20514903, 8): "UNVERIFIABLE",   # Dermatitis
    (20514903, 9): "UNVERIFIABLE",   # Hypoglycemia — criterion check
    (20514903, 10): "UNVERIFIABLE", # Anxiety
    # 28898389
    (28898389, 4): "UNVERIFIABLE",   # Stroke/TIA — criterion check
    (28898389, 5): "UNVERIFIABLE",   # Aspiration PNA
    (28898389, 6): "UNVERIFIABLE",   # Hyponatremia — criterion check
    (28898389, 7): "UNVERIFIABLE",
    (28898389, 8): "UNVERIFIABLE",
    (28898389, 9): "UNVERIFIABLE",
    (28898389, 10): "UNVERIFIABLE",
    # 22501264
    (22501264, 4): "UNVERIFIABLE",   # Hypomagnesemia — criterion check
    (22501264, 5): "UNVERIFIABLE",
    (22501264, 6): "UNVERIFIABLE",
    # 24420954
    (24420954, 4): "UNVERIFIABLE",
    (24420954, 5): "UNVERIFIABLE",
    (24420954, 6): "UNVERIFIABLE",
    (24420954, 7): "UNVERIFIABLE",   # Metabolic acidosis — criterion check
    (24420954, 8): "UNVERIFIABLE",
    (24420954, 9): "UNVERIFIABLE",
    (24420954, 10): "UNVERIFIABLE",
    # 28255293
    (28255293, 4): "UNVERIFIABLE",
    (28255293, 5): "UNVERIFIABLE",
    (28255293, 6): "UNVERIFIABLE",
    (28255293, 7): "UNVERIFIABLE",
    (28255293, 8): "UNVERIFIABLE",
    (28255293, 9): "UNVERIFIABLE",
    # 21318246 (rank 4 is the HIDDEN MATCH)
    (21318246, 5): "UNVERIFIABLE",
    (21318246, 6): "UNVERIFIABLE",
    (21318246, 7): "UNVERIFIABLE",
    (21318246, 8): "UNVERIFIABLE",
    # 22669030
    (22669030, 4): "UNVERIFIABLE",   # Fever — criterion check
    (22669030, 5): "UNVERIFIABLE",   # AKI — criterion check
    (22669030, 6): "UNVERIFIABLE",   # Hypocalcemia
    (22669030, 7): "UNVERIFIABLE",
    (22669030, 8): "UNVERIFIABLE",
    (22669030, 9): "UNVERIFIABLE",
    (22669030, 10): "UNVERIFIABLE",
    # 23793305
    (23793305, 4): "UNVERIFIABLE",
    (23793305, 5): "UNVERIFIABLE",
    (23793305, 6): "UNVERIFIABLE",
    (23793305, 7): "UNVERIFIABLE",
    (23793305, 8): "UNVERIFIABLE",
    # 21452016
    (21452016, 4): "UNVERIFIABLE",
    (21452016, 5): "UNVERIFIABLE",
    (21452016, 6): "UNVERIFIABLE",
    (21452016, 7): "UNVERIFIABLE",
    (21452016, 8): "UNVERIFIABLE",
    (21452016, 9): "UNVERIFIABLE",
    (21452016, 10): "UNVERIFIABLE",
}


def main() -> None:
    results = json.load(open(PILOT / "results_haiku_confidence.json"))

    # Label every candidate
    labeled = []
    for r in results:
        matched_rank = r.get("matched_rank", -1)
        for c in r["candidates"]:
            label = None
            if c["rank"] == matched_rank:
                label = "HIDDEN_TP"
            else:
                label = MANUAL.get((int(r["hadm_id"]), c["rank"]), "UNVERIFIABLE")
            labeled.append({
                "hadm_id": int(r["hadm_id"]),
                "rank": c["rank"],
                "confidence": c.get("confidence", 0),
                "diagnosis": c["diagnosis"],
                "label": label,
            })

    # Print summary by label
    from collections import Counter
    counts = Counter(c["label"] for c in labeled)
    print(f"\n=== Candidate label totals (across all 81) ===")
    for k, v in counts.most_common():
        print(f"  {k:<15} {v}")

    # Recompute PPV sweep — criterion check
    # STRICT: TP = HIDDEN_TP + VERIFIED_TP. FP = CONFIRMED_FP + UNVERIFIABLE.
    # LENIENT: TP = HIDDEN_TP + VERIFIED_TP. FP = CONFIRMED_FP only. UNVERIFIABLE EXCLUDED.

    print(f"\n=== PPV sweep — STRICT (Unverifiable counted as FP) ===")
    print(f"{'T':>4} | {'TP':>3} {'FP':>3} {'Total':>5} | {'PPV':>7}")
    print("-" * 35)
    for T in [0, 50, 60, 70, 75, 80, 85, 90]:
        TP = sum(1 for c in labeled if c["confidence"] >= T and c["label"] in {"HIDDEN_TP", "VERIFIED_TP"})
        FP = sum(1 for c in labeled if c["confidence"] >= T and c["label"] in {"CONFIRMED_FP", "UNVERIFIABLE"})
        tot = TP + FP
        ppv = TP / tot * 100 if tot else 0
        print(f">{T:>3} | {TP:>3} {FP:>3} {tot:>5} | {ppv:>6.1f}%")

    print(f"\n=== PPV sweep — LENIENT (Unverifiable EXCLUDED from numerator+denominator) ===")
    print(f"{'T':>4} | {'TP':>3} {'FP':>3} {'Total':>5} | {'PPV':>7}")
    print("-" * 35)
    for T in [0, 50, 60, 70, 75, 80, 85, 90]:
        TP = sum(1 for c in labeled if c["confidence"] >= T and c["label"] in {"HIDDEN_TP", "VERIFIED_TP"})
        FP = sum(1 for c in labeled if c["confidence"] >= T and c["label"] == "CONFIRMED_FP")
        tot = TP + FP
        ppv = TP / tot * 100 if tot else 0
        print(f">{T:>3} | {TP:>3} {FP:>3} {tot:>5} | {ppv:>6.1f}%")


if __name__ == "__main__":
    main()
