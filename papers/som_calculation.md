# Andy — SOM Calculation

**Last updated:** 2026-05-24
**Companion docs:** `papers/sam_calculation.md` (US SAM = $156B); `papers/tam_calculation.md` (Global TAM ≈ $350B)

---

## Definition

**SOM** = the realistic dollars-of-customer-revenue Andy can capture in years 1, 3, and 5 given:
- Our GTM motion (CDI buyer + MA payer)
- Competitive density (SmarterDx, Reveleer, Datavant, Pareto, Episource)
- Hospital and payer sales cycles (12-24 months)
- Sales team size and ramp
- Realistic per-customer pricing

**Key distinction from SAM:** SAM measures the *damage pool* Andy could theoretically address. SOM measures the *Andy ARR* we can realistically book. These are linked but different — Andy captures only a fraction of damage averted as vendor revenue (15-30% via software fees or contingency).

---

## Methodology in plain English

For each customer segment (hospitals, MA plans), the formula is:

```
SOM = (# of customers acquired by year N)
    × (annual contract value per customer)
    × (renewal × expansion factor)
```

I build this bottom-up by:
1. Counting total addressable accounts in the US (hospital count + MA plan count).
2. Estimating realistic acquisition rate per year given sales team size.
3. Pricing per industry benchmarks (SmarterDx, Datavant, CDI vendor norms).
4. Triangulating against comparable healthcare-AI startups' historical trajectories.

---

## Addressable account base

| Segment | Total US accounts | Source |
|---|---|---|
| **Hospitals with ≥200 beds** | ~2,400 | AHA Hospital Statistics |
| **All US hospitals** | ~6,100 | AHA |
| **MA plans (parent organizations)** | ~700 (top 40 cover 80% of lives) | CMS / KFF |
| **ACO REACH entities** | ~480 | CMS |
| **Large physician groups (≥50 docs)** | ~3,500 | MGMA |

