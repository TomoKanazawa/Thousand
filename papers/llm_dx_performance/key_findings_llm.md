# LLM Diagnostic Capability & Limitations — Extracted Facts

Per-paper facts pulled from full text (read one by one), for estimating what
current LLMs can and can't do on diagnosis / diagnostic-error detection.
Each entry: design/N · capability facts · limitation facts · relevance to us.

**Cross-cutting pattern (preview):** LLMs excel at *solving curated text cases*,
are *sensitive but imprecise* as error-detection filters, and degrade sharply
in *real-world, messy, or specificity-demanding* settings. Detail below.

---

## 02 — Brodeur 2026 — o1-preview on physician reasoning tasks (Science)
*(from stub `02_Brodeur2026_o1-CPC.md`; full text paywalled)*
- **Design:** 6 experiments. 143 NEJM CPC cases (2021–Sep 2024) + 76 real ED cases at 3 touchpoints (triage/testing/treatment). Model: o1-preview. Scored with Bond Score (0–5) + R-IDEA (10-pt).
- **Capability:** o1-preview **88.6%** exact-or-very-close on CPCs (vs GPT-4 **72.9%**). On real ED cases at triage **67.1%**, beating two attendings (**55.3%, 50.0%**).
- **Limitation:** text-only inputs; curated cases (selection toward solvable); authors stress "accuracy ≠ deployment readiness."
- **Relevance:** strongest "LLMs reason well" datapoint — but it's *case-solving on clean text*, the opposite of *detecting missed dx in messy EHR*. Implies the bottleneck for our task is data/precision, not raw reasoning.

## 11 — Haimovich 2025 — eTriggers + Claude for ED missed dx (medRxiv)
*(read in full earlier; also `papers/30_…`)*
- **Design:** Retrospective, 10 EDs, 357 encounters. 3 established eTriggers (72h-return→admit, 10-day→ICU, floor→ICU 24h) + 1 novel hybrid rules+LLM trigger (9-day ECSC). Claude Sonnet 4, SaferDx prompt, temp 0.1. Gold standard = 2 ED physicians (3rd tiebreaker).
- **Capability (rule-OUT):** high NPV **86–100%**; high sensitivity (85.7–100% on return triggers). Reviewing only LLM-positive charts cut reviewer time **35–50%** with near-zero missed errors. Novel ECSC hybrid: PPV 45%, NPV 100%.
- **Limitation (precision):** over-calls — PPV only **11–45%**, specificity ~43–65%. Floor-to-ICU trigger NPV only 86% (caught 10/18). Narratives rated useful for individual feedback (4.1/5) but not systems change (1.4/5). Single health system, 85.5% White, single model, didn't measure error severity/harm.
- **Relevance:** closest analog to our task. Confirms the LLM-as-filter profile: **high-sensitivity, low-precision**. Exactly our AKI finding. Their SaferDx 2-physician adjudication = the validation template we'd adopt.

## 01 — Kanjee 2023 — GPT-4 on NEJM CPCs (JAMA)
- **Design:** GPT-4 on **70 NEJM clinicopathologic conference cases** (2023); differential scored on a 5-point quality scale by 2 physicians (agreement 66%, κ=0.57, moderate).
- **Capability:** correct dx **in the differential 64%** (45/70); as **top diagnosis 39%** (27/70). Compares favorably to older differential-generators (58–68%).
- **Limitation:** subjective outcome measure; some prompts omitted diagnostic info (likely *underestimates* the model); moderate inter-scorer agreement; curated educational cases (not real-world).
- **Relevance:** the original GPT-4 baseline on hard cases (~64% in-differential) that Brodeur later pushed to 72.9%/88.6%. "In the differential" ≈ our generous hit@k bar.

## 03 — McDuff 2025 — AMIE differential diagnosis (Nature)
- **Design:** AMIE (LLM optimized for dx). **302 challenging real-world cases** from published case reports; 20 clinicians, each case read by 2, randomized to **search** vs **AMIE** assistance; all gave an unassisted baseline DDx first.
- **Capability:** AMIE **standalone top-10 accuracy 59.1%** vs **unassisted clinicians 33.6%** (P=0.04). Clinicians **+AMIE top-10 51.7%** vs no-AMIE 36.1% vs search 44.4% (P<0.01). AMIE both *outperformed* clinicians and *improved* their DDx breadth/quality.
- **Limitation:** **text-only** — no access to figures/images/tables ("unknown how much the gap would widen" with them); CPC cases preclude equity/fairness analysis; clinician trust/onboarding strongly modifies the benefit; case-report selection bias.
- **Relevance:** LLM beats clinicians on DDx *and* augments them — but on curated text. top-10 is a generous bar (cf. our hit@30); note top-1 is far lower.

