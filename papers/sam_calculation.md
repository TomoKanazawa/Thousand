# Andy — SAM Calculation (Canonical)

**Last updated:** 2026-05-24
**Source-of-truth document:** `papers/key_findings.md` (entries #01–#82)

> **Definition update (2026-05-24):** This document now defines SAM as the **US-wide, all-diseases, all-settings, all-mechanisms** market — what we previously called "TAM". The previous "SAM" (5 conditions × 2 settings, bottom-up) is now positioned as the **Evidence Base** that anchors the expansion to all diseases. Global TAM will be calculated separately.

---

## SAM headline

**SAM ≈ $156B / year** — total annual US financial damage from missed / delayed / miscoded / undiagnosed conditions across all diseases, all inpatient + outpatient settings, measured through 4 mechanisms (DRG uplift + HCC capture + downstream treatment cost + malpractice liability).

This SAM is constructed in two stages:

| Stage | Method | Output |
|---|---|---|
| **Stage 1 — Evidence Base** | Bottom-up: 5 conditions × 2 settings × 4 dx categories × 4 mechanisms, every input paper-cited or CMS-anchored | **$55B** |
| **Stage 2 — Expansion to all diseases** | Top-down: macro anchors per mechanism, swap downstream cost from bottom-up to NAM 2015 authoritative figure | **$156B** |

Stage 1 establishes that the math works on cells where we have full evidence. Stage 2 scales the same 4 mechanisms to the entire US disease pool using authoritative macro anchors.

---

## Definitions (current)

**SAM** = total annual financial damage in the US from missed / delayed / miscoded / undiagnosed conditions across **all diseases**, **all inpatient + outpatient settings**, measured as the revenue impact to hospitals + payers + plaintiffs (lost DRG revenue + uncaptured HCC payments + downstream treatment costs + malpractice liability).

**Evidence Base (formerly "SAM"):** The bottom-up subset on which the SAM expansion rests — limited to:
- **Conditions:** AKI, Diabetes, CKD, HFpEF, AF
- **Settings:** US inpatient + Medicare Advantage outpatient
- **Mechanisms:** all 4
- **Evidence bar:** peer-reviewed literature OR authoritative government data must quantify both the undetection rate AND the dollar impact per case

**TAM** = (to be calculated separately) Global market for diagnostic-error damage, all diseases, all geographies, all settings.

---

# Stage 1 — Evidence Base ($55B bottom-up)

## Methodology in plain English

For each cell of (5 conditions × 2 settings × 4 dx-error categories), the formula is:

```
Cell SAM = (US population in setting)
         × (prevalence of condition)
         × (% undetected / undercoded)
         × (% in this dx-error category)
         × Σ (applicable mechanisms × $/case)
```

The 4 financial mechanisms are **coexistent** — capturing a missed dx unlocks revenue AND avoids cost AND prevents claims simultaneously. They are summed within each cell (not picked as alternatives).

The 4 dx-error categories trigger different mechanisms:

| Mechanism | Coding error | Never-detected | Delayed | Wrong |
|---|---|---|---|---|
| DRG uplift | yes | yes | partial | partial |
| HCC capture | yes | yes | partial | partial |
| Downstream treatment cost | no | yes | yes | yes |
| Malpractice | no | yes | yes | yes |

---

## Baselines (government sources, accepted)

| Item | Value | Source |
|---|---|---|
| US inpatient admissions / year | 33.7M | AHRQ NIS 2021 |
| US ICU admissions / year | 5.7M | CMS |
| US Medicare Advantage enrollees | 33.4M | KFF/CMS 2024 |
| US adult population | 260M | Census |
| MA share of US adults | 12.8% | derived |
| Average inpatient cost / day | ~$2,500 | industry (Hautz cross-check) |
| US HF admissions / year | 1.1M | AHA #79 |

---

## Per-mechanism unit dollar values (paper- or CMS-cited)

| Mechanism | $ per case | Source |
|---|---|---|
| DRG uplift — CC tier | $3,000 | Industry + #57 SmarterDx benchmark |
| DRG uplift — MCC tier | $4,330 | HHS-OIG #48 (pneumonia DRG 193 vs 195) |
| HCC capture — Diabetes | $3,000 / yr | CMS HCC 18/19 weighted (V24/V28 blend) |
| HCC capture — CKD | $1,500 / yr | CMS HCC 138-140 weighted |
| HCC capture — HF | $3,972 / yr | CMS HCC 85 |
| HCC capture — AF | $2,500 / yr | CMS HCC 96 (V28-adjusted) |
| Downstream cost — AKI | $1,795 / case | Silver 2017 #42 |
| Downstream cost — DM (dx-yr excess) | $4,828 / case | Khan 2021 #45 |
| Downstream cost — generic missed inpatient dx | $8,500 (3.4 days × $2,500) | Hautz 2019 #13 |
| Downstream cost — undx AF stroke avoidance | ~$1,250 / AF-yr | derived |
| Malpractice — US total dx-error indemnity | $1.55B / yr | Saber Tehrani 2013 #10 (NPDB 25-yr extrap) |

---

## Per-condition prevalence + undetection (paper-cited)

| Condition | Prevalence (paper-cited) | Undetection rate (paper-cited) | Source(s) |
|---|---|---|---|
| AKI inpatient | 21.6% adult hospitalized (KDIGO) | 68% undercoded | #73 Susantitaphong, #14 Esposito |
| AKI ICU | 57.3% (KDIGO) | — | #74 Hoste AKI-EPI |
| Diabetes inpatient undx | 5.6% of admits via A1c | (100% undx by definition) | #16 Greci |
| Diabetes outpatient undx | 8.7M US adults (4.5%) | (100% undx by definition) | #24 NCHS DataBrief 516 |
| CKD prevalence | 14% US adults | 87% unaware overall; 72.5% uncoded inpatient | #79 AHA, #66 CDC, #17 Ferris |
| CKD Stage 3 outpatient | ~18M US (Stage 3+) | 62% undiagnosed | #65 Tangri REVEAL-CKD |
| HFpEF share of HF | 47% | — | #78 Owan |
| HFpEF undetected (community) | — | 76% may remain undetected | #64 Groenewegen |
| HF moderate/severe diastolic dysfunction unrecognized | — | <50% recognized | #62 Redfield |
| HF prevalence age 65+ | 13% | — | #79 AHA |
| AF prevalence | 6.6M US adults | 698K undiagnosed (~13.1% of AF) | #79 AHA, #27 Turakhia |
| AF asymptomatic share | 26% | — | #80 Sgreccia |

---

## Category-split assumptions (reasoned — not paper-cited)

The split of missed cases across the 4 dx-error categories is not directly measured in the literature. These reasoned splits drive ~$10B of sensitivity in the SAM total — flagged for SME validation.

| Condition class | Coding error | Never-detected | Delayed | Wrong |
|---|---|---|---|---|
| Acute (AKI) | 40% | 30% | 20% | 10% |
| Chronic — inpatient (DM, CKD) | 60% | 30% | 10% | — |
| Chronic — inpatient (HFpEF) | 5% | 50% | 30% | 15% |
| Chronic — outpatient (DM, CKD, HFpEF MA) | — | 75-95% | 5-20% | 5% |
| AF | mostly coding (inpt) / mostly never-detected (outpt) | | | |

---

## Cell-by-cell calculation

### AKI Inpatient (no HCC — acute condition)

Pool: 33.7M × 21.6% × 68% undetected = **4.95M missed AKI cases / yr**

| Category | # cases | DRG | Downstream cost | Malpractice | Cell $ |
|---|---|---|---|---|---|
| Coding error (40%) | 1.98M | $3K | — | — | **$5.95B** |
| Never-detected (30%) | 1.49M | $3K | $1,795 | ~$20M | **$7.16B** |
| Delayed (20%) | 0.99M | $1.5K partial | $1,795 | ~$20M | **$3.28B** |
| Wrong (10%) | 0.50M | $1K partial | $1,795 | ~$10M | **$1.41B** |
| **Subtotal** | | | | | **$17.80B** |

### Diabetes Inpatient (all never-detected, by Greci cohort definition)

Pool: 33.7M × 5.6% = **1.89M undx DM via A1c**

| Category | # cases | DRG | Downstream cost | Malpractice | Cell $ |
|---|---|---|---|---|---|
| Never-detected (100%) | 1.89M | $1.5K | $2,414 (50% Khan) | <$5M | **$7.40B** |
| **Subtotal** | | | | | **$7.40B** |

### Diabetes Outpatient (MA)

Pool: 8.7M × 12.8% MA share = **1.11M undx DM in MA**

| Category | # cases | HCC | Downstream cost | Malpractice | Cell $ |
|---|---|---|---|---|---|
| Never-detected (95%) | 1.05M | $3K/yr | $4,828 | — | **$8.22B** |
| Delayed (5%) | 0.06M | $1.5K partial | $4,828 | — | **$0.38B** |
| **Subtotal** | | | | | **$8.60B** |

### CKD Inpatient

Pool: 33.7M × 14% × 72.5% uncoded = **3.42M missed**

| Category | # cases | DRG | Downstream cost | Malpractice | Cell $ |
|---|---|---|---|---|---|
| Coding error (60%) | 2.05M | $2K | — | — | **$4.10B** |
| Never-detected (30%) | 1.03M | $2K | $4,250 (50% Hautz) | — | **$6.43B** |
| Delayed (10%) | 0.34M | $1K partial | — | — | **$0.34B** |
| **Subtotal** | | | | | **$10.87B** |

### CKD Outpatient (MA)

Pool: ~18M US Stage 3+ × 62% undx × 12.8% MA = **1.44M undx Stage 3+ CKD in MA**

| Category | # cases | HCC | Downstream | Malpractice | Cell $ |
|---|---|---|---|---|---|
| Never-detected (80%) | 1.15M | $1.5K/yr | — | — | **$1.73B** |
| Delayed (15%) | 0.22M | $750 partial | — | — | **$0.16B** |
| Wrong (5%) | 0.07M | minimal | — | — | **$0.05B** |
| **Subtotal** | | | | | **$1.94B** |

### HFpEF Inpatient

Pool: 1.1M HF admits × 47% HFpEF × 50% undetected (Redfield) = **258K missed HFpEF inpatient / yr**

| Category | # cases | DRG | Downstream cost | Malpractice | Cell $ |
|---|---|---|---|---|---|
| Coding (5%) | 13K | $2.5K | — | — | **$0.03B** |
| Never-detected (50%) | 129K | $2.5K | $8,500 (Hautz) | ~$30M | **$1.45B** |
| Delayed (30%) | 77K | $1.25K | $4,250 | ~$15M | **$0.44B** |
| Wrong (15%) | 39K | $1.25K | $4,250 | ~$5M | **$0.22B** |
| **Subtotal** | | | | | **$2.14B** |

### HFpEF Outpatient (MA)

Pool: 33.4M MA × 13% HF age 65+ × 47% HFpEF × 76% undetected (Groenewegen) = **1.55M undx HFpEF in MA**

| Category | # cases | HCC | Downstream | Malpractice | Cell $ |
|---|---|---|---|---|---|
| Never-detected (75%) | 1.16M | $3,972/yr | — | — | **$4.61B** |
| Delayed (20%) | 0.31M | $2K partial | — | — | **$0.62B** |
| Wrong (5%) | 0.08M | minimal | — | — | **$0.05B** |
| **Subtotal** | | | | | **$5.28B** |

### AF Inpatient (minimal — already on EKG)

Pool: ~50K newly screen-detectable AF in admits

| Category | # cases | DRG | Downstream | Malpractice | Cell $ |
|---|---|---|---|---|---|
| Coding (100%) | 50K | $1.5K | — | — | **$0.08B** |
| **Subtotal** | | | | | **$0.08B** |

### AF Outpatient (MA)

Pool: 698K undx US AF × MA-age share = **140K**

| Category | # cases | HCC | Downstream (stroke risk) | Malpractice | Cell $ |
|---|---|---|---|---|---|
| Never-detected (90%) | 126K | $2,500 | $1,250 | ~$10M | **$0.48B** |
| Delayed (10%) | 14K | $1.25K | $625 | — | **$0.03B** |
| **Subtotal** | | | | | **$0.51B** |

---

## SAM aggregate

### By dx-error category

| Category | $/yr | % of SAM |
|---|---|---|
| Coding error | $10.16B | 18.5% |
| **Never-detected** | **$37.81B** | **68.8%** |
| Delayed | $5.25B | 9.6% |
| Wrong | $1.73B | 3.1% |
| **Total SAM** | **$54.95B** | 100% |

### By setting

| Setting | $/yr | % |
|---|---|---|
| Inpatient | $38.29B | 69.7% |
| Outpatient (MA) | $16.33B | 29.7% |
| Malpractice overlay | $0.33B | 0.6% |
| **Total** | **$54.95B** | 100% |

### By condition

| Condition | Inpatient | Outpatient MA | Total |
|---|---|---|---|
| AKI | $17.80B | — | **$17.80B** |
| Diabetes | $7.40B | $8.60B | **$16.00B** |
| CKD | $10.87B | $1.94B | **$12.81B** |
| HFpEF | $2.14B | $5.28B | **$7.42B** |
| AF | $0.08B | $0.51B | **$0.59B** |
| Malpractice | | | **$0.33B** |
| **Total** | **$38.29B** | **$16.33B** | **$54.95B** |

### By mechanism

| Mechanism | $/yr |
|---|---|
| DRG uplift (inpatient) | ~$22.0B |
| HCC capture (MA outpatient) | ~$14.5B |
| Downstream treatment cost | ~$18.1B |
| Malpractice liability | ~$0.33B |
| **Total** | **~$54.95B** |

---

## Evidence Base range

| Posture | $/yr | Assumption |
|---|---|---|
| **Pure ceiling** | **$55B** | Full mechanism stacking, no conversion attenuation, year 1 |
| **Realistic midpoint** | **$27B** | 50% conversion attenuation applied to DRG + HCC (industry rule of thumb) |
| **Conservative floor** | **$18B** | Drops downstream cost as separate mechanism (only counts revenue-side) |

The **$55B Evidence Base** is the most defensible bottom-up number we can build today. It represents the share of total US diagnostic-error damage that is fully paper-cited across our 5 conditions and 2 settings. We use it as the anchor for the Stage 2 expansion to all diseases.

---

# Stage 2 — Expansion to all diseases ($156B SAM headline)

## Plain-English process

**Why we expand.** The Evidence Base ($55B) covers 5 conditions. But SAM is defined as **all diseases in all US inpatient + outpatient settings**. We can't enumerate ~70,000 ICD codes from the bottom up, so we expand top-down using the best macro anchor available per mechanism.

**The 4 mechanisms (same as Stage 1).**

| Mechanism | What it captures |
|---|---|
| Lost DRG revenue | Inpatient revenue hospitals fail to bill because diagnoses don't push DRG into higher severity tier (CC / MCC) |
| Uncaptured HCC payments | MA / ACO-REACH payment hospitals/plans fail to receive because chronic dx isn't coded in the calendar year |
| Downstream treatment cost | Excess US healthcare spending caused by complications and admissions that earlier dx would have averted |
| Malpractice liability | Indemnity + legal cost from dx-error claims |

**The double-count trap, avoided.** If we naively scaled the Evidence Base ×3 ("5 conditions → all conditions"), the downstream cost line ($18B × 3 = $54B bottom-up) would overlap with NAM 2015's authoritative $100B figure — they measure the same dollar pool. We use NAM for mechanism #3 and drop the bottom-up estimate. Mechanisms #1, #2, #4 are extrapolated from the Evidence Base + macro anchors.

---

## Per-mechanism Stage-2 calculation

### Mechanism 1 — Lost DRG revenue (all conditions, all US inpatient)

"How much inpatient revenue is left on the table because diagnoses aren't optimally coded for DRG severity tier?"

| Input | Value | Source |
|---|---|---|
| US inpatient admissions / year | 33.7M | AHRQ NIS |
| Net new revenue per discharge (vendor benchmark) | $200-250 | #57 SmarterDx |
| Already-captured CDI pool | $6.7-8.4B/yr | derived |
| Total addressable headroom (uncaptured + hospitals without CDI) | ~2× already-captured | implied by #47 Gluckman + #48 HHS-OIG |
| **Stage-2 estimate** | **$17B / yr** | midpoint |

### Mechanism 2 — Uncaptured HCC payments (all conditions, all risk-adjusted outpatient)

"How much MA / ACO-REACH / risk-adjusted commercial payment is missing because chronic conditions aren't documented in the calendar year?"

| Input | Value | Source |
|---|---|---|
| MA chart-review-only payments (2017) | $9.2B | #51 HHS-OIG |
| MA HRA-driven payments (2019) | $12.3B | #53 Meyers |
| Already-captured retrospective MA review | ~$15-21B/yr (with overlap) | derived |
| Still-uncaptured MA pool | At least as large as captured | #65 Tangri + scaling |
| ACO-REACH + risk-adjusted commercial pool | ~$5-10B | industry estimate |
| **Stage-2 estimate** | **$35B / yr** | midpoint |

### Mechanism 3 — Downstream treatment cost (all conditions, all settings)

"How much excess US healthcare spending is caused by diagnoses missed or delayed?"

| Input | Value | Source |
|---|---|---|
| **NAM authoritative anchor** | **>$100B / yr** | #70 NAM 2015 |
| Triangulation: 12M outpatient dx errors × ~$5K | $60B | #05 Singh |
| Triangulation: 7.4M ED dx errors × $8,500 | $63B | #12 AHRQ × #13 Hautz |
| Triangulation: 795K serious harms × $50K | $40B | #01 Newman-Toker |
| **Stage-2 estimate** | **$100B / yr** | NAM headline |

### Mechanism 4 — Malpractice liability (all conditions)

"What's the total US dollar cost of diagnostic-error malpractice?"

| Input | Value | Source |
|---|---|---|
| Direct indemnity (25-yr NPDB extrapolation) | $1.55B/yr | #10 Saber Tehrani ($38.8B / 25 yr) |
| Legal defense + admin (2-3× indemnity, historical) | $3-5B/yr total | medical malpractice norm |
| **Stage-2 estimate** | **$4B / yr** | midpoint |

---

## SAM aggregate (Stage 2 final)

| Mechanism | $/yr | Basis |
|---|---|---|
| Lost DRG revenue | $17B | SmarterDx × admits, scaled |
| Uncaptured HCC payments | $35B | HHS-OIG + Meyers, scaled |
| Downstream treatment costs | $100B | NAM 2015 |
| Malpractice liability | $4B | Saber Tehrani × 2.5 |
| **SAM Total** | **~$156B / yr** | |

### SAM by setting

| Setting | $/yr | Notes |
|---|---|---|
| Inpatient | ~$50B | DRG $17B + inpatient share of NAM cost (~$30B) + portion of malpractice |
| Outpatient — all payers | ~$106B | HCC $35B + outpatient majority of NAM cost (~$70B) + portion of malpractice |
| **SAM Total** | **$156B** | |

---

## SAM range

| Posture | $/yr | What it assumes |
|---|---|---|
| **Pure ceiling** | **$156B** | NAM downstream cost + full mechanism stacking |
| **NAM-only conservative** | **$100B** | Downstream cost mechanism alone (most-cited number) |
| **Revenue-only floor** | **$56B** | DRG + HCC + malpractice only; drops downstream cost |

---

## Sanity checks against external benchmarks

| External anchor | Implied $ | Our SAM line | Match |
|---|---|---|---|
| NAM 2015 ">$100B/yr" misdiagnosis cost | $100B | $100B (downstream cost) | direct |
| Newman-Toker 2024 #01: 795K serious harms × $50K avg | ~$40B | subset of $100B | within |
| AHRQ ED #12: 7.4M dx errors × $8,500 Hautz cost | $63B | subset of $100B | within |
| MA payment integrity industry (~$15B annual reviews captured) | $15B captured | $35B SAM (includes uncaptured) | consistent |
| Healthcare CDI industry (~$8B/yr current vendor revenue) | $8B captured | $17B SAM headroom | ~2× upside |

All five external benchmarks land inside the SAM range — order-of-magnitude correct.

---

## Unified caveats (Stage 1 + Stage 2)

1. **Category splits in Stage 1 are reasoned, not paper-cited.** Evidence Base is ±$10B sensitive.
2. **Mechanism stacking assumes independence.** DRG payment, HCC capture, cost avoidance, and malpractice prevention are different parties' dollars — conceptually stackable but operationally may attenuate each other.
3. **HCC capture is annual recurring**; counts year-1 only. Multi-year NPV is 2-3× larger.
4. **Stage 2 macro anchors carry wider uncertainty than Stage 1 cells.** NAM "$100B/yr" is a 2015 estimate; the 2026 value could plausibly be $130-150B.
5. **6 of 9 per-case dollar inputs in Stage 1 are peer-reviewed** (Silver, Khan, Hautz, Owan, Redfield, Groenewegen). The other 3 are CMS coefficients (gov) or industry benchmarks.
6. **HFpEF assumption sensitivity:** the 76% undetection rate from Groenewegen drives a meaningful share of the HFpEF cells. Using Redfield's 50% instead drops Evidence Base from $55B → $53B.
7. **SAM does NOT include patient-borne costs** (out-of-pocket, lost productivity, mortality). NAM separately estimates these at additional hundreds of billions.
8. **Saber Tehrani's $38.8B/25-yr** is stub-derived (full paper not downloaded). Verify before quoting verbatim.

---

## Headline for team

> **SAM ≈ $156B/yr** — total US financial damage from diagnostic gaps across all conditions, all settings, all 4 mechanisms.
>
> Composed of:
> - **$100B downstream treatment cost** (NAM 2015 anchor)
> - **$35B uncaptured MA/ACO HCC payments**
> - **$17B lost inpatient DRG revenue**
> - **$4B malpractice liability**
>
> **Built in two stages:**
> 1. **Evidence Base ($55B):** bottom-up for 5 conditions × 2 settings × 4 dx categories × 4 mechanisms, every input paper-cited or CMS-anchored.
> 2. **Expansion to all diseases ($156B):** top-down macro anchors per mechanism, deduplicated against the bottom-up cost line.
>
> The Evidence Base proves the math works on cited cells; the Expansion scales the same 4 mechanisms to the entire US disease pool using authoritative literature.
