# AKI Hit-Rate Reslice

Source: `results_aki_haiku.json` × `tier2_verification.json` × `selected_admissions_aki.json`. No API calls.

## Cutoff: `admit`

| Slice | n | hit@5 | hit@15 |
|---|---|---|---|
| All (original) | 100 | 49/100 (49%) | 94/100 (94%) |
| Severe (KDIGO Stage 3) | 15 | 9/15 (60%) | 14/15 (93%) |
| Moderate (KDIGO Stage 2) | 3 | 2/3 (67%) | 3/3 (100%) |
| Mild (KDIGO Stage 1) | 82 | 38/82 (46%) | 77/82 (94%) |
| NOT_MENTIONED (clean) | 54 | 24/54 (44%) | 49/54 (91%) |
| Severe ∩ NOT_MENTIONED (most defensible) | 11 | 5/11 (45%) | 10/11 (91%) |

## Cutoff: `plus24h`

| Slice | n | hit@5 | hit@15 |
|---|---|---|---|
| All (original) | 99 | 32/99 (32%) | 64/99 (65%) |
| Severe (KDIGO Stage 3) | 15 | 6/15 (40%) | 11/15 (73%) |
| Moderate (KDIGO Stage 2) | 3 | 1/3 (33%) | 2/3 (67%) |
| Mild (KDIGO Stage 1) | 81 | 25/81 (31%) | 51/81 (63%) |
| NOT_MENTIONED (clean) | 54 | 10/54 (19%) | 28/54 (52%) |
| Severe ∩ NOT_MENTIONED (most defensible) | 11 | 3/11 (27%) | 8/11 (73%) |

## Verdict × severity distribution (n=100)

| Severity | NOT_MENTIONED | IMPLIED | MENTIONED | Total |
|---|---|---|---|---|
| severe | 11 | 4 | 0 | 15 |
| moderate | 1 | 2 | 0 | 3 |
| mild | 42 | 39 | 1 | 82 |