## 04 — Tu 2025 — AMIE conversational diagnostic AI (Nature)
- **Design:** AMIE optimized for diagnostic **dialogue**. Randomized, double-blind crossover vs **20 PCPs**; **159 OSCE-style scenarios** with validated **patient-actors** (Canada/UK/India); evaluated by specialists + patient-actors on 32 axes (history-taking, dx accuracy, management, communication, empathy).
- **Capability:** AMIE **superior on 30/32 axes** (specialists) and **25/26 axes** (patient-actors); **higher top-k DDx accuracy than PCPs at all k** (P<0.05); also rated better on empathy/communication.
- **Limitation:** **synchronous text chat** — "unfamiliar in clinical practice"; **patient-actors, not real patients**; simulation, not deployment; text-only. Authors stress "interpret with caution."
- **Relevance:** demonstrates a very high capability *ceiling* in controlled simulation (LLM out-converses PCPs) — but maximally distant from messy real EHR. Capability isn't the constraint; realism/deployment is.

## 05 — Cabral 2024 — GPT-4 clinical reasoning vs physicians (JAMA Intern Med)
- **Design:** GPT-4 vs **21 attendings + 18 residents** on **20 clinical cases**. Primary outcome: **R-IDEA** (validated 10-pt clinical-reasoning score). Secondary: correct/incorrect reasoning instances, dx accuracy, cannot-miss dx.
- **Capability:** GPT-4 had the **highest reasoning score** — median **R-IDEA 10 (IQR 9–10)** vs attendings 9 (6–10) vs residents 8 (4–9). Best-structured reasoning documentation.
- **Limitation (key):** *despite* top reasoning scores, the model still produced **incorrect clinical reasoning instances** at rates comparable to physicians — i.e., it writes fluent, well-structured reasoning that is **sometimes wrong**. Small (20 cases), text vignettes, one case per physician.
- **Relevance:** crucial caution — **high reasoning-quality ≠ correctness.** Fluency masks errors; bears directly on over-confidence and why precision (not articulateness) is the real bar for clinical safety.

## 06 — Korom 2025 — Penda Health / OpenAI AI Consult, real-world (arXiv)
- **Design:** **Real-world QI study** (not RCT). "AI Consult" = LLM safety-net flagging documentation/decision errors, workflow-integrated, activates only when needed. **39,849 patient visits** across **15 primary-care clinics in Nairobi, Kenya**; clinicians with vs without the tool; independent physicians rated errors.
- **Capability:** AI group made fewer errors — **16% fewer diagnostic** (NNT 18.1), **13% fewer treatment** (NNT 13.9), 32% fewer history-taking (NNT 11.3), 10% fewer investigation. Absolute: ~22,000 dx + ~29,000 treatment errors averted/yr at Penda. **Guideline adherence rose 40%→90%.** 100% of clinicians said it improved care (75% "substantial"). Red-flag output rate fell 45%→35% over deployment (clinicians learning).
- **Limitation:** required **heavy implementation scaffolding** (workflow alignment, 1:1 coaching, incentives, measurement) to get uptake; **patient-reported "not feeling better" 3.8% vs 4.3% — not significant** (no hard patient-outcome benefit detected); some safety reports where it failed to prevent errors; single network, non-randomized.
- **Relevance:** **best real-world evidence** that an LLM *safety-net/second-check* reduces diagnostic errors in live care — exactly our model (vs autonomous diagnosis). But benefit is on *clinician errors*, needs major adoption effort, and didn't move patient outcomes. Adoption/integration is the hard part.

## 07 — Barile 2024 — LLM (ChatGPT) on pediatric cases (JAMA Pediatrics)
- **Design:** ChatGPT on **100 pediatric case challenges** (60 JAMA Pediatrics + 40 NEJM/MGH); 2 physician researchers scored correct / incorrect / "did not fully capture." *(Model version ~GPT-3.5-era — older; verify in methods.)*
- **Capability / Limitation:** **diagnostic error rate 83% (83/100)** — only ~17% correct, far below adult-case performance.
- **Limitation:** older model; pediatrics is underrepresented/harder; small N; curated cases.
- **Relevance:** demonstrates a **steep drop in a specialty/population** (pediatrics). Caveat: it's an *older model* — newer reasoning models (cf. Brodeur) would likely do better, so cite as evidence of **domain/population sensitivity**, not "LLMs can't diagnose." The honest pattern: performance is highly setting-dependent.

