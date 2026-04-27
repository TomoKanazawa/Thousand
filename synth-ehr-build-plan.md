# Synthetic EHR Dataset Build Plan (v0.1)

## Goal

Build a synthetic ambulatory EHR-shaped dataset that:
- Looks plausible to a non-physician at a glance
- Has zero PHI (safe for demos, docs, public marketing)
- Includes both structured data and free-text notes
- Comes with a hidden answer key for automated DDx evaluation
- Is reusable as a permanent regression-test substrate

This dataset supports the **CMIO demo** (the audience that signs pilot contracts), not investor or KOL demos.

---

## Build steps

### Step 1 — Pull source data

Working directory: `~/andy-data/`

| Dataset | Purpose | Auth | Size |
|---|---|---|---|
| **Synthea** | Structured skeleton: patient, problem list, meds, labs, longitudinal history | None (open) | ~2 GB for 1000 patients |
| **MIMIC-IV-Note** (`discharge.csv.gz`) | Style reference — inpatient/ED discharge summary voice | PhysioNet ✅ | ~4 GB |
| **MIMIC-IV-ED** | Style reference — ED notes (ambulatory-adjacent) | PhysioNet ✅ | ~3 GB |
| **MTSamples** | Style reference — public-domain ambulatory clinical notes across specialties | None (scrape) | <100 MB |
| **Physician co-founder reference notes** | Few-shot gold standard — 5–10 hand-written clinic notes | N/A | trivial |

**Skipped from Step 1 (deferred):**
- MIMIC-IV on FHIR — not needed for v0.1; we use MIMIC for note style only
- DDXPlus — moves to Step 9 (eval harness), not the dataset build
- MIMIC-IV-Ext-CDM — separate eval track
- NEJM Case Records — separate "wow demo" reel
- MedQA / MedMCQA / PubMedQA — public benchmark phase

**Storage rules:**
- PhysioNet data stays local or on a private encrypted S3 bucket with access logging — never public
- Tag every artifact `synthetic=true` from day one
- DUA constraints apply to MIMIC; do not redistribute

### Step 2 — Set up storage

- Run HAPI FHIR server locally via Docker: `docker run -p 8080:8080 hapiproject/hapi:latest`
- Postgres backend (default in HAPI image)
- Verify FHIR query endpoints respond: `Patient`, `Condition`, `MedicationRequest`, `Observation`, `DiagnosticReport`
- Load Synthea bundles by POSTing each `output/fhir/*.json` to `/fhir`

### Step 3 — Sample & analyze MIMIC + MTSamples notes

- Pull 200–500 discharge summaries from MIMIC-IV-Note
- Pull ~500 ambulatory notes from MTSamples (multi-specialty)
- Pull a sample of MIMIC-IV-ED notes
- Extract style patterns: section headers, abbreviations, sentence length, copy-paste artifacts, SOAP structure
- Build few-shot prompt templates per note type (clinic progress note, ED note, follow-up note)

### Step 4 — Build the note-generation pipeline

For each Synthea patient:
- Read their problem list, active meds, recent labs, vitals, demographics from HAPI
- Prompt Claude (via Bedrock) with a few-shot template + the structured data
- Constrain output to be consistent with the FHIR data
- Generate 3–10 notes per patient across a multi-year timeline

Output: free-text notes attached as `DocumentReference` resources back into HAPI, linked to the patient.

### Step 5 — Inject realistic messiness

Real charts have:
- Copy-paste forward of prior notes (often slightly stale)
- Outdated info (med discontinued in problem list but still listed as active)
- Inconsistent abbreviations across notes
- Occasional contradictions between structured and unstructured data
- Pasted lab values that don't quite match current values

Add these deliberately to a subset of patients. The copilot should handle messiness gracefully — that's the whole product.

### Step 6 — Generate hidden answer key

For each patient:
- Derive ground-truth top-3 DDx from their Synthea condition list
- Store separately from the chart (out-of-band, not in HAPI)
- Format: `{ patient_id, gold_ddx_ranked: [...], reasoning_notes: "..." }`

### Step 7 — Tag and version

- Every record tagged `synthetic=true`
- Bundle as `synth-ehr-v0.1`, frozen for eval reuse
- Subsequent versions: v0.2, v0.3 — never mutate v0.1

### Step 8 — Sanity check

- Physician co-founder reads 10 random charts
- Bar: "plausible at a glance" — not "indistinguishable from real"
- Iterate prompts if charts read as obviously AI-generated

### Step 9 — Build eval harness

- Pull DDXPlus (deferred from Step 1)
- Script: load patient → run copilot → compare ranked DDx to answer key → compute precision@3, recall@3, MRR
- This becomes the permanent regression test
- Add DDXPlus's labeled symptom→DDx pairs as a parallel eval track

---

## Three rules (avoid the trap)

1. **Don't perfect it.** "Plausible to a non-physician at a glance" is the v1 bar. Physicians spot seams; that's fine — they'll see real data in pilots.
2. **Don't train on it.** Eval, demo, and pipeline testing only. Training on synthetic notes is a footgun (model learns synthetic patterns).
3. **Version it strictly.** Never mutate a frozen version. Drift kills eval comparability.

---

## Stack

- **Synthea** → FHIR bundles (skeleton)
- **HAPI FHIR + Postgres** → EHR-shaped storage and query layer
- **Claude via Bedrock** → note generation, anchored to FHIR resources
- **MTSamples + MIMIC + co-founder samples** → style reference corpus

---

## Timeline

1–2 weeks of focused engineering for v0.1, parallel to other workstreams (gold case authoring, App Orchard application, SOC 2 Type I kickoff).

---

## What this is NOT

- ❌ Not training data
- ❌ Not a substitute for real pilot data in validation papers
- ❌ Not the 20–30 handcrafted gold cases (those are a separate, physician-authored asset)
- ❌ Not an FDA submission artifact

It is: a demo + eval substrate that unblocks all UX and pipeline work before pilot data lands.
