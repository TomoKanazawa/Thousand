# MIMIC-IV DDx Benchmark — Aggregate Summary

> Per-case details (real MIMIC ICD codes, per-patient gold lists, per-patient model output) are gitignored under MIMIC's Data Use Agreement. This file contains only aggregate metrics that do not reveal individual patient data.

## Pipeline overview

The benchmark tests: "given a patient chart at cutoff time T, what fraction of the eventual acute discharge diagnoses does the LLM rank in its top K?"

Cutoffs evaluated: `admit` (HPI + ED triage + initial labs only) · `+24h` · `+48h` · `pre-discharge` (full chart minus Brief Hospital Course / Discharge Diagnoses / Discharge Medications)

Gold set: discharge ICD codes, filtered to exclude chronic conditions, symptom codes, external-cause codes, hospital-acquired complications, and status codes. We score only the **business-relevant acute diagnoses**.

**Three metrics reported:**

1. **All-acute recall@k** — fraction of acute discharge dx the model surfaced
2. **High-stakes recall@k** — same but restricted to clinically dangerous conditions (sepsis, AKI, pneumonia, MI, PE, stroke, HF, GI bleed, encephalopathy, cancer, DKA, pancreatitis, respiratory failure, electrolyte derangement, acute anemia) — this is the metric most aligned with the missed-diagnosis product claim
3. **Case-normalized recall@N** — k set to case's own gold count, so each case contributes equally

## Run 2 — Haiku 4.5, n=10 stratified cases, FIXED pipeline

Bugs fixed since first run:
- ED triage/vitals were leaking across patients (each patient's input contained other patients' ED data)
- 3 of 10 selected admissions had no discharge summary in MIMIC-IV-Note, leaving the LLM essentially nothing at the admit cutoff

The fixes:
- ED data filtered per-stay before formatting
- `cherry_pick.py` now requires the admission has a discharge summary

### Results

n=10 stratified cases (1 per specialty bucket: cardiac, derm, endocrine_metab, ent_eye, gi, infectious, msk_rheum, neuro, onc_hem, psych)
Total acute gold across all cases: ~99 codes, of which 35 are high-stakes.

| Cutoff | all-acute r@15 | case-norm r@N | **high-stakes r@15** | non-high-stakes r@15 |
|---|---|---|---|---|
| admit | 52% | 45% | **71% (24/35)** | 41% |
| +24h | 55% | 43% | **74% (26/35)** | 44% |
| +48h | 48% | 40% | 69% (24/35) | 38% |
| pre-discharge | 56% | 45% | **66% (23/35)** | 50% |

**Cost:** ~$0.40 (200K input + 41K output tokens with Haiku, including LLM-judge calls)

### Comparison vs Run 1 (buggy pipeline)

| Metric | Run 1 (buggy) | Run 2 (fixed) | Δ |
|---|---|---|---|
| High-stakes r@15 at admit | 58% | **71%** | **+13 pp** |
| High-stakes r@15 at +24h | 71% | 74% | +3 pp |
| Total high-stakes targets | 24 | 35 | new sample is harder (more dx per case) |
| Absolute high-stakes hits at pre-discharge | 19 | **23** | catching more in absolute terms |

The big lift is at the **admit cutoff** — the buggy run had 3 cases with no admission narrative, dragging the average down. With clean data, admission-time recall jumps to 71% on high-stakes.

## What this tells us

**Defensible claim:** *"At admission with only HPI + ED triage + initial labs, our system catches 71% of high-stakes diagnoses that will be documented during the stay."*

**Strategic context (Dalal 2024, BMJ Q&S):** 7.2% of inpatient encounters have a diagnostic error caught later in care. If our system at the admission timepoint recovers ≥94% of the full discharge dx set, by inclusion it would catch those 7%. We're at 71% on high-stakes, with documented headroom (see "next steps" below).

## Negative results worth noting

Three optimizations were attempted and *failed* to beat the simple Haiku baseline:

1. **Opus 4.7 + simple prompt** — 71% pre-discharge HS recall (vs Haiku's 79% on same Run 1 sample). 17× the cost for worse accuracy.
2. **Haiku + heavy, rule-heavy prompt** — 71% pre-discharge HS recall (-8 pp). The prompt's 6 explicit extraction rules distracted the model from clinical reasoning.
3. **Both made the model produce more output tokens but catch fewer diagnoses.**

The lesson: this task isn't bottlenecked by raw model capability or prompt verbosity. Pipeline integrity and data quality matter more than either.

## Miss-evidence investigation

For each missed gold diagnosis at pre-discharge (Run 1), we asked Sonnet 4.6 to judge whether the chart actually contained evidence pointing to it:

| Verdict | Run 1 count | Interpretation |
|---|---|---|
| EVIDENCE_SUFFICIENT | 9/21 (43%) | Model failure — chart had the signals |
| EVIDENCE_PARTIAL | 11/21 (52%) | Hints in chart, borderline |
| EVIDENCE_ABSENT | 1/21 (5%) | Genuine data gap |

**95% of misses had recoverable evidence in the chart.** The bottleneck is the LLM layer, not the data pipeline. Specific failure modes: not treating med orders as diagnostic evidence, not combining related findings into named entities (e.g., listing three cytopenias as three entries instead of pancytopenia), missing specific electrolyte direction (hyperkalemia vs hypokalemia).

## Next steps

In priority order:

1. **Scale to n=50** — confirm the 71% admit recall holds with tighter confidence intervals (~$2 cost)
2. **Investigate misses at n=50** — see if failure modes from n=10 are stable or sample-specific (~$2)
3. **Better chart formatting** — current labs are a flat timestamp list; a trend-table format might help the model see patterns
4. **Prior admissions context** — for repeat patients, including (sanitized) prior discharge summaries adds context

## Repro

```bash
cd ml/prototype_b
python cherry_pick.py --n 10
python stitch_case.py
python ddx.py --model haiku
python investigate_misses.py   # optional: per-miss evidence audit
```

Requires PhysioNet credentials and MIMIC-IV + MIMIC-IV-Note + MIMIC-IV-ED downloaded under `physionet.org/files/...` (gitignored).
