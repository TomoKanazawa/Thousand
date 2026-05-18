# MIMIC-IV DDx Benchmark — Aggregate Summary

> Per-case details (real MIMIC ICD codes, per-patient gold lists, per-patient model output) are gitignored under MIMIC's Data Use Agreement. This file contains only aggregate metrics that do not reveal individual patient data.

## Pipeline overview

The benchmark tests: *"given a patient chart at cutoff time T, what fraction of the eventual acute discharge diagnoses does the LLM rank in its top K?"*

Cutoffs evaluated: `admit` (HPI + ED triage + initial labs only) · `+24h` · `+48h` · `pre-discharge` (full chart minus Brief Hospital Course / Discharge Diagnoses / Discharge Medications)

Gold set: discharge ICD codes, filtered to exclude chronic conditions, symptom codes, external-cause codes, hospital-acquired complications, and status codes. We score only the **business-relevant acute diagnoses**.

**Three metrics reported:**

1. **All-acute recall@k** — fraction of acute discharge dx the model surfaced
2. **High-stakes recall@k** — restricted to clinically dangerous conditions (sepsis, AKI, pneumonia, MI, PE, stroke, HF, GI bleed, encephalopathy, cancer, DKA, pancreatitis, respiratory failure, electrolyte derangement, acute anemia) — this is the metric most aligned with the missed-diagnosis product claim
3. **Case-normalized recall@N** — k set to case's own gold count, so each case contributes equally

## Headline result — Haiku 4.5, n=50 stratified cases

| Cutoff | all-acute r@15 | case-norm r@N | **high-stakes r@15** | non-high-stakes r@15 |
|---|---|---|---|---|
| admit | 58% | 45% | **73% (88/120)** | 51% |
| **+24h** | 63% | 50% | **79% (95/120)** | 55% |
| +48h | 62% | 47% | 78% (93/120) | 54% |
| pre-discharge | 59% | 46% | 77% (92/120) | 51% |

**Cost: $1.89** for 200 DDx calls + 200 judge calls (Haiku for both).

**The model is reliably biased toward high-stakes conditions.** Gap between HS and nHS recall: +22 to +26 pp across cutoffs. The system spends its 15 top slots on clinically dangerous diagnoses rather than incidental findings — exactly the inductive bias a copilot should have.

### Pitch-ready statement

> *"At admission + 24 hours of workup data, our system surfaces 79% of high-stakes diagnoses that will be documented during the stay. The recall curve plateaus at +24h — additional data beyond that does not meaningfully improve recall, suggesting the model is essentially saturated by the first day's findings."*

### Curve shape

```
HS recall@15:
  admit          73%
  +24h           79%   ← peak
  +48h           78%
  pre-discharge  77%
```

Recall **plateaus at +24h** rather than monotonically climbing. Most predictive signal is in the first day of workup.

## Miss-evidence investigation (n=50)

For each of the 153 missed gold diagnoses at pre-discharge, Sonnet 4.6 judged whether the chart actually contained evidence pointing to it.

### Aggregate verdicts

| Verdict | Count | %  |
|---|---|---|
| **EVIDENCE_SUFFICIENT** | **96** | **63%** |
| EVIDENCE_PARTIAL | 45 | 29% |
| EVIDENCE_ABSENT | 12 | 8% |

### High-stakes misses only (n=28)

| Verdict | Count | %  |
|---|---|---|
| **EVIDENCE_SUFFICIENT** | **18** | **64%** |
| EVIDENCE_PARTIAL | 10 | 36% |
| **EVIDENCE_ABSENT** | **0** | **0%** |

**Zero high-stakes misses are due to missing data.** For dangerous conditions, every miss had at least some chart evidence — the LLM layer is the bottleneck, not the data pipeline.

**92% of all misses have recoverable evidence** in the chart. The path to higher recall runs through model behavior (smarter chart formatting, better extraction logic), not adding more data sources.

## Strategic context (Dalal 2024, BMJ Q&S)

7.2% of inpatient encounters have a diagnostic error caught later in care. If our system at the admission timepoint recovers ≥94% of the full discharge dx set, by inclusion it would catch those 7%. We're at 73% on high-stakes at admit. The headroom is real, and the miss-evidence investigation shows the chart almost always has the signal — closing the gap is a model-behavior problem.

## Negative results worth recording

Three optimizations were attempted on the n=10 pilot and failed to beat the simple Haiku baseline:

1. **Opus 4.7 + simple prompt** — 71% pre-discharge HS recall (vs Haiku's 79% on the same sample). 17× cost for worse accuracy.
2. **Haiku + heavy, rule-based prompt** — 71% pre-discharge HS recall (-8 pp). The prompt's 6 explicit extraction rules distracted the model from clinical reasoning.
3. **Both produced more output tokens for fewer correct diagnoses.**

This task is not bottlenecked by raw model capability or prompt verbosity. Pipeline integrity, gold-set definition, and data quality matter more than either.

## Pipeline corrections during this work

Two real bugs were fixed; both were dragging the headline number:

1. **ED triage/vitals were leaking across patients** — each stitched chart contained other patients' ED vitals (timestamps spanning decades made this visible). Fixed by filtering triage/vitals to each patient's own `stay_id` before formatting.
2. **3 of the original 10 cherry-picked admissions had no discharge summary in MIMIC-IV-Note at all**, leaving the LLM with no admission narrative. Fixed by requiring the admission have a discharge summary in `cherry_pick.py`.

After fixes, admission-time high-stakes recall went from 58% → 71% (n=10) → 73% (n=50).

## Repro

```bash
cd ml/prototype_b
python cherry_pick.py --n 50
python stitch_case.py
python ddx.py --model haiku
python investigate_misses.py   # optional: per-miss evidence audit
```

Requires PhysioNet credentials and MIMIC-IV + MIMIC-IV-Note + MIMIC-IV-ED downloaded under `physionet.org/files/...` (gitignored).

## Next steps (in priority order)

1. **Better chart formatting** — current labs are a flat timestamp list; a trend-table format may help the model see patterns it currently misses
2. **Tighten chronic-code filter** — some misses are chronic PMH items leaking through our exclusion filter, inflating the apparent miss count
3. **Prior admissions context** — for repeat patients, including (sanitized) prior discharge summaries adds real context
4. **Scale to n=200+** — for publication-grade confidence intervals
5. **Physician spot-review** — once a co-founder is available, validate that "high-stakes recall" matches clinical judgment of which misses actually matter