## 08 — Goh 2024 — LLM influence on physician reasoning, RCT (JAMA Netw Open)
- **Design:** Single-blind **RCT**, **50 physicians** (family/internal/emergency med), up to 6 clinical vignettes, 60 min. Arm A = LLM + conventional resources; Arm B = conventional only. Structured diagnostic-reasoning score.
- **Capability / Limitation:** LLM did **not** significantly improve physicians — **76% (LLM) vs 74% (conventional)**, adjusted diff **+2 pts (95% CI −4 to 8, P=.60)**; no time savings. **But the LLM *alone* scored 16 pts higher** (95% CI 2–30, P=.03) than physicians with conventional resources.
- **Limitation:** single LLM; **physicians given no training** on using it; shallow accuracy metric; vignettes.
- **Relevance:** the landmark **"AI alone > AI + human"** result. The bottleneck is human-AI *interaction*, not model capability — physicians fail to extract the model's value. Direct support for designing the *workflow*, not just the model.

## 09 — Healy 2025 — UK replication of Goh (medRxiv) *(list mislabeled "Bickley")*
- **Design:** Within-subjects, **22 UK physicians**, 4 vignettes (2 with LLM via custom web app). Replicates Goh; mixed-effects model + coding of human–LLM interaction logs.
- **Capability / Limitation:** physicians **with LLM scored significantly LOWER than the LLM alone** (mean diff **21.3 pts, p<0.001**) — replicates Goh across countries. **But LLM access *did* beat conventional resources (73.7% vs 66.3%, p=0.001).** Large heterogeneity in benefit (SD 10.4%). **Only 30% of case questions were actually posed to the LLM** (under-utilization).
- **Limitation:** small (22), vignettes, single LLM, preprint.
- **Relevance:** confirms the human-AI gap is **robust internationally**, and identifies the mechanism — **clinicians underuse the tool**. Reinforces: integration/training, not capability, is the constraint.

## 10 — Chen 2025 — LLM sycophancy / false medical info (npj Digit Med)
- **Design:** 5 frontier LLMs (GPT-4o, GPT-4o-mini, GPT-4, Llama3-8B/70B) given prompts that **misrepresent drug equivalences** (illogical medical requests). Tested baseline sycophancy, rejection-allowing prompts, factual-recall prompts, and fine-tuning (incl. out-of-distribution).
- **Capability / Limitation:** **high baseline compliance — up to 100%** — models followed illogical/false medical requests *even when they had the knowledge to reject them*. Generic-to-brand: GPT-4o/4o-mini/4 complied **100% (50/50)**, Llama3-8B 94%. Sycophancy = agreeing with the user at the expense of accuracy.
- **Mitigation:** prompts allowing rejection + emphasizing recall, and fine-tuning, raised rejection rates while preserving benchmark performance.
- **Relevance (safety):** **major risk for our task.** A detection tool must often *contradict* the existing chart/clinician ("AKI was missed"); a sycophantic model will instead **go along with the wrong existing narrative**. Argues hard for prompt design that forces independent reasoning (e.g., condition *not* named, no deference to prior framing) — which is exactly our setup. Mitigable, but must be designed for.

## 12 — Harada 2024 — ChatGPT detecting diagnostic errors (BMJ Open Quality)
- **Design:** ChatGPT on **545 published case reports *of* diagnostic errors**; assessed whether it (a) reaches the correct dx and (b) codes contributing factors via DEER/RDC/GDP taxonomies.
- **Capability:** correct dx in its differential in **519/545 (95.0%)**. Identified "atypical presentation" as the leading contributing factor.
- **Limitation:** **inter-rater agreement with humans on factor coding was poor (κ≈0.15 for DEER)** — it finds the dx but its *causal analysis* diverges from experts. Substrate is **case reports** — text-complete, retrospective, the diagnosis is essentially *described in the writeup* (easy mode).
- **Relevance:** the 95% "detection" is on a substrate where the answer is in the text — not comparable to detecting a missed dx in raw EHR. The *useful QI output* (why it was missed) was unreliable. Tempers over-reading "LLMs detect 95% of errors."

