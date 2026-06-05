# 02 — Brodeur 2026 — o1-preview on the reasoning tasks of a physician

> **Stub note (no PDF).** The full text is paywalled (Science, HTTP 403). This
> entry is compiled from the official abstract, press summaries, and the open
> preprint. **Verify numbers against full text before quoting verbatim.**

- **Intended file:** `02_Brodeur2026_o1-CPC.pdf` (not stored — paywalled/copyright)
- **Citation:** Brodeur PG, Buckley TA, Kanjee Z, Goh E, Chen JH, Manrai AK, Rodman A, et al. *Performance of a large language model on the reasoning tasks of a physician.* **Science. 2026;392:524.** doi:10.1126/science.adz4433.
- **Open preprint:** "Superhuman performance of a large language model on the reasoning tasks of a physician," arXiv:2412.10849 (Dec 2024) — earlier title, freely downloadable; the published Science version dropped "Superhuman."
- **Group:** Same Beth Israel Deaconess / Harvard (Rodman, Kanjee) + Stanford (Goh, Chen) lab cluster as several other papers in this folder.

## Design / N
- **Six experiments** comparing **OpenAI o1-preview** against prior models (GPT-4) and physicians on clinical reasoning.
- **143 NEJM clinicopathological conference (CPC) cases**, published 2021 – Sept 2024; o1-preview prompted Sept 2024.
- **6th experiment:** **76 actual emergency department cases**, evaluated at **three diagnostic touchpoints** (triage → testing → treatment).
- **Scoring instruments:** **Bond Score** (0–5, differential-diagnosis quality, by attending internal-medicine physicians); **R-IDEA** (10-point clinical-reasoning documentation); plus "exact or very close" diagnostic accuracy.

## Key numbers
- **CPC cases (differential accuracy, exact-or-very-close):**
  - **o1-preview: 88.6%**
  - GPT-4: 72.9%
- **Real ED cases — exact-or-very-close at initial triage:**
  - **o1-preview: 67.1%**
  - Attending physician A: 55.3%
  - Attending physician B: 50.0%
  - → o1-preview outperformed both expert attendings on text-based triage diagnosis.

## Headline quote (from abstract / coverage)
- "[o1-preview] outperform[ed] … attending physicians" on text-based diagnostic reasoning, while the authors caution that the study "addresses only text-based performance … clinical medicine is multifaceted and awash with nontext inputs," and that "accuracy on a defined task is only one dimension of deployment readiness."

## Relevance to our work
- **Strongest "LLMs are good at diagnosis" data point** in the folder: a frontier **reasoning model** beats both GPT-4 and expert attendings on hard differential-diagnosis tasks, including real ED cases at triage.
- **But it's the *opposite task* from ours.** This measures *solving a presented case* (generate the right differential) on **curated, text-complete vignettes**. Our problem is **detecting a missed/undocumented condition from messy EHR data** — a screening/precision problem, not a case-solving one.
- **Caveats that protect our framing:** text-only inputs; curated cases (selection bias toward solvable, well-documented presentations); accuracy ≠ deployment readiness. The real-world papers in this folder (pediatrics 83% error, UDN 13.3%, human+LLM RCTs null) show the gap between CPC performance and the wild.
- **Takeaway for the pitch:** frontier models clearly *can* reason at/above physician level on clean cases — so the bottleneck for catching missed diagnoses isn't raw reasoning, it's **data access, signal extraction, and precision/specificity in real records**. That's exactly the wedge.

## Sources
- [Science — Performance of a large language model on the reasoning tasks of a physician](https://www.science.org/doi/10.1126/science.adz4433) (paywalled)
- [Inside Precision Medicine — Could AI Surpass Doctors at Clinical Reasoning?](https://www.insideprecisionmedicine.com/topics/precision-medicine/could-ai-surpass-doctors-at-clinical-reasoning/)
- [Science Media Centre — expert reaction](https://www.sciencemediacentre.org/expert-reaction-to-study-evaluating-performance-of-a-large-language-model-on-the-reasoning-tasks-of-a-physician/)
- [Singularity Hub — An AI Just Beat Doctors at Diagnosing ER Patients](https://singularityhub.com/2026/05/04/an-ai-just-beat-doctors-at-diagnosing-er-patients/)
- Preprint: arXiv:2412.10849
