# 06b — Marks 2026 (Haimovich co-senior) — JAMA Network Open published version

> Peer-reviewed JAMA Network Open version of what we had as Haimovich's medRxiv
> preprint (`06_Haimovich2025_etrigger-LLM.pdf`). Substantially evolved — different
> first author, more models, AUC now reported, 5 reviewers, multiple LLMs. Treat
> this as the **current state** of the work, not the preprint.

## Citation
Marks CM, Gibney S, Stenson B, Sarma D, Gaudet C, Mombini H, Buckley TA, Keko M, Nathanson LA, Burke LG, Shapiro NI, Burstein JL, Grossman SA, Parab A, Janke AT, Manrai AK, Taylor RA, Rosen CL, **Rodman A**, **Haimovich AD**. *Screening for Missed Opportunities for Diagnosis in the ED Using eTriggers and Large Language Models.* **JAMA Netw Open.** 2026;9(6):e2620939. doi:10.1001/jamanetworkopen.2026.20939. Published June 29, 2026.

- **First author:** Clifford M. Marks, MD, MBA (Georgetown EM)
- **Co-senior authors:** Adam Rodman, MD, MPH (BIDMC Internal Medicine) + Adrian D. Haimovich, MD, PhD
- **Corresponding:** Adrian Haimovich — `adrian.haimovich@yale.edu` *(new affiliation — Yale, not BIDMC as in preprint)*
- **Open access (CC-BY).** TRIPOD-LLM reporting guideline followed.
- **Code:** "available on request" (no GitHub link).

## Design (one paragraph)
Retrospective diagnostic study, **2 ED eTrigger cohorts** within Beth Israel Lahey Health enterprise (**9 hospitals: 1 academic + 7 community**), Apr 2015 – Mar 2025. Two cohorts:

1. **72-hour return cohort:** ED discharge with return hospital admission within 72h. N = **191 analyzed**, stratified between academic medical center (BIDMC) and network sites.
2. **Floor-to-ICU cohort:** ED admission to floor with escalation to ICU within 24h of inpatient admission. N = **97 analyzed**. Limited to 2024+ due to EHR coding reliability.

Total analyzed: **288 encounters** (300 sampled, 12 excluded for duplication/miscoding).

## Physician adjudication (gold standard)
- **5 emergency physicians** (Marks, Stenson, Sarma, Buckley, Gaudet) independently reviewed every case (up from 2 reviewers in the preprint — large methodological strengthening).
- Question: *"was there a missed opportunity to make a correct or timely diagnosis based on the available evidence, regardless of harm?"*
- **Safer Dx instrument** used as a rubric for case-level adjudication, NOT as a numeric score with a prespecified cutoff.
- Disagreements adjudicated to a final label; persistent disagreements resolved by Haimovich (6th reviewer).
- Reviewers had access to ED + subsequent hospitalization records, no restrictions on review content.
- **Inter-rater agreement: 81.9% (95% CI 77.4–86.1%), Gwet's AC1 = 0.77 (0.70–0.83).**

## LLMs evaluated (six models — major change from preprint)
- **Claude Sonnet 4** (Anthropic, via AWS Bedrock — PHI-compliant)
- **Claude Sonnet 4.6** (Anthropic)
- **Claude Opus 4.6** (Anthropic)
- **Gemini 3 Pro** (Google DeepMind)
- **GPT-5** (OpenAI)
- **GPT-5 mini** (OpenAI)

Single locked prompt across all models. Last date of use: March 2026. Single-run inference. Each model returned structured JSON: **binary MOD classification (yes/no), probability estimate 0–100%, and free-text rationale.** Binary used for sensitivity/specificity/PPV/NPV; probability used for AUC.

## Headline results

### 72-h return cohort (n = 191, 21 MODs, PPV trigger = 11.0%)

