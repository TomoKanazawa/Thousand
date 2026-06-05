# LLM Performance on Diagnosis & Diagnostic-Error Detection — Literature

Evidence base for "what current LLMs can and can't do on diagnosis," to ground
our positioning and the Haimovich collaboration.

**Filing convention:** `NN_FirstAuthorYEAR_topic.pdf` (matches parent `papers/`).
PDFs are gitignored (paywalled/copyrighted); `.md` notes are committed.

**Extracted facts:** see `key_findings_llm.md` (one structured entry per paper).

---

## A. LLMs performing well on diagnosis

| # | File | Paper | Venue / Year | Shows |
|---|---|---|---|---|
| 1 | `01_Kanjee2023_GPT4-complex-dx.pdf` | Kanjee, Crowe & Rodman — GPT-4 on NEJM CPCs | JAMA 2023 | 64% correct in differential |
| 2 | `02_Brodeur2026_o1-CPC.md` *(stub — paywalled, no PDF)* | Brodeur et al. — o1-preview on CPCs + ED cases | Science 2026 | 88.6% exact/close on CPCs; beat attendings on ED triage |
| 3 | `03_McDuff2025_AMIE-ddx.pdf` | McDuff et al. — Google AMIE differential dx | Nature 2025 | 59.1% top-10 vs 33.6% unassisted clinicians |
| 4 | `04_Tu2025_AMIE-conversational.pdf` | Tu et al. — AMIE conversational diagnostic AI | Nature 2025 | Beat PCPs on 30/32 axes |
| 5 | `05_Cabral2024_GPT4-clinical-reasoning.pdf` | Cabral & Rodman et al. — GPT-4 clinical reasoning vs physicians | JAMA Intern Med 2024 | LLM reasoning competitive with physicians |
| 6 | `06_Korom2025_PendaHealth-AIConsult.pdf` | Korom et al. — Penda Health / OpenAI AI Consult (real-world) | arXiv 2025 | 16% fewer diagnostic errors in deployment |

## B. LLMs performing poorly / limitations

| # | File | Paper | Venue / Year | Shows |
|---|---|---|---|---|
| 7 | `07_Barile2024_LLM-pediatric-dx.pdf` | Barile, Margolis & Cason — LLM on pediatric cases | JAMA Pediatrics 2024 | 83% error rate (pediatrics) |
| 8 | `08_Goh2024_LLM-reasoning-RCT.pdf` | Goh et al. — LLM didn't improve physician reasoning (RCT) | JAMA Netw Open 2024 | +2 pts, not significant |
| 9 | `09_Healy2025_UK-replication.pdf` | **Healy et al.** — UK replication & interaction analysis *(your list said "Bickley")* | medRxiv 2025 | Physicians scored *lower* with LLM than LLM alone |
| 10 | `10_Chen2025_LLM-sycophancy.pdf` | Chen et al. — LLM sycophancy in medical settings | npj Digit Med 2025 | Models defer to user-stated wrong answers |

## C. Missed-diagnosis / error detection (most relevant to us)

| # | File | Paper | Venue / Year | Shows |
|---|---|---|---|---|
| 11 | `11_Haimovich2025_etrigger-LLM_DUP.pdf` *(dup of `papers/30_…`)* | Haimovich et al. — eTriggers + Claude, ED missed opportunities | medRxiv 2025 | Sens 85–100%, PPV 20–45%, NPV ~100% |
| 12 | `12_Harada2024_ChatGPT-error-detection.pdf` | Harada et al. — GPT-4 detecting dx errors in 545 case reports | BMJ Open Qual 2024 | 95% of errors detected |

## D. Condition-specific EHR detection (specificity data)

| # | File | Paper | Venue / Year | Shows |
|---|---|---|---|---|
| 13 | `13_RodriguezNava2025_CLABSI-LLM.pdf` | **Rodriguez-Nava et al.** — GPT-4-turbo for CLABSI *(your list said "Stanford")* | Infect Control Hosp Epidemiol 2025 | Sens 80% / spec 35% → ~75–80% w/ context |
| 14 | `14_Boussina2025_COMPOSER-LLM-sepsis.pdf` | Boussina/Shashikumar et al. — COMPOSER-LLM, prospective sepsis | npj Digit Med 2025 | False alarms cut ~4×, effective PPV >80% |
| 15 | `15_Estiri2025_cognitive-detection.pdf` | Moura, Estiri et al. — agentic workflow, cognitive-concern detection | npj Digit Med 2025 | 98% specificity, confidence-aware |
| 16 | `16_Pan2025_LLM-EHR-disease-detection.pdf` | Pan et al. — LLM + human expertise, EHR disease detection (arXiv preprint) | arXiv 2025 (→ Comput Biol Med) | AMI sens 88%/spec 63%; HTN spec 32% |

## E. Rare / undiagnosed disease

| # | File | Paper | Venue / Year | Shows |
|---|---|---|---|---|
| 17 | `17_Shyr2025_UDN-rare-disease.pdf` | **Shyr et al.** — LLMs for rare disease at the Undiagnosed Diseases Network | JAMA (Res Letter) 2025 | Only 13.3% identified |

---

## Status
- **17/17 accounted for.** #2 Brodeur is a committed `.md` stub (paywalled). #11 Haimovich is a duplicate of `papers/30_…` (kept for self-containment; safe to delete).
- A few **author corrections** vs the original list: #9 is **Healy** (not Bickley); #13 is **Rodriguez-Nava** (not "Stanford"); #16 is the **arXiv preprint** of the Pan EHR-detection work.

## Quick read of the landscape
- **Curated/teaching cases (CPCs):** LLMs look excellent (64% → 88.6%).
- **Real-world / harder settings:** much weaker — pediatrics 83% error, rare/undiagnosed 13.3%, human+LLM RCTs null or negative.
- **As an error-detection *filter* (our space):** strong **rule-out** (high sensitivity/NPV), **low precision/PPV** — matches our AKI findings.
- **Specificity is the recurring weakness** (CLABSI 35%, HTN 32%) — the failure mode to design around.
