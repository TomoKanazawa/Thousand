"""Verify all v2 candidates against deterministic criteria + recompute PPV.

Labels per (hadm_id, rank):
  HIDDEN_TP    — judge matched as the hidden dx
  VERIFIED_TP  — criterion clearly met from chart values
  CONFIRMED_FP — criterion clearly NOT met
  UNVERIFIABLE — clinical/imaging-only, no chart-level lab criterion (or lab value missing)
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path("/Users/tomohiro/Projects/Thousand/ml/prototype_b")
PILOT = ROOT / "pilot_hide_one_v2"

# Manual verification: (hadm_id, rank) -> label. HIDDEN_TPs auto-derived from matched_rank.
MANUAL = {
    # ---------- 20514903 Pneumonia (matched rank 2) ----------
    (20514903, 1): "UNVERIFIABLE",   # ACS — no troponin value visible
    (20514903, 3): "UNVERIFIABLE",   # ADHF — clinical, no BNP
    (20514903, 4): "CONFIRMED_FP",   # Htn urgency — BP 158/91 NOT ≥180/120
    (20514903, 5): "VERIFIED_TP",    # Anemia — Hgb 11.9 (<13)
    (20514903, 6): "VERIFIED_TP",    # Coagulopathy — INR 1.9 (>1.5)
    (20514903, 7): "UNVERIFIABLE",   # AKI — Cr 1.5 no baseline
    (20514903, 8): "UNVERIFIABLE",   # Psoriasis — clinical
    (20514903, 9): "UNVERIFIABLE",   # Anxiety — clinical

    # ---------- 28898389 UTI (matched rank 1) ----------
    (28898389, 2): "UNVERIFIABLE",   # Dehydration — clinical
    (28898389, 3): "VERIFIED_TP",    # Htn urgency — BP 185/101 (≥180)
    (28898389, 4): "UNVERIFIABLE",   # Stroke/TIA — imaging
    (28898389, 5): "UNVERIFIABLE",   # Seizure — clinical
    (28898389, 6): "UNVERIFIABLE",   # Med-induced AMS — clinical
    (28898389, 7): "UNVERIFIABLE",   # Aspiration PNA — imaging
    (28898389, 8): "UNVERIFIABLE",   # SDH — imaging
    (28898389, 9): "UNVERIFIABLE",   # Hypoglycemia — glu redacted
    (28898389, 10): "UNVERIFIABLE",  # Vertebrobasilar — imaging

    # ---------- 22501264 Cellulitis (NOT matched, no HIDDEN_TP) ----------
    (22501264, 1): "CONFIRMED_FP",   # Microcytic anemia — MCV 80 (NOT <80)
    (22501264, 2): "VERIFIED_TP",    # Leukopenia — WBC 3.5, 3.9 (<4.0)
    (22501264, 3): "CONFIRMED_FP",   # Hypomag — Mg 1.9-2.0 (NOT <1.7)
    (22501264, 4): "UNVERIFIABLE",   # T2DM uncontrolled — glu redacted, no HbA1c
    (22501264, 5): "UNVERIFIABLE",   # LE edema/venous insuff/DVT — clinical/imaging
    (22501264, 6): "CONFIRMED_FP",   # Acute blood loss anemia — Hgb stable, no drop
    (22501264, 7): "UNVERIFIABLE",   # Hypoglycemia — glu redacted
    (22501264, 8): "VERIFIED_TP",    # Hyperkalemia — K 5.1 (>5.0)

    # ---------- 24420954 CHF (matched rank 1) ----------
    (24420954, 2): "VERIFIED_TP",    # ACS/NSTEMI — troponin elevated + EKG changes (per HPI)
    (24420954, 3): "VERIFIED_TP",    # Hyperkalemia — K 5.4
    (24420954, 4): "CONFIRMED_FP",   # Met acidosis — HCO3 28-32 (high) → alkalosis
    (24420954, 5): "UNVERIFIABLE",   # COPD exacerbation — clinical
    (24420954, 6): "CONFIRMED_FP",   # Perimenopause — irrelevant for this patient
    (24420954, 7): "CONFIRMED_FP",   # Hypomag — Mg 2.6-3.4 (HIGH, not low)
    (24420954, 8): "CONFIRMED_FP",   # HIT — plt stable, no drop
    (24420954, 9): "VERIFIED_TP",    # Macrocytic anemia — Hgb 9.1 + MCV 99-102
    (24420954, 10): "CONFIRMED_FP",  # Htn urgency — BP 165/92 NOT ≥180/120

    # ---------- 28255293 Gastroenteritis (matched rank 5) ----------
    (28255293, 1): "VERIFIED_TP",    # Hypomag — Mg 1.2 (<1.7)
    (28255293, 2): "VERIFIED_TP",    # Thrombocytopenia — plt 123, 129 (<150)
    (28255293, 3): "CONFIRMED_FP",   # Coagulopathy — INR 1.2 NOT >1.5
    (28255293, 4): "UNVERIFIABLE",   # SDH — imaging
    (28255293, 6): "UNVERIFIABLE",   # IBS — clinical
    (28255293, 7): "UNVERIFIABLE",   # Anxiety — clinical
    (28255293, 8): "UNVERIFIABLE",   # Nutritional def — no B12/folate
    (28255293, 9): "CONFIRMED_FP",   # Hyponatremia — Na 142, 144 (NOT <135)
    (28255293, 10): "CONFIRMED_FP",  # Hypophos — PO4 2.6-2.9 (NOT <2.5)

    # ---------- 21318246 Malnutrition (matched rank 6) ----------
    (21318246, 1): "CONFIRMED_FP",   # Microcytic — Hgb low but MCV 93 (NOT <80)
    (21318246, 2): "CONFIRMED_FP",   # Hypomag — Mg 1.9 (NOT <1.7)
    (21318246, 3): "VERIFIED_TP",    # Met alkalosis — HCO3 30 (>26)
    (21318246, 4): "VERIFIED_TP",    # Iron def — ferritin 9, TSAT 5%
    (21318246, 5): "UNVERIFIABLE",   # Acute gastric dilation — imaging
    (21318246, 7): "VERIFIED_TP",    # Reactive thrombocytosis — plt 464 (>450)
    (21318246, 8): "UNVERIFIABLE",   # Hyperglycemia — glu redacted

    # ---------- 22669030 Cholelithiasis (matched rank 8) ----------
    (22669030, 1): "VERIFIED_TP",    # Hypokalemia — K 3.4 (<3.5)
    (22669030, 2): "CONFIRMED_FP",   # Hypomag — Mg 1.7 (NOT strictly <1.7)
    (22669030, 3): "VERIFIED_TP",    # Hypocalcemia — Ca 7.9 (<8.5)
    (22669030, 4): "VERIFIED_TP",    # Macrocytic — Hgb 7.4 + MCV 100-102
    (22669030, 5): "CONFIRMED_FP",   # Left shift — bands 1, 4, 4 (none >10%)
    (22669030, 6): "UNVERIFIABLE",   # UTI/urinary — no urine values
    (22669030, 7): "UNVERIFIABLE",   # Drug reaction — clinical
    (22669030, 9): "UNVERIFIABLE",   # Fatty liver — imaging
    (22669030, 10): "VERIFIED_TP",   # Hypoalbuminemia — Albumin 3.4 (<3.5)

    # ---------- 23793305 Mononucleosis (matched rank 2) ----------
    (23793305, 1): "VERIFIED_TP",    # Acute hepatitis — AST 235-676, ALT 250-884 (>3× ULN)
    (23793305, 3): "CONFIRMED_FP",   # Hemolytic anemia — Hgb 14.6-15.2 (no anemia)
    (23793305, 4): "UNVERIFIABLE",   # SIADH — Na 131-132 but no urine osm
    (23793305, 5): "CONFIRMED_FP",   # Coagulopathy — INR 1.2-1.3 NOT >1.5
    (23793305, 6): "VERIFIED_TP",    # Hypophos — PO4 2.1 (<2.5)
    (23793305, 7): "CONFIRMED_FP",   # AKI — Cr 0.9-1.0 no Δ
    (23793305, 8): "CONFIRMED_FP",   # Hypomag — Mg 1.9 (NOT <1.7)
    (23793305, 9): "VERIFIED_TP",    # Pharyngitis — sore throat in HPI (clinical evidence)

    # ---------- 21452016 SIADH (matched rank 1) ----------
    (21452016, 2): "UNVERIFIABLE",   # ICH — imaging
    (21452016, 3): "UNVERIFIABLE",   # Meningitis — imaging+CSF
    (21452016, 4): "UNVERIFIABLE",   # Bradycardia — no HR data
    (21452016, 5): "UNVERIFIABLE",   # Htn emergency — no BP data shown
    (21452016, 6): "UNVERIFIABLE",   # Ileus — clinical
    (21452016, 7): "VERIFIED_TP",    # Anemia — Hgb 8.9 (<13)
    (21452016, 8): "UNVERIFIABLE",   # Radiation necrosis — imaging
    (21452016, 9): "VERIFIED_TP",    # Leukocytosis — WBC 11.2 (>11)
    (21452016, 10): "CONFIRMED_FP",  # AKI — Cr 0.8 (normal)
}


def main() -> None:
    results = json.load(open(PILOT / "results_haiku_confidence.json"))
    labeled = []
    for r in results:
        matched_rank = r.get("matched_rank", -1)
        for c in r["candidates"]:
            if c["rank"] == matched_rank:
                label = "HIDDEN_TP"
            else:
                label = MANUAL.get((int(r["hadm_id"]), c["rank"]), "UNVERIFIABLE")
            labeled.append({
                "hadm_id": int(r["hadm_id"]),
                "rank": c["rank"],
                "confidence": c.get("confidence", 0) or 0,
                "diagnosis": c["diagnosis"],
                "label": label,
            })

    from collections import Counter
    counts = Counter(c["label"] for c in labeled)
    print(f"=== Candidate label totals (across all {len(labeled)}) ===")
    for k, v in counts.most_common():
        print(f"  {k:<15} {v}")

    print(f"\n=== PPV sweep — STRICT (Unverifiable counted as FP) ===")
    print(f"{'T':>4} | {'TP':>3} {'FP':>3} {'Total':>5} | {'PPV':>7}")
    print("-" * 35)
    for T in [0, 50, 60, 70, 75, 80, 85, 90]:
        TP = sum(1 for c in labeled if c["confidence"] >= T and c["label"] in {"HIDDEN_TP", "VERIFIED_TP"})
        FP = sum(1 for c in labeled if c["confidence"] >= T and c["label"] in {"CONFIRMED_FP", "UNVERIFIABLE"})
        tot = TP + FP
        ppv = TP / tot * 100 if tot else 0
        print(f">{T:>3} | {TP:>3} {FP:>3} {tot:>5} | {ppv:>6.1f}%")

    print(f"\n=== PPV sweep — LENIENT (Unverifiable EXCLUDED) ===")
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