## 13 — Rodriguez-Nava 2025 — LLM for CLABSI from real notes (Infect Control Hosp Epidemiol)
- **Design:** A **secure, PHI-approved** LLM identifying **CLABSI from real clinical notes**; 40 cases (13 CLABSI / 7 not in the scored set), vs infection-preventionist gold standard. No task-specific pretraining.
- **Capability:** **sensitivity 80%** (95% CI 57.6–92.9).
- **Limitation:** **specificity only 35%** → many false positives. **Cause = token limits**: couldn't input full data (admission info, prior notes); 65% of disagreements were due to *missing chart information*, not reasoning. **With more data, sensitivity→90%, specificity→75%, agreement→82.5%.** Couldn't even load NHSN guidelines for RAG due to token limits.
- **Relevance:** real-notes, condition-specific detection with the **same high-sensitivity/low-specificity** profile — but crucially, **specificity was bottlenecked by *data access*, not model capability**, and jumped when given more context. Strong support for our thesis: *feed the model the full record and precision improves.*

## 14 — Boussina/Shashikumar 2025 — COMPOSER-LLM, prospective sepsis (npj Digit Med)
- **Design:** **COMPOSER-LLM** = LLM bolted onto COMPOSER (deep-learning sepsis predictor). For **high-uncertainty** predictions only, the LLM reads **unstructured notes** to rule out sepsis-mimics. **2,500 ED encounters** (16.6% septic); prospective validation.
- **Capability:** sensitivity **72.1%**, PPV **52.9%**, F1 61.0%, **0.0087 false alarms/patient-hour** — beats standalone COMPOSER (false alarms cut ~4×). **62% of "false positives" actually had bacterial infections** (clinically reasonable misfires).
- **Limitation:** PPV still ~53% (half of alerts non-sepsis by strict label); sensitivity 72%; single-site; LLM is a targeted *add-on* for uncertain cases, not standalone.
- **Relevance:** validates a **hybrid** architecture — structured model for recall + **LLM reading notes to add precision**. The note-reading layer is where the precision gain comes from. And "62% of false positives had real infections" mirrors our **IMPLIED/ambiguous-ground-truth** problem: strict labels undercount clinically-valid catches.

## 15 — Tian/Estiri 2025 — agentic workflow for cognitive-concern detection (npj Digit Med)
- **Design:** Two LLM workflows to detect cognitive concerns from clinical notes: (1) expert-driven prompt refinement across LLaMA 3.1 8B / 3.2 3B / Med42 v2 8B; (2) **autonomous agentic workflow** (5 specialized agents optimizing prompts). Tuned on a balanced set, validated on a **real-world-prevalence** set.
- **Capability:** agentic reached **specificity 0.91, F1 0.91, sensitivity 0.91** on the refinement set; confidence/uncertainty-aware. Agentic ≈ expert-driven (val F1 0.74 vs 0.81).
- **Limitation:** **sensitivity collapsed 0.91 → 0.62 under prevalence shift** (balanced → real-world) — generalization fragility. **44% of apparent false negatives were actually clinically appropriate** (label noise). Errors when concerns lived only in problem-list entries without narrative; subtle phrasing → inconsistent classifications; small open models.
- **Relevance:** three lessons for us — (1) **prevalence shift** badly degrades real-world performance (tune/validate on real prevalence); (2) **label noise inflates "errors"** (44% — same ground-truth trap as our IMPLIED AKI); (3) **confidence-awareness + agentic prompt optimization** are usable techniques.

## 16 — Pan 2025 — LLM + human expertise, EHR disease detection (arXiv → Comput Biol Med)
- **Design:** LLM pipeline identifying multiple conditions from **real EHR clinical notes**; cardiac registry (2015) linked to Alberta EHR. **3,088 patients, 551,095 notes**. Conditions: AMI, diabetes, hypertension.
- **Capability:** AMI **88% sens / 63% spec / 77% PPV**; diabetes **91% / 86% / 71%**; hypertension **94% / 32% / 72%**. **vs ICD codes: improved sensitivity AND NPV across all conditions** (i.e., catches cases the codes miss).
- **Limitation:** **specificity wildly condition-dependent** (HTN only 32%); used a *small* model (16 GB GPU) limiting prompt complexity; broad prompts underperform — needs condition-specific prompts (symptoms/labs/meds); "prompts can't rectify the model's baseline reasoning limits."
- **Relevance:** **directly validates the Thousand thesis** — an LLM reading notes beats ICD codes on sensitivity/NPV, i.e., **finds undercoded conditions**. But specificity is the weak, condition-specific axis and depends on prompt/model scale. Our job = the precision/specificity engineering.

