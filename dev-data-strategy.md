# Getting realistic patient data without a hospital contract

**Epic's free sandbox is essentially useless for clinical AI development — but a practical path exists.** The sandbox at open.epic.com contains roughly 8–15 test patients with minimal clinical depth, no meaningful notes, and zero real-world messiness. It was designed to test OAuth flows and FHIR parsing, not to build AI. However, a combination of Synthea synthetic data with deliberate error injection, MIMIC-IV's real clinical records (now available in FHIR R4), and specialized NLP datasets can give a solo developer or small team a workable foundation for building a temporal truth layer today — entirely without hospital access.

The most important insight from this research: **no single tool or dataset solves this problem**, but a layered strategy using free resources gets surprisingly close to what you need.

---

## Epic's sandbox: 8 patients named "Test Cancer"

Epic's open sandbox provides roughly **8 named test patients** (Camila Lopez, Derrick Lin, Jason Argonaut, and others) with clinically shallow records. A patient literally named "Test Cancer" lives at "123 Main St." with 1–3 isolated conditions, no comorbidity patterns, and lab values from a single date. Developers consistently report the data is inadequate for anything beyond connectivity testing.

The sandbox exposes FHIR R4 resources including Patient, Condition, MedicationRequest, Observation, DocumentReference, and others. But populated data tells a different story. Querying Camila Lopez's labs returns **two observations from the same date** — one HbA1c, one glucose. No trending. No longitudinal trajectory. No prior values. DocumentReference resources technically exist, but contain no discharge summaries, no progress notes, and no realistic clinical narrative. One test patient's sole clinical note reads: "It was a real big gator" (attached to a "Struck by alligator" condition).

For temporal truth layer development specifically, the sandbox fails on every dimension that matters. There are no conditions that progress, resolve, and recur. No medications started, adjusted, and stopped. No copy-paste note propagation. No contradictions between providers. As one developer analysis put it: "These patients exist to validate API connectivity. They were never designed to represent what real patient data looks like." Epic expanded sandbox capabilities in 2025 with self-service test data creation, but the fundamental constraint remains: **this is a certification tool, not a development environment**.

---

## Synthea generates clean data, but you can make it messy

**Synthea** (by MITRE) is the strongest starting point for synthetic FHIR data. It simulates birth-to-death patient lifecycles using ~120 disease modules built as state-transition machines, outputting native FHIR R4 bundles. Conditions onset, progress, and resolve over time. Medications are prescribed and discontinued. Encounters accumulate across a patient's lifespan. You can generate unlimited patients at no cost under Apache 2.0 licensing.

But Synthea has a fundamental limitation for temporal truth layer work: **it models what should happen, not what actually happens**. Every patient follows clinical guidelines perfectly. There are no stale problem list entries, no medication discrepancies, no copy-paste bloat, no contradictions between providers. A 2023 JAMIA Open study found Synthea diabetes patients had a **4,000% overrepresentation of amputations**, and 100% of asthma patients received the identical inhaler — illustrating that even its "correct" pathways can be unrealistic. A validation study showed Synthea generated 0% blood pressure control rates versus 69.7% in real data.

Synthea does not natively generate clinical notes. The companion tool **Chatty-Notes** bridges this gap by feeding Synthea FHIR bundles to OpenAI's API to generate encounter notes, but it produces clean, well-structured narrative — not the messy, templated, abbreviation-heavy text found in real EHRs.

The critical strategy is to use Synthea as the structural backbone and then **inject known errors** through post-processing. This is a proven approach: a 2025 Data Quality Contract study used Synthea-generated FHIR data for 750,000 patients with explicitly injected "chaos" — schema drift, vocabulary misalignment, completeness regressions, and referential integrity violations. For a temporal truth layer, the injection targets are specific:

- **Problem list staleness**: Add conditions that should have been resolved (acute bronchitis still active 2 years later), omit conditions documented only in notes, leave superseded diagnoses (Type 2 Diabetes when notes show Type 2 Diabetes with nephropathy)
- **Copy-paste propagation**: Duplicate text blocks across encounter notes with outdated information ("post-op day 2" persisting for days), maintaining the ~50% duplication rate found in real-world studies
- **Medication discrepancies**: Discontinued medications still on active lists, dose changes in notes not reflected in structured data, admission/discharge med list mismatches
- **Temporal contradictions**: Specialist notes contradicting primary care assessments, lab results contradicting documented assessments, conditions progressing through stages without prior entries being updated