For SOM purposes, Andy's primary targets are:
- **Hospitals ≥200 beds:** ~2,400 (where CDI is mature, per #58 AHIMA 89.81% penetration and #60 Black Book 65% outsourcing)
- **MA plans:** top 40-50 plans covering ~80% of MA lives

---

## Per-customer ACV (annual contract value)

| Segment | ACV range | Source / basis |
|---|---|---|
| **Hospital pilot (year 1)** | $50-150K | Standard healthcare AI pilot pricing |
| **Hospital production deal** | $200-600K | Per-bed pricing ~$1-2K/bed × 200-500 beds; matches SmarterDx $200-250/discharge × avg 1,500 discharges/yr |
| **MA plan (per-member pricing)** | $1-5M | $0.05-0.15 per member per month × 500K-2M members per mid-sized plan |
| **Large MA plan (top-5)** | $10-30M | Per-member × 5-15M members |

Andy's blended ACV assumption: **~$300K avg hospital + ~$2.5M avg MA plan**.

---

## Year-by-year SOM build

### Year 1 (pilot phase)

| Customer type | # acquired | ACV | Y1 revenue |
|---|---|---|---|
| Hospital pilots | 5 | $100K | $0.5M |
| MA plan pilot | 1 | $500K | $0.5M |
| **Year 1 SOM** | 6 customers | | **~$1M ARR** |

Assumes a founding sales team of 1-2 reps + founder selling, with 6-9 month sales cycles.

### Year 3 (early expansion)

| Customer type | # accounts | ACV | Y3 revenue |
|---|---|---|---|
| Hospitals | 50 | $250K avg (mix of pilots + production) | $12.5M |
| MA plans | 8 | $1.5M avg | $12.0M |
| **Year 3 SOM** | 58 customers | | **~$25M ARR** |

Assumes Series A funded (~$15M raise), 8-10 person sales team, NRR ~120%.

### Year 5 (scale)

| Customer type | # accounts | ACV | Y5 revenue |
|---|---|---|---|
| Hospitals | 250 | $400K avg (production-heavy) | $100M |
| MA plans | 20 | $2.5M avg | $50M |
| **Year 5 SOM** | 270 customers | | **~$150M ARR** |

Assumes Series B + C raised (~$50M cumulative), 30+ person sales team, expansion into multi-product (DRG + HCC + dx error prevention).

### Year 7-10 (maturity ceiling)

If Andy reaches the trajectory of comparable companies (SmarterDx, Reveleer):
- ~10-15% of US hospitals + ~50% of MA covered lives
- $500M-1B ARR plausible 10-year ceiling
- Beyond Year 10, international expansion (matches Global TAM)

---

## SOM as % of SAM (sanity check)

| Year | SOM (ARR) | % of US SAM ($156B) | % of US SAM realistic ($27B) |
|---|---|---|---|
| Year 1 | $1M | 0.0006% | 0.004% |
| Year 3 | $25M | 0.016% | 0.09% |
| Year 5 | $150M | 0.10% | 0.56% |
| Year 10 | $1B | 0.64% | 3.7% |

These percentages are **tiny relative to SAM** — that's correct. SAM is the *damage pool* (multi-hundred-billion). Andy's vendor capture is a small slice of that pool. Even SmarterDx at $50M ARR is <0.05% of US SAM.

---

## Comparable healthcare AI / CDI company benchmarks

| Company | Founded | Current revenue estimate | Time to current scale |
|---|---|---|---|
| **SmarterDx** | 2020 | ~$50M ARR (2024 est) | 4 years |
| **Reveleer** | 2014 | $100-200M ARR (2024 est) | 10 years |
| **Datavant** | 2017 | $300-500M revenue (2024) | 7 years |
| **Pareto Intelligence** | 2018 | $50-100M ARR (est) | 6 years |
| **Episource** | 2008 | $200M+ (acquired by Optum 2024) | 16 years |

Andy's Year 5 SOM of **~$150M** would place it ahead of SmarterDx's Year 4 trajectory and competitive with Reveleer's Year 5 — realistic but aggressive.

---

## SOM range

| Posture | Year 5 SOM | What it assumes |
|---|---|---|
| **Bull case** | **$250M ARR** | Faster sales cycle, hospital network effects kick in, top-3 MA plan signed |
| **Realistic midpoint** | **$150M ARR** | Standard healthcare AI trajectory, matches SmarterDx + |
| **Conservative floor** | **$60M ARR** | Slow hospital sales, no large MA logo, 100 small/mid customers |

---

## Caveats

1. **SOM assumes funding milestones hit on schedule** — slip a Series B by 12 months and Year 5 SOM drops 30-50%.
2. **Per-customer ACV assumptions are based on industry benchmarks**, not Andy contracts. Once Andy has 5-10 paying customers, validate ACV against actuals.
3. **Hospital sales cycles are long (12-18 months)** — Year 1-2 are pilot/POC heavy. Real revenue ramp starts Year 3.
4. **MA plan deals are even longer (18-24 months)** — but ACVs are 5-10× larger per deal, so 2-3 anchor MA deals can transform the trajectory.
5. **Competitive risk:** if SmarterDx (or Optum, post-Episource acquisition) bundles a comparable product into existing contracts, Andy's hospital SOM compresses 30-50%.
6. **Regulatory risk:** CMS V28 HCC phase-in (2024-2026, per #50) reduces the HCC-capture incentive for MA plans, which could compress MA SOM by 10-20%.

---

## Final market hierarchy

| Layer | Value | Time horizon | Purpose |
|---|---|---|---|
| **TAM (Global)** | $350B/yr | Theoretical max | "Big picture" pitch |
| **SAM (US)** | $156B/yr | Theoretical max addressable | What we *could* serve |
| **SAM realistic** | $27B/yr | With 50% conversion attenuation | What's pragmatically capturable |
| **SOM Year 1** | $1M ARR | 12 months | Pilot-grade revenue |
| **SOM Year 3** | $25M ARR | 36 months | Series B-ready scale |
| **SOM Year 5** | $150M ARR | 60 months | Series C / pre-IPO scale |
| **SOM Year 10 ceiling** | ~$1B ARR | 10 years | Mature category leader |

---

## Headline for team

> **SOM (Year 5) ≈ $150M ARR** — realistic obtainable revenue assuming standard healthcare-AI trajectory (matches SmarterDx + at same age) with Series A → C funding on schedule.
>
> **Range:** $60M (conservative) — $150M (realistic) — $250M (bull).
>
> **10-year ceiling:** ~$1B ARR (~0.6% of US SAM) — would put Andy in the top tier of healthcare AI companies alongside Datavant and Reveleer.
>
> **Key levers that move SOM materially:**
> 1. Time to first large MA plan signing (each top-10 MA plan = +$10-30M ARR)
> 2. Hospital sales cycle compression (going from 18 → 9 months doubles Year 3 SOM)
> 3. Bundling additional modules (HCC + DRG + dx prevention) to push per-hospital ACV from $250K → $600K
