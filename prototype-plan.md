# Prototype Plan — Two-Stage Validation

Run before committing to the full synth-EHR pipeline (`synth-ehr-build-plan.md`).

## The core loop (same for both options)

```
patient chart  →  LLM with DDx prompt  →  ranked disease list  →  compare to known answer
```

Everything in both options is variations on this loop at different scales.

---

## Option A — Smallest useful thing

**Goal:** answer "does the LLM rank DDx well at all?" before building any infrastructure.

**Inputs:**
- **MTSamples** — 5–10 hand-picked ambulatory notes (free, public, no auth)
- That's it.

**Method:**
1. Pick MTSamples cases where the diagnosis is clearly stated in the Assessment section
2. **Strip the Assessment section** so the LLM can't cheat
3. Feed the stripped chart to Claude with a DDx prompt
4. Score: did the stated diagnosis land in the top 5?

**Ground truth:** the stripped Assessment line (self-extracted, no physician required).

**Stack:**
- ~50 lines of Python
- `cases/*.txt`, `gold.json`, `ddx.py`, `results.md`
- Direct Anthropic API, Haiku 4.5

**Time / cost:** 2–4 hours / under $1.

**What it proves:**
- ✅ Core loop works
- ✅ Prompt produces sensible output
- ✅ Failure modes are visible
- ❌ Doesn't prove FHIR ingestion
- ❌ Doesn't prove ambulatory style realism
- ❌ Not a CMIO demo

**When to do this:** week 1, before anything else.

---

## Option B — Full pipeline at small scale (10 patients)

**Goal:** answer "does the synthetic-data pipeline produce useful end-to-end output?"

**Inputs:**
- **Synthea** — generate 10 patients (FHIR skeleton)
- **MIMIC-IV-Note** — note style reference
- **MIMIC-IV-ED** — note style reference (ambulatory-adjacent)
- **MTSamples** — true ambulatory style reference
- **Co-founder's 5–10 reference notes** — few-shot gold standard

**Method:** the full pipeline from `synth-ehr-build-plan.md`, just at n=10 instead of n=1000.

**Ground truth:** auto-derived from Synthea's condition list per patient.

**Stack:**
- Synthea + HAPI FHIR + Postgres + Bedrock/Anthropic API + eval harness
- All Step 1–9 infrastructure

**Time / cost:** 1–2 weeks / ~$10.

**When to do this:** only after Option A produces good output.

---

## Eval comparison

| | Option A | Option B |
|---|---|---|
| Ground truth source | Stripped Assessment | Synthea condition list |
| Human required | No | No |
| Scoring | Automatable | Automatable |
| Scale ceiling | ~hundreds (manual curation) | Unlimited |
| Re-run cost | Manageable | Trivial |
| **Honesty as eval** | **High** — real notes, real physician reasoning | **Lower** — notes generated from the answer, leakage risk |

**Critical risk in Option B:** because notes are generated *from* the condition list, the generation prompt may make the diagnosis too obvious. A 95% score on B with a 60% score on A means leakage, not progress.

**Best practice:**
- Option B = fast feedback loop during prompt iteration
- Option A = honesty check before claiming any accuracy number externally
- Run both; treat divergence as a signal, not noise.

---

## Sequence

1. **Week 1:** Option A. 10 cases, hand-picked. Eyeball + auto-score.
2. **Decision gate:** If output is bad, fix prompt/model — don't build infrastructure around a broken loop.
3. **Week 2–3:** Option B if A passed. Build full pipeline at n=10.
4. **Week 4+:** Scale Option B to n=1000 per `synth-ehr-build-plan.md`.

## What goes where

| Concern | Doc |
|---|---|
| Why these datasets vs others | `dataset-strategy.md` |
| Full pipeline build at scale | `synth-ehr-build-plan.md` |
| Two-stage prototype before that | **this doc** |
