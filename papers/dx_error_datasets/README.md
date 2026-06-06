# Diagnostic-Error Datasets — Candidate Sources for Our Research

Studies built on **real patient records with physician-adjudicated missed/delayed
diagnosis labels** — i.e., potential gold-standard data to validate our detection
method against (the labels our AKI work currently lacks).

**Filing convention:** `NN_FirstAuthorYEAR_topic.pdf` (matches parent `papers/`).
PDFs are gitignored; `.md` notes are committed.

**All are request-only — none publicly downloadable.** Access = collaboration /
IRB / DUA, not download.

---

## Direct hits — real records + physician-adjudicated dx-error labels (8)

| # | Save as | Study | Data | Labels |
|---|---|---|---|---|
| 1 | `01_Dalal2024_brigham-adverse-dx.pdf` | Dalal et al. 2024 | Brigham, **675 cases** | SaferDx + DEER (2 reviewers) |
| 2 | `02_Auerbach2024_UPSIDE.pdf` | Auerbach et al. 2024 | UCSF / **29 centers, 2,428 cases** | SaferDx |
| 3 | `03_Raffel2020_readmissions.pdf` | Raffel et al. 2020 | UCSF, **376 readmissions, 21 errors** | physician review |
| 4 | `04_Auerbach2023_COVID-PUI.pdf` | Auerbach et al. 2023 (COVID-19 PUI) | **8 centers, 257 charts, 36 errors** | physician review |
| 5 | `05_Mahajan2025_pediatric-ED.pdf` | Mahajan et al. 2025 | **5 pediatric EDs, 151 reviewed, 76 MODs** | physician review |
| 6 | `06_Haimovich2025_etrigger-LLM.pdf` *(have: `papers/30_…`)* | Haimovich et al. 2025 | **10 EDs, 317 cases** | SaferDx + Claude |
| 7 | `07_Singh2012_VA-primary-care.pdf` | Singh et al. 2012 | VA primary care, **1,300 records (886 trigger+)** | physician review |
| 8 | `08_Murphy2024_telehealth.pdf` | Murphy et al. 2024 | telehealth, **100 reviewed, 11 MODs** | physician review |

## Partial / different format (2)

| # | Save as | Study | Why partial |
|---|---|---|---|
| 9 | `09_BenAbacha2025_MEDEC.pdf` | MEDEC (Ben Abacha et al. 2025) | **488 real EHR notes**, but errors are **synthetically introduced** |
| 10 | `10_Shojania_autopsy-discrepancy.pdf` | Autopsy-discrepancy meta-analyses (Shojania; ICU meta) | gold-standard dx, but **no antemortem note-level data** |

---

## Notes for evaluating these as data sources
- **MOD** = missed opportunity for diagnosis.
- **Strongest fit:** large N + SaferDx labels + inpatient → **Auerbach/UPSIDE (2,428)** and **Dalal (675)**. Both are the validation-label gold standard our KDIGO lab proxy can't provide.
- **Caveat (recurring theme):** these are mostly **revealed/delayed** errors (trigger-based: ICU transfer, death, readmission), not the **silent never-detected** segment we target. Useful for adjudication *method* and for label-paired validation, less so as a denominator for "undetected."
- **MEDEC** = synthetic errors → good for benchmarking error-*detection* mechanics, not real missed-dx prevalence.
- **Access reality:** all PHI / single-institution → realistic path is collaboration under their IRB or a de-identified derived dataset, not a data download. Boston/Harvard overlap (Dalal, Haimovich, Rodman) and UCSF (Auerbach, Raffel) are the two clusters to target.