| Model | Sens | Spec | PPV | NPV | AUC |
|---|---|---|---|---|---|
| **Claude Sonnet 4** | **85.7** (65.4–95.0) | 55.9 (48.4–63.1) | 19.4 | 96.9 | **0.73** (0.61–0.85) |
| Claude Sonnet 4.6 | 71.4 | 57.6 | 17.2 | 94.2 | 0.68 |
| Claude Opus 4.6 | 47.6 | 79.4 | 22.2 | 92.5 | 0.69 |
| Gemini 3 Pro | 61.9 | 69.4 | 20.0 | 93.7 | 0.70 |
| GPT-5 | 57.1 | 66.5 | 17.4 | 92.6 | 0.66 |
| **GPT-5 mini** | 42.9 | **82.9** (76.6–87.9) | 23.7 | 92.2 | 0.65 (0.53–0.77) |

### Floor-to-ICU cohort (n = 97, 18 MODs, PPV trigger = 18.6%)

| Model | Sens | Spec | PPV | NPV | AUC |
|---|---|---|---|---|---|
| Claude Sonnet 4 | **55.6** | 64.6 | 26.3 | 86.4 | 0.61 |
| Claude Sonnet 4.6 | 22.2 | 86.1 | 26.7 | 82.9 | 0.65 |
| Claude Opus 4.6 | 22.2 | 87.3 | 28.6 | 83.1 | 0.68 |
| Gemini 3 Pro | 22.2 | 93.7 | 44.4 | 84.1 | 0.69 |
| **GPT-5** | 33.3 | 93.7 | **54.5** | 86.0 | **0.82** (0.73–0.91) |
| GPT-5 mini | 5.6 | 97.5 | 33.3 | 81.9 | 0.57 |

### Time-savings analysis (operating threshold tuned to maintain ≥80% sensitivity)
- **72-h cohort, Claude Sonnet 4:** screens out 99/191 cases (51.8%) → ~8.2-hour time savings (assuming 5 min/case).
- **Floor-to-ICU cohort, GPT-5:** screens out 43/97 cases (44.3%) → ~3.6-hour time savings.
- Overall: 24h → 12.2h single-physician review, **11.8h total savings while maintaining >80% sensitivity.**

### Reviewer-model concordance (secondary analysis)
- Physician-to-physician agreement (5 reviewers, 4 reviewer pairs): 76.6%–92.6%.
- Mean reviewer-model Gwet's AC1 was computed per model; **GPT-5 mini had highest reviewer-model concordance**, Claude Sonnet 4 had lowest.
- Key insight: **discrimination (AUC) and concordance are distinct model properties** — a model can have high AUC but low physician-like concordance.

## Headline findings (verbatim from abstract)
- Across cohorts, **LLMs showed broadly similar discrimination (AUC) but very different binary thresholds** — Claude Sonnet 4 favored sensitivity, GPT-5 mini favored specificity.
- "Similar model AUCs did not translate to similar binary case determinations; similar threshold-related behavior has been observed in real-world ED note evaluations, where LLMs tended to make overly cautious recommendations with relatively high sensitivity at the expense of specificity."

## Conclusions (verbatim)
> *"Model performance varied by cohort, with LLMs showing similar discrimination but different binary thresholds. These findings suggest that evaluation within the review workflow is needed before implementation and that reviewer-like concordance captures a distinct dimension of model behavior from discrimination."*

## Limitations
1. Single health system (Beth Israel Lahey) → generalizability constraint.
2. **Single locked prompt** with no model-specific tuning — relative performance could change with prompt optimization.
3. Reviewers may have considered EHR content not in model input → adjudication-vs-model asymmetry.
4. Temporal bias: most 72-h return network stratum cases were pre-2024.
5. **Binary MOD adjudication only** — no severity, harm, or error-subtype evaluation.
6. Only 5 reviewers — concordance analysis is exploratory.

## What changed vs. preprint (significant)

