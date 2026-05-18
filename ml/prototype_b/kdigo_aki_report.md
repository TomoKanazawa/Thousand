# KDIGO-AKI detection in MIMIC-IV

## Aggregate statistics (n=320,679 admissions with ≥2 creatinine values)

- **Meet KDIGO Stage 1+ criteria:** 106,980 (33.4%)
- **AKI coded in discharge ICD list:** 68,815 (21.5%)

### Cross-tab

| | AKI coded | AKI not coded | Total |
|---|---|---|---|
| KDIGO+ | 50,647 | **56,333** | 106,980 |
| KDIGO− | 18,168 | 195,531 | 213,699 |
| Total | 68,815 | 251,864 | 320,679 |

### Undercoding rate
- **Our finding:** 52.7% of KDIGO+ admissions had no AKI code
- **Literature (Cammarata 2024, n=56,820):** 68% AKI undercoding rate

⚠️ Undercoding rate diverges from literature; differences may be due to:
  - Definition of baseline creatinine (we use first 24h min; Cammarata may use prior outpatient)
  - Population (MIMIC is BIDMC ICU-heavy)
  - Coding practices specific to BIDMC

### Candidate set for LLM test
- Total candidates (KDIGO+ but not coded): **56,333**
- These are the cases where, if our LLM correctly flags AKI from chart data,
  it has caught a clinically real condition the hospital failed to document.