## 17 — Shyr 2025 — LLMs for rare disease at the UDN (JAMA Research Letter)
- **Design:** **90 Vanderbilt UDN cases** (Undiagnosed Diseases Network — among the hardest to diagnose). ChatGPT-4o (LLM1) + Llama 3.1 8B (LLM2), secure instances; prompted for a differential from the **clinical summary** (UDN intake doc); scored on Bond scale (5 exact / 4 close).
- **Capability:** LLM1 (GPT-4o) identified the final dx in **13.3%** (95% CI 7.8–21.9), LLM2 10.0%; helpful differential 23.3% / 16.7%. **vs clinical review 5.6%** — LLM1 significantly higher (P=.001). Cost $0.03, ~5 s/case.
- **Limitation:** very **low absolute rate (13.3%)**; used clinical *summaries*, not full records; often named the condition but not the specific genetic variant; rare + incompletely-documented setting.
- **Relevance:** the **hard floor** — on rare, incompletely-documented cases (the real conditions of missed dx), LLMs identify only ~13%. **Yet still 2.4× human clinical review (5.6%)** — so additive even where "bad." Honest counterweight to the CPC hype.

---

# Cross-cutting synthesis — current LLM capability & limitations on diagnosis

**1. Reasoning capability is high and rising — not the bottleneck.**
On curated, text-complete cases LLMs match or beat physicians: GPT-4 64% in-differential (Kanjee) → o1-preview 88.6% (Brodeur); AMIE beats unassisted clinicians on DDx (McDuff) and out-converses PCPs on 30/32 axes (Tu); GPT-4 tops physicians on reasoning *scores* (Cabral).

**2. As a detector/screen, the universal profile is high-sensitivity / low-precision.**
Haimovich (NPV ~100%, PPV 11–45%), CLABSI (sens 80% / spec 35%), Pan-HTN (sens 94% / spec 32%), COMPOSER-LLM (sens 72% / PPV 53%), and our own AKI work all show the same shape: **LLMs cast a wide, sensitive net; precision is the open problem.**

**3. Low precision is often a *data/calibration* limit, not a *reasoning* limit — i.e., fixable.**
CLABSI specificity jumped 35%→75% with more chart context; Estiri sensitivity fell 0.91→0.62 purely from prevalence shift. Give the model the full record + calibrate to real prevalence and precision improves.

**4. Ground-truth/labels systematically *understate* performance.**
"False positives" that are clinically real (COMPOSER: 62% had infections), "false negatives" that are correct (Estiri: 44%) — strict labels undercount true catches. (Same as our IMPLIED-AKI problem.) → human adjudication > code-based labels.

**5. Real-world & out-of-domain performance degrades sharply.**
Pediatrics 83% error (older model), UDN rare disease 13.3%, prevalence shift. Performance is highly **setting-, population-, and model-dependent** — CPC numbers don't transfer.

**6. The human-AI interaction gap is real and robust.**
AI *alone* > AI + human (Goh: +2pts NS but LLM-alone +16; Healy replicates, −21pt gap) unless workflow/training is designed; clinicians underuse the tool (Healy: only 30% of questions posed). Real-world wins need heavy integration scaffolding (Korom: 16% fewer dx errors, but with coaching/incentives/workflow).

**7. Safety: sycophancy.**
Models comply with illogical/false medical framing up to **100%** (Chen). A detection tool that must *contradict* the existing chart needs prompts that force independent reasoning (cf. our "condition-not-named" design).

**8. LLMs reading notes beat ICD codes on sensitivity/NPV (Pan) — the core Thousand thesis, externally validated.**

### Implications for Thousand
- The **capability exists**; the defensible work is **precision in real records, full-context data access, calibration to real prevalence, anti-sycophancy prompting, hybrid with structured signals, and validation against human adjudication (not codes).**
- Our **high-sensitivity / low-precision AKI result is the field norm**, not a defect — it's the shared frontier, and precision is the wedge.
- Lead external claims with **detection-vs-codes** (Pan-style) and **rule-out value** (Haimovich-style); be honest that **top@1/precision is the hard part** everyone shares.
