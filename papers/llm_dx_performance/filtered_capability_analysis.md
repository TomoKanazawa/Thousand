# LLM Diagnostic Capability — Filtered Analysis & White Space

**Purpose:** Cut through the "LLMs are great at diagnosis" hype by progressively
filtering our 17-paper set down to studies that actually test *our* problem
(open-ended detection of an undocumented condition, answer withheld, on raw EHR).
Identifies where the real evidence is — and the unfilled gap our AKI work occupies.

Per-paper detail lives in `key_findings_llm.md`. This file is the synthesis.

---

## The cumulative filters

We narrowed the set one constraint at a time:

### Filter 1 — Was the answer *withheld* from the input?
(Many "detection" papers had the diagnosis sitting in the input text → easy mode.)

- **Answer IN the input (extraction, not diagnosis):** Pan (diagnosis written in full chart), Harada (answer in the published case write-up), partly Estiri/CLABSI.
- **Answer WITHHELD (must infer):** Kanjee, Brodeur, McDuff, Cabral, Tu, Barile, Goh, Healy, Haimovich, Shyr/UDN, Boussina. → **11 survive.**

### Filter 2 — Real patient data (not synthetic / simulated / published narrative)?
| Paper | Data type | Real raw EHR? |
|---|---|---|
| Haimovich | Real ED charts (10 EDs) | ✅ raw EHR |
| Boussina | Real ED encounters, real-time | ✅ raw EHR |
| Brodeur (ED sub-study) | 76 actual ED cases | ✅ (that sub-experiment) |
| Shyr / UDN | Real patients, **tidy intake summaries** | ⚠️ real patients, curated input |
| Kanjee, McDuff, Brodeur-CPC, Barile | Published case reports (real pts, polished) | ❌ curated |
| Cabral | Clinical cases/vignettes | ❌ curated |
| Tu (AMIE) | **Patient-actors** | ❌ simulated |
| Goh, Healy | Clinical vignettes | ❌ constructed |

→ Real patient data survivors: **Haimovich, Boussina, Brodeur-ED, Shyr/UDN.**
**Note:** all the famous "LLMs beat doctors" results (Kanjee, McDuff, Tu, Brodeur-CPC) **drop out here** — they ran on published or simulated cases, not real EHR.

### Filter 3 — Did it test *open-ended diagnostic capability* (generate/name the diagnosis)?
| Paper (real data) | What it actually tested | Open-ended diagnosis? |
|---|---|---|
| **Brodeur** (ED subset) | Produce the dx from a real ED case vs attendings | ✅ Yes |
| **Shyr / UDN** | Name the dx from a real patient summary | ✅ Yes |
| Haimovich | Binary "was a dx missed? yes/no" | ❌ miss-*detection*, not diagnosing |
| Boussina | "Will this patient become septic?" | ❌ single-condition *prediction* |

→ Only **Brodeur-ED** and **Shyr/UDN** test diagnostic capability on real patients.

---

## The two survivors — what they test & tell

### Brodeur (76-case ED sub-study) — the "easy/common" end
- **Tests:** real ED cases at 3 workup points (triage → testing → treatment); o1-preview produces the dx vs 2 attendings.
- **Tells:** at **initial triage**, o1-preview exact-or-close **67.1%** vs attendings **55.3% / 50.0%** — **out-diagnosed ER doctors on real patients, earliest in the workup.** Strongest "LLM ≥ doctors on real patients" datapoint.
- **Caveats:** only 76 cases; input was a **structured case presentation** (curated from chart, not raw EHR); text-only; research eval, not deployment.

### Shyr / UDN — the "hard/rare" end
- **Tests:** 90 genuinely **undiagnosed** real patients (hardest in medicine); GPT-4o / Llama-3.1-8B name the dx from a clinical summary; vs expert clinical review.
- **Tells:** GPT-4o named the final dx **13.3%** (helpful ddx 23.3%) — **mostly wrong (~87% miss)** — **but still beat expert review's 5.6%** (~2.4×), at **$0.03 / 5 s** per case.
- **Caveats:** input was a **tidy intake summary**, not raw chart; often got the condition but not the specific genetic variant.

### What the two together tell us
1. **Capability is governed by case difficulty + data cleanliness, not the model.** Common + clean input → superhuman (67%); rare + incomplete → mostly fails (13%) but still additive. Same model era, opposite results.
2. **Both withheld the answer on real patients but fed *curated* input.** They measure diagnostic *reasoning on real cases*, NOT extraction-from-raw-EHR.
3. **The floor is "additive," not "useless"** — even at 13%, the LLM beat expert review. An LLM needn't be right often to add value as a second look.

---

## The white space (why our AKI work is novel)

Stacking all filters — **answer withheld + real patient data + open-ended diagnosis + raw/messy EHR** — **no paper in the set qualifies.**
- Diagnosis on real patients → only on **curated presentations** (Brodeur, Shyr).
- Raw EHR → only for **detection/prediction**, not open-ended diagnosis (Haimovich, Boussina).

**Our AKI work occupies the unfilled cell:** open-ended detection of an *undocumented* condition, answer withheld, on **raw admission-window EHR**.

### Where our task lands on the difficulty axes
- **Favorable:** AKI is a **common** condition → Brodeur regime, not Shyr regime (commonness helps).
- **Unfavorable:** input is **raw, messy, admission-window EHR** and the condition is **undocumented** → harder than either paper's curated input.

So: strong on the commonness axis, unexplored/hard on the data-messiness axis. That mix is exactly what a collaboration (real progress notes + physician adjudication) would pin down.

---

## Best-supported claim about current LLM capability (2026)

> Frontier LLMs are good enough to act as a **high-sensitivity, human-in-the-loop screening layer** that surfaces likely-missed diagnoses for a clinician to confirm — and they do this even on real EHR data, where they out-find diagnosis codes. They are **not** yet good enough to **adjudicate autonomously**: precision is low (they over-call), so a human must verify every flag. The binding constraint is **not reasoning** (already ≥ physicians on curated cases) but **precision, full-data access, calibration to real prevalence, and workflow integration.**

One line: **LLMs reliably *flag* diagnostic errors; they cannot yet *rule them in* on their own.** High recall, low precision, human-in-the-loop.

### Do-not-claim list
- ❌ "LLMs can autonomously diagnose from the EHR."
- ❌ "LLMs improve patient outcomes." (Korom was null on patient-reported outcomes; no RCT shows hard outcomes.)
- ❌ "Our detection generalizes." (Setting/population/model-specific.)
- ❌ "High accuracy" without specifying recall-vs-precision and curated-vs-real.
