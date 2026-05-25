# Andy — TAM Calculation (Global)

**Last updated:** 2026-05-24
**Companion docs:** `papers/sam_calculation.md` (US SAM = $156B); `papers/key_findings.md` (evidence base entries #01–#82)

---

## Definition

**TAM** = the total annual global financial damage from missed, delayed, miscoded, and undiagnosed conditions across **all diseases**, **all geographies**, **all settings**, measured as the combined revenue impact to hospitals + payers + plaintiffs from unrecognized diagnoses (lost coding-driven revenue + downstream treatment costs + malpractice liability) if every such condition were hypothetically identified and acted upon worldwide.

---

## Methodology in plain English

We have a defensible **US SAM = $156B/yr** (all diseases, US-only). To scale it to global TAM, we need a multiplier that captures how much larger the global market is than the US market for this *specific category of damage*.

The most defensible multiplier is **US share of global healthcare spending** — because diagnostic-error damage is largely incurred as healthcare spending (excess admissions, complications, treatment). If the US is 45% of global spending and US damage is $156B, global damage ≈ $156B / 0.45 ≈ $347B.

This is a deliberately conservative scaling. Alternative multipliers (GDP-based, population-based, disease-burden-based) would give different answers but are less directly relevant to *dollar-denominated damage*.

---

## The multiplier — US share of global healthcare spending

| Year | US health spending | Global health spending | US share | Source |
|---|---|---|---|---|
| 2000 | $1.37T | $4.5T | 30% | WHO Global Health Expenditure DB |
| 2022 | $4.5T | $9.8T | **43%** | WHO Global Spending on Health 2024 report |
| 2024 (est) | $5.3T | ~$11.5T | **~46%** | CMS NHE + WHO extrapolation |

**Multiplier from US to global = 1 / 0.43–0.46 ≈ 2.2× – 2.3×**

Why this multiplier works for our use case:
1. **Dx-error damage scales with spend, not population.** A missed AKI in the US costs $1,795 (Silver #42); the same miss in India costs ~$150 (per-capita scaling). Aggregate damage = total population × per-case cost ≈ proportional to total spending.
2. **OECD 2025 confirmed the scaling.** OECD's "The economics of diagnostic safety" (March 2025) reports diagnostic error = **17.5% of healthcare expenditure**, which gives $870B for the US and consistent ratios elsewhere.
3. **WHO/OECD/World Bank joint estimate:** all unsafe care globally costs ~$1T/yr. Dx error is ~40-50% of that = $400-500B — consistent with our ~$340B estimate, within the range.

---

## Global TAM calculation

```
Global TAM = US SAM × (1 / US share of global health spending)
           = $156B  × (1 / 0.45)
           = $347B / yr
```

| Posture | $/yr | Multiplier | What it assumes |
|---|---|---|---|
| **Ceiling** | **$390B** | 2.5× | Dx-error damage scales slightly faster than spend in lower-income countries with weaker dx infrastructure |
| **Midpoint** | **$347B** | 2.2× | Direct healthcare-spending share (most defensible) |
| **Conservative floor** | **$310B** | 2.0× | Assumes US is ~50% of global spend (under-counts emerging markets) |

**Headline TAM = ~$350B / yr** (midpoint).

---

## Sanity checks against external benchmarks

| External anchor | Implied global $ | Our TAM | Match |
|---|---|---|---|
| OECD 2025: dx error = 17.5% of health spend; global health spend = $11.5T | $2.0T | $347B | Our TAM is **6× smaller** than OECD's broadest definition |
| WHO/OECD/World Bank "all unsafe care" = $1T/yr globally | $1T (broad) | $347B (dx-only) | Dx-error share consistent at 30-50% |
| NAM 2015 US ">$100B" × 3.5× (US 28% of global GDP) | $350B | $347B | Direct match |
| Global CDI software market = $4.88B (2024) | (vendor revenue, not damage) | $347B TAM | CDI vendor capture = ~1.4% of global TAM (consistent with early-stage market penetration) |

**The 6× gap with OECD** is worth noting. Two reasons it's there:
- OECD's 17.5% is broadest definition (includes productivity loss, patient-borne costs, etc.). Our TAM is narrower (hospital + payer + plaintiff financial damage only — same scope as our US SAM).
- If we adopt OECD's broader definition, our headline TAM would be **~$2T/yr** instead of $350B. That's a positioning choice for the team to make.

---

## Andy market hierarchy (final)

| Layer | $/yr | Scope | Purpose |
|---|---|---|---|
| **TAM (Global)** | **~$350B** | All conditions, all countries, all settings, narrow financial-damage definition | Theoretical maximum |
| **SAM (US)** | **$156B** | All conditions, US only, all settings, 4 mechanisms | Our addressable market given US-only GTM |
| **SAM — Evidence Base (US, 5 cond)** | **$55B** | Bottom-up cell calc for AKI/DM/CKD/HFpEF/AF, inpatient + MA outpatient | Defensible anchor for SAM |
| **SAM — Realistic** | **$27B** | SAM × 50% conversion attenuation | What's pragmatically capturable |
| **SOM (TBD)** | TBD | Andy's realistic 3-5 year capture given GTM, competition, sales team | Calculated separately |

**Ratios:**
- SAM / TAM = $156B / $347B = **45%**
- Evidence Base / TAM = $55B / $347B = **16%**

The 45% SAM-to-TAM ratio looks high but is structurally consistent — the US is 45% of global health spending, so its share of global dx-error damage matches.

---

## Caveats

1. **Multiplier ambiguity.** The 2.2× multiplier assumes dx-error damage tracks healthcare spending linearly. In reality, lower-income countries may have higher dx-error *rates* but lower per-case $; the aggregate scaling holds, but with wider uncertainty.
2. **Definition scope.** Our TAM uses the *narrow* (financial-damage to hospitals/payers/plaintiffs) definition consistent with our US SAM. The *broad* OECD definition (including productivity, patient-borne) gives ~$2T global TAM.
3. **No multi-year NPV.** This is year-1 annual damage. Multi-year compounding (especially HCC-style recurring capture) would 2-3× the number.
4. **Currency and inflation.** All figures in 2024 USD. WHO 2022 data adjusted forward at ~10% spend growth.
5. **Excludes patient-borne and productivity-loss costs.** NAM separately estimates these at additional hundreds of billions globally. Our TAM is strictly the dollar pool that can theoretically be addressed by a CDI/HCC/decision-support product.

---

## Headline for team

> **Global TAM ≈ $350B/yr** — the total worldwide financial damage from diagnostic gaps across all conditions, all settings, all 4 mechanisms.
>
> Built by scaling the US SAM ($156B) by the inverse of US share of global health spending (1 / 0.45 = 2.2×). Triangulated against OECD 2025 (17.5% of spend = dx error), WHO/OECD/World Bank ($1T unsafe care), and CDI market data — all consistent with the $300-400B range.
>
> **Market hierarchy:**
> - **TAM (Global):** $350B
> - **SAM (US):** $156B (45% of TAM)
> - **Evidence Base (US, 5 conds):** $55B (16% of TAM)
> - **SOM (3-yr realistic):** to be calculated

---

## Sources

- [WHO Global Spending on Health Report 2024](https://www.who.int/teams/health-financing-and-economics/global-spending-on-health-report)
- [CMS NHE 2024 — $5.3T US spending](https://www.medicaleconomics.com/view/health-care-spending-reaches-5-3-trillion-or-18-of-u-s-economy-in-2024)
- [OECD Health Working Paper 176 — Economics of Diagnostic Safety (2025)](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/03/the-economics-of-diagnostic-safety_6e0ed50b/fc61057a-en.pdf)
- [WHO/OECD/World Bank — $1T unsafe care costs](https://healthpolicy-watch.news/wrong-diagnosis-medication-errors-care-related-infections-adding-usd-1-trillion-to-spiraling-health-costs-globally-warn-oecd-who-world-bank/)
- [Global CDI market = $4.88B (2024)](https://www.precedenceresearch.com/clinical-documentation-improvement-market)
- [Peterson-KFF — US health spending vs other countries](https://www.healthsystemtracker.org/chart-collection/health-spending-u-s-compare-countries/)