| | medRxiv preprint (06_…) | JAMA Network Open (06b_…) |
|---|---|---|
| First author | Haimovich | **Marks** |
| Co-senior authors | (just Haimovich) | **Rodman + Haimovich** |
| N analyzed | 317–357 across 3 cohorts | 288 across 2 cohorts |
| eTriggers | 3 established + 1 novel (ECSC) | 2 established (ECSC dropped) |
| Models | Claude Sonnet 4 only | **6 LLMs across 3 vendors** |
| Reviewers | 2 ED physicians | **5 ED physicians** |
| AUC reported? | No (binary only) | **Yes (primary outcome)** |
| Reporting std | (none stated) | **TRIPOD-LLM** |
| Haimovich affiliation | BIDMC | **Yale** (corresponding author email) |

## Why this matters for our work

### Methodological precedent (now stronger)
- **TRIPOD-LLM compliance** — the gold-standard reporting bar; we should match it.
- **5-reviewer adjudication** raises the bar from 2-reviewer Safer Dx; gold-standard credibility just went up.
- **6-model evaluation** sets the new norm — comparing multiple frontier models is now expected, not optional.

### Critical methodological insight for our paper
> **"AUCs were broadly similar across models, yet binary thresholds varied substantially."**

This is the actual headline finding and it's a *deep* methodological point. It means:
- Reporting AUC alone hides the operating-point story.
- Different models with same AUC produce wildly different clinical workflows.
- **Threshold calibration is its own deployment problem, separate from model selection.**

We should adopt this dual-reporting (AUC + threshold-tuned PPV at fixed sensitivity) as standard. Haimovich/Rodman will respect us reporting it; they won't if we don't.

### Operating-point lesson for our wedge
- **Best AUC ≠ best deployment.** Claude Sonnet 4 had top sensitivity (85.7%) in 72h cohort but only AUC 0.73; GPT-5 mini had similar AUC (0.65) with totally different threshold behavior.
- For our missed-dx product, **the choice of model and threshold is *the* product decision**, not a separate calibration step.

### Adam Rodman is now a co-senior author
- Rodman = Cabral 2024 (R-IDEA), JAMA Internal Medicine; major clinical-AI reasoning researcher at BIDMC.
- He's now formally tied to Haimovich's work. **Boston cluster (BIDMC) just got tighter** — Rodman, Haimovich, possibly Dalal (Brigham, nearby).
- Implication: a warm intro to Rodman via Haimovich is now natural — *"now that you've published with Adam, would he be open to a methods conversation about our work?"* Rodman holds equity in a clinical-AI startup (Google visiting researcher; possibly others — disclosed in paper as "personal fees from Google").

### Haimovich → Yale
- Corresponding author affiliation **moved to Yale** between preprint (BIDMC) and publication.
- His direct email is now `adrian.haimovich@yale.edu`. Worth updating any contact references.
- He may be in transition — possibly recruited away or splitting time. Either way, the BIDMC + Yale dual identity is useful (two warm-intro hubs).

## Open questions worth raising on a call
1. **Why binary-only for primary?** They had probability outputs but only used them for AUC. Did they consider tuning a threshold on probability?
2. **Why drop the ECSC trigger?** The preprint's novel hybrid trigger (Emergency Care Sensitive Conditions) is gone from the published version.
3. **Single prompt across all 6 models** — they acknowledge this as a limitation. Did they consider per-model prompt tuning?
4. **What did the 5 reviewers actually disagree on?** The 81.9% agreement is high but the disagreement pattern probably reveals where LLMs and humans diverge most.

## Sources
- DOI: 10.1001/jamanetworkopen.2026.20939
- Acknowledgment of Source: pages 1–11 of the JAMA Netw Open published article, June 29, 2026 (read via shared screenshots, not stored locally).
- Conflict of Interest disclosures: Stenson (Accurine grants), Burke (AHRQ/ABMS/VA grants), Taylor (Beckman Coulter, VeraHealth stock options), **Rodman (personal fees from Google as visiting researcher)**, Haimovich (personal fees from MBO Partners). No other disclosures.