Other synthetic generators exist but serve different niches. **MDClone** creates synthetic derivatives of real data, preserving statistical properties — but requires access to real source data. **Syntegra** offers FHIR USCDI output trained on 6 million real patient records from community hospitals, available commercially. **HALO** (Nature Communications 2023) and **EHR-Safe** (Google, npj Digital Medicine 2023) are research-grade generative models achieving high fidelity on structured data but aren't turnkey tools.

---

## MIMIC-IV is your most valuable free resource

**MIMIC-IV is the single most important dataset for this use case.** It contains real clinical data from Beth Israel Deaconess Medical Center covering **65,000+ ICU patients** (2008–2022) with structured data and, critically, massive volumes of clinical notes. MIMIC-IV-Note provides **331,794 discharge summaries** and **2,321,355 radiology reports** — real physician-written text with all the messiness that implies.

Three features make MIMIC-IV uniquely valuable for temporal truth layer development:

First, **MIMIC-IV on FHIR already exists**. MIT's team has published a validated conversion with 25 FHIR R4 profiles, 5.84 million resources across ~315,000 patients, aligned to US Core STU4. It's available as NDJSON files on PhysioNet. A 100-patient demo subset is openly available for initial testing. This means you can build your FHIR ingestion pipeline against real data in the same format Epic produces.

Second, the **MIMIC-IV-Ext-22MCTS extension** contains 22.6 million clinical events with timestamps extracted from 267,284 discharge summaries — purpose-built for temporal analysis. This directly supports training temporal reasoning models.

Third, MIMIC data inherently contains the quality problems you need to detect. Studies on MIMIC notes show **~50% of text is duplicated from prior documentation**. Problem lists are known to be incomplete. Medication records contain discrepancies. Multiple note types from different providers contain contradictory information. This isn't a limitation — it's your training signal.

Access requires completing CITI human subjects training and signing a Data Use Agreement through PhysioNet. The license restricts use to "lawful use in scientific research," which has been interpreted to include commercial R&D. You cannot redistribute the data, but you can train models on it and deploy those model weights commercially — the standard approach in healthcare AI.

Beyond MIMIC, several specialized datasets target the exact NLP tasks a temporal truth layer requires:

- **i2b2/n2c2 2012 Temporal Relations Challenge**: Gold-standard annotations of temporal relations (BEFORE, AFTER, OVERLAP) on clinical discharge summaries — directly applicable to temporal reasoning
- **MedNLI** (PhysioNet): Doctor-annotated natural language inference with entailment, contradiction, and neutral labels on clinical text from MIMIC-III
- **EMNLP 2023 Clinical Contradiction Detection dataset**: Built from 22 million medical abstracts using SNOMED-grounded distant supervision for contradiction identification
- **n2c2 2019 Clinical STS**: 2,054 sentence pairs from Mayo Clinic notes scored on 0–5 similarity scale — useful for copy-paste and paraphrase detection

---

## How healthcare AI startups actually get their data

The successful clinical AI companies followed remarkably similar paths. **Abridge** started with de-identified data from consenting patients and academic partnerships with Carnegie Mellon and UPMC. **Regard** secured early backing from Cedars-Sinai Health Ventures, gaining data access through that investment relationship. **Navina** launched in Israel with a government innovation grant, leveraging Israel's more centralized health data infrastructure. **Suki** built a medical-specific ASR system and designed a data flywheel where physician corrections continuously improve models.

The pattern is consistent: **public datasets and synthetic data for proof-of-concept, then one strategic clinical partnership for validation**. As one analysis noted, "A hundred carefully labeled examples can be enough to train and validate a model when paired with the right strategy."

The **Mayo Clinic Platform_Accelerate** program is the single best data access opportunity for early-stage startups. It provides access to de-identified data from **13.6 million patients** including structured data, clinical notes, pathology reports, and radiology reports. The program runs three times per year, has served 40+ startups since 2022, and accepts international applicants. Participants access Mayo's cloud environment by week 6 of the 30-week program. A multiyear pathway option provides up to 2 years of data access.

Other accessible programs include the **Massachusetts Digital Health Sandbox** (rolling grants up to $60,000, with access to simulation facilities and clinical innovation sites), cloud provider startup programs (**AWS Activate** offers up to $100,000 in credits; **Google for Startups** and **Microsoft Founders Hub** offer comparable amounts), and academic medical center partnerships at UCSF, Johns Hopkins, and Mass General Brigham, all of which have formal innovation programs.

---

## What the research literature tells us about EHR messiness

Published research quantifies exactly how messy real clinical data is — and these numbers should calibrate your error injection rates:

**Problem lists are 40–90% incomplete.** A VA study found problem list sensitivity ranged from just **8% for myocardial infarction to 46% for diabetes**. A UK study of 516 COVID patients found only 62.3% of diagnoses appeared on the problem list; chart review uncovered 1,722 additional diagnoses. Intermountain Healthcare found problem list sensitivity of just 8.9% before NLP intervention.

**Half of all clinical note text is copied.** A 2022 analysis of over 100 million notes found **50.1% of text was duplicated** from prior documentation, increasing from ~33% in 2015 to 54.2% by 2020. At UCSF, 82% of inpatient progress notes contained copied or template-generated text. Copy-paste contributed to **35.7% of documentation errors** in a 2013 JAMA Internal Medicine study.

**Medication lists are wrong 70% of the time at transitions of care.** Prior to reconciliation, medication details were nonexistent or incorrect 85% of the time in one study. Computerized medication profiles were inaccurate in 71% of patients in another. Patients consistently report taking more medications than their EHR reflects.

These aren't edge cases — they're the baseline reality of clinical data. A temporal truth layer that can detect and surface these patterns addresses a genuine, pervasive problem.

---

## A practical development roadmap you can start today

For a solo developer or small team building a temporal truth layer without hospital access, here is the recommended phased approach, ordered by what to do first:

**Phase 1 — Build your FHIR pipeline (Week 1–2).** Generate 1,000+ patients with Synthea in FHIR R4. Use this to build your ingestion, parsing, and temporal indexing infrastructure. Synthea is free, unrestricted, and outputs the same FHIR format you'll encounter in production. Download the MIMIC-IV on FHIR 100-patient demo (openly available, no credentialing needed) to validate your pipeline against real data structure.

**Phase 2 — Create your annotated test corpus (Week 2–4).** Build a post-processing pipeline that injects known errors into Synthea output at empirically validated rates: ~38% missing problem list entries, ~50% note text duplication, ~70% medication discrepancies at care transitions. Annotate every injected error with type, severity, source documents, temporal context, and ground truth resolution. This gives you a fully labeled evaluation dataset where you know every answer.

**Phase 3 — Train temporal reasoning on real data (Week 3–6).** Complete PhysioNet credentialing (CITI training takes a few hours; approval takes days to weeks). Access MIMIC-IV on FHIR, MIMIC-IV-Note, and MIMIC-IV-Ext-22MCTS. Use the i2b2 2012 Temporal Relations dataset and MedNLI for supervised temporal NLP training. Use the EMNLP 2023 Clinical Contradiction Detection dataset for contradiction models.

**Phase 4 — Apply for accelerator access (Ongoing).** Apply to Mayo Clinic Platform_Accelerate for access to 13.6 million real patient records. Apply for cloud credits (AWS, Google, Microsoft — $100–150K each). Identify one physician champion at an academic medical center willing to provide consented, de-identified data for validation.

**Phase 5 — Validate and iterate.** Test your temporal truth layer against MIMIC-IV's inherent data quality issues (copy-paste in notes, incomplete problem lists, medication discrepancies). Compare detection rates against published literature benchmarks. Use the eICU database (139,000 patients across 208 hospitals) to test generalization across institutions.

The key architectural insight: **design your system to collect corrections from day one**. Every startup that succeeded — Abridge, Suki, Regard — built a data flywheel where clinician feedback on AI output becomes training data. Your temporal truth layer should capture when clinicians confirm or reject its findings, creating a continuously improving dataset that eventually surpasses anything synthetic.

---

## Conclusion

Epic's sandbox is a connectivity test, not a development environment. But the broader ecosystem provides everything a temporal truth layer needs. **Synthea gives you unlimited FHIR structure. MIMIC-IV gives you real clinical messiness in FHIR format. Specialized NLP datasets give you annotated temporal reasoning and contradiction detection training data. Error injection at published prevalence rates gives you a labeled evaluation corpus.** No hospital contract is required for any of this.

The gap that no existing tool fills — generating synthetic data with realistic EHR messiness built in — is itself a product opportunity. The DQC chaos injection framework and published prevalence rates from copy-paste, problem list, and medication reconciliation research provide the blueprint. Build the error injection layer once, and you have both your test harness and a potential contribution back to the healthcare AI development community.

The most underutilized resource is MIMIC-IV on FHIR: 5.84 million real FHIR resources, 331,000 discharge summaries, 2.3 million radiology reports, and 22.6 million timestamped clinical events — all accessible within weeks of starting the credentialing process, and all in the exact format your production system will consume.