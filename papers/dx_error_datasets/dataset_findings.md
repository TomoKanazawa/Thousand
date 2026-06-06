# Dataset Findings — what data each study actually used

**Goal:** find a dataset with **(a) detailed patient records** AND **(b) physician-reviewed diagnostic-error labels** that we could access for our research.

Read each paper's Methods one by one. Bottom line up front: **several have exactly what we want (real charts + Safer Dx physician adjudication), but all are PHI / request-or-collaboration only. The one *publicly downloadable* set (MEDEC) has synthetic errors, not real ones.**

---

## Summary table

| # | Study | Dataset (source) | N reviewed | Detailed records? | Physician-reviewed dx errors? | Access |
|---|---|---|---|---|---|---|
| 1 | Dalal 2024 | **Brigham/MGB** inpatient (1 center) | 675 (of 9,147) | ✅ full chart | ✅ Safer Dx + DEER, 2 reviewers + panel | PHI · request/collab |
| 2 | **Auerbach/UPSIDE 2024** | **29 US academic centers**, inpatient (ICU transfer/died), 2019 | **2,428** | ✅ full chart | ✅ 2 physicians, both must agree | PHI · single-IRB · restricted |
| 3 | Raffel 2020 | **UCSF/ZSFG** (1 center), 7-day readmissions, 2019 | 376 (21 errors) | ✅ full chart | ✅ Safer Dx (11-item), 2 physicians | PHI · single center |
| 4 | Auerbach COVID-PUI 2023 | **~10 centers**, COVID-PUI inpatients | 257 (36 errors) | ✅ full chart | ✅ trained reviewers, gold-standard calibration | PHI · "available on request" |
| 5 | Mahajan 2025 | **Multiple pediatric EDs** (CHOP etc.), 2019 | 2,937 trigger+ → 151 Safer Dx (76 MOIDs) | ✅ full chart | ✅ Revised Safer Dx + expert panel | PHI · pediatric |
| 6 | Haimovich 2025 | **Beth Israel Lahey, 10 EDs** | 357 | ✅ full ED chart | ✅ Safer Dx, 2 physicians (+ Claude) | PHI · "data will not be shared" |
| 7 | Singh 2012 | **Houston VA** primary care, 2007 | 212,165 queried → ~1,300 reviewed (886 trigger+) | ✅ full chart | ✅ blinded physicians + 3rd reviewer | VA PHI · restricted |
| 8 | Murphy 2024 *(unverified)* | telehealth (likely VA) | ~100 (11 MODs) | ✅ likely | ✅ likely Safer Dx | PHI · citation unconfirmed |
| 9 | **MEDEC 2025** | clinical notes (US med-board + UW/MS notes) | 3,848 notes | ⚠️ notes, not full EHR | ❌ **errors synthetically introduced** | ✅ **publicly downloadable** |
| 10 | Shojania autopsy meta | 53 autopsy series (aggregate) | — | ❌ no note-level data | ✅ autopsy = truth, but aggregate only | public (no patient data) |

---

## Per-study: the exact dataset

1. **Dalal 2024** — one center (Mass General Brigham), general-medicine inpatients; 675 charts reviewed (stratified from 9,147), full-record retrospective review with Safer Dx + DEER by 2 adjudicators + expert panel.
2. **Auerbach/UPSIDE 2024** — random sample of adults at **29 academic medical centers** who were transferred to ICU or died in 2019; **2,428 full inpatient records**, each adjudicated by 2 trained physicians (consensus required). The largest, most rigorous multicenter Safer Dx corpus.
3. **Raffel 2020** — single urban academic hospital (UCSF/Zuckerberg SF General); adults readmitted within 7 days; **376 readmissions**, 21 diagnostic errors; validated 11-item Safer Dx, 2 physicians.
4. **Auerbach COVID-PUI 2023** — ~10 hospital-medicine sites; patients hospitalized *under investigation* for COVID-19; **257 charts, 36 errors**; same trained-reviewer Safer Dx pipeline as UPSIDE. Data "available on request."
5. **Mahajan 2025** — multiple **pediatric** EDs; e-trigger screen of **2,937** records → Revised Safer Dx on 151 → **76 missed opportunities (MOIDs)**; consensus + multidisciplinary expert panel.
6. **Haimovich 2025** — Beth Israel Lahey, **10 EDs**, 357 encounters; full ED charts; Safer Dx 2-physician gold standard + Claude. Paper states **"Data will not be shared as they include PHI."**
7. **Singh 2012** — Houston VA primary care; e-trigger queries over **212,165 visits** → blinded physician review of trigger-positive + control visits (~1,300; 886 trigger+), 2007 data; 3rd reviewer for disagreements.
8. **Murphy 2024** — telehealth, ~100 charts, 11 MODs *(citation unverified — see `08_…md`)*.
9. **MEDEC 2025** — **first publicly available** medical-error benchmark; 3,848 clinical texts; errors are **synthetically introduced** (or drawn from med-board cards), then human-validated — i.e., **not real, organically-occurring diagnostic errors**.
10. **Shojania autopsy meta** — 53 autopsy series; gold-standard post-mortem truth, but **only aggregate discrepancy rates, no antemortem patient-level notes**.

---

## Bottom line — which fits "detailed records + physician-reviewed dx errors"

**Best fits (have exactly what we want):**
- **#2 Auerbach/UPSIDE** — biggest (2,428), multicenter, rigorous 2-physician Safer Dx. Top target.
- **#1 Dalal** — Brigham, 675, Safer Dx + DEER, full-record.
- Then #3 Raffel, #4 Auerbach-PUI, #6 Haimovich, #7 Singh (all real charts + Safer Dx, smaller or narrower).

**The catch:** **none are publicly downloadable.** Every dataset with *real* physician-reviewed errors is single/multi-institution PHI → obtainable only via **collaboration / IRB / DUA**. The only public set (**MEDEC**) uses **synthetic errors**, so it's good for benchmarking detection *mechanics* but not for studying real missed diagnoses.

**Implication for us:**
1. There is **no off-the-shelf public dataset** of detailed records + real adjudicated dx errors. Confirms we either **partner** (UPSIDE/Auerbach group at UCSF, or Dalal/Brigham — same Boston cluster as Haimovich/Rodman) or **build our own** (what our AKI/MIMIC work does).
2. All these use **Safer Dx physician adjudication** — that's the standard label method we'd adopt for validation.
3. Most are **revealed/delayed** errors (trigger-based), not silent-undetected — same caveat as before.
