# Andy — Literature Source-of-Truth

**Purpose:** Consolidated key findings from 71 papers/sources collected to support TAM / SAM calculations and team-facing claims about Andy's market opportunity.

**How to use:**
- Every numeric claim Andy makes externally should trace back to an entry here.
- Each entry includes: full citation, design/N, headline numbers with units, a short verbatim quote, and a 1-2 sentence SAM-relevance note.
- Confidence: peer-reviewed journal + gov reports = high. Industry survey = medium. Vendor / press release = low.
- Entries marked **"Stub-derived only"** were extracted from PubMed abstracts or the publisher's abstract page because the full PDF was paywalled — verify against full text before quoting verbatim.
- Some entries flag verification needs (wrong PDF, missing stat, etc.) — see "Verification queue" at the bottom.

**Coverage:** 71 of 72 numbered references (one was a duplicate; #43 PDF is the wrong paper and needs re-download).

---

## Section A — Diagnostic error epidemiology, never-detected conditions, outpatient undiagnosed (#01–#28)

# Section A — Findings from papers #01–#28

### 01 — Newman-Toker 2024 — Burden of Serious Harms from Diagnostic Error in the US ("Big Three")

- **Source:** `01_NewmanToker2024_burden-of-dx-error.pdf`
- **Citation:** Newman-Toker DE, Nassery N, Schaffer AC, et al. Burden of Serious Harms from Diagnostic Error in the United States: A National, Cross-Sectional Analysis Using "The Big Three". BMJ Qual Saf. 2024;33(2):109–120. doi:10.1136/bmjqs-2021-014130.
- **Design / N:** Cross-sectional national extrapolation, 21.5M sampled US hospital discharges (2012–2014) + cancer registries (2014); Monte Carlo simulation.
- **Key numbers:**
  - Annual US incidence: 6.0M vascular events, 6.2M infections, 1.5M cancers.
  - Weighted mean error rate per Big Three case: 11.1%; serious-harm rate: 4.4%.
  - Total US serious misdiagnosis-related harms: ~795,000/year (plausible range 598,000–1,023,000).
  - Conservative sensitivity estimate: 549,000 serious harms/year.
  - 15 dangerous diseases = 50.7% of serious harms; top 5 (stroke, sepsis, pneumonia, VTE, lung cancer) = 38.7%.
- **Headline quote:** "estimated total serious harms annually in the US to be 795,000 (plausible range 598,000-1,023,000)." (Abstract)
- **SAM relevance:** Headline TAM denominator for misdiagnosis harm in the US; bounds the addressable injury population Andy can prevent across inpatient/ED/ambulatory.

### 02 — Dalal 2024 — Adverse diagnostic events in hospitalised patients (stub)

- **Source:** `02_Dalal2024_adverse-dx-events.md`
- **Citation:** Dalal AK, Plombon S, Konieczny K, et al. Adverse diagnostic events in hospitalised patients: a single-centre, retrospective cohort study. BMJ Qual Saf. 2025 May;34(6):377–388. doi:10.1136/bmjqs-2024-017183.
- **Design / N:** Single-center retrospective cohort, stratified sampling of 675 from 9,147 eligible general-medicine inpatients; Safer Dx adjudication.
- **Key numbers:**
  - Harmful diagnostic errors: 7.2% of inpatients (95% CI 4.66–9.80).
  - Preventable diagnostic errors: 6.1% (95% CI 3.79–8.50).
  - Severely harmful errors: 1.1% (95% CI 0.55–1.68).
  - Delays involved in 61.9% of harmful errors.
  - ~1 in 14 general-medicine inpatients suffer preventable harmful dx errors.
- **Headline quote:** "harmful diagnostic errors in 7.2% (95% CI 4.66–9.80)" (Abstract; stub).
- **SAM relevance:** Strongest contemporary inpatient denominator (7.2% harm) for sizing Andy's hospital TAM. Stub-derived only — verify against full text before citing.

### 03 — Auerbach 2024 — UPSIDE: Diagnostic errors in hospitalised patients with suspected pneumonia, sepsis, or HF

- **Source:** `03_Auerbach2024_UPSIDE.pdf`
- **Citation:** Auerbach AD, Lee TM, Hubbard CC, et al. Diagnostic Errors in Hospitalized Adults Who Died or Were Transferred to Intensive Care. JAMA Intern Med. 2024;184(2):164–173. doi:10.1001/jamainternmed.2023.7347.
- **Design / N:** Retrospective cohort, 29 academic medical centers, n=2,428 hospitalized adults transferred to ICU or who died.
- **Key numbers:**
  - Diagnostic error in 23.0% of patients (550/2,428; 95% CI 20.9–25.3%).
  - Errors contributed to temporary harm, permanent harm, or death in 17.8% (436/2,428; 95% CI 15.9–19.8%).
  - Among 1,863 deaths, dx error contributed to death in 6.6% (121; 95% CI 5.3–8.2%).
  - Top causes: patient-assessment problems aPAF 21.4% (95% CI 16.4–26.4%); test ordering/interpretation aPAF 19.9% (95% CI 14.7–25.1%).
- **Headline quote:** "550 patients (23.0%; 95% CI, 20.9%-25.3%) had experienced a diagnostic error." (p.164)
- **SAM relevance:** Anchors the ICU-transfer / inpatient-deterioration TAM — nearly 1 in 4 high-acuity admits has a dx error, of which ~3/4 are harmful. Direct trigger pool for Andy.

### 04 — Gunderson 2020 — Prevalence of harmful dx errors in hospitalised adults: meta-analysis (stub)

- **Source:** `04_Gunderson2020_harmful-dx-errors-meta.md`
- **Citation:** Gunderson CG, Bilan VP, Holleck JL, et al. Prevalence of harmful diagnostic errors in hospitalised adults: a systematic review and meta-analysis. BMJ Qual Saf. 2020 Dec;29(12):1008–1018. doi:10.1136/bmjqs-2019-010822.
- **Design / N:** Meta-analysis, 22 studies, 80,026 patients, 760 documented harmful dx errors.
- **Key numbers:**
  - Pooled harmful dx error rate: 0.7% of adult hospital admissions (95% CI 0.5–1.1%).
  - Translates to ~249,900 harmful dx errors/year in US hospitals.
  - Most frequently missed: malignancy and pulmonary embolism.
- **Headline quote:** "pooled rate was 0.7% (95% CI 0.5% to 1.1%) of adult hospital admissions" (Abstract; stub).
- **SAM relevance:** Conservative meta-analytic floor for inpatient harmful dx error; brackets the inpatient TAM together with Dalal (#02) 7.2%. Stub-derived only — verify against full text before citing.

### 05 — Singh 2014 — Frequency of outpatient diagnostic errors in the US

- **Source:** `05_Singh2014_outpatient-dx-error-freq.pdf`
- **Citation:** Singh H, Meyer AND, Thomas EJ. The frequency of diagnostic errors in outpatient care: estimations from three large observational studies involving US adult populations. BMJ Qual Saf. 2014;23:727–731.
- **Design / N:** Synthesis of three e-trigger / chart-review studies; extrapolation to US adult population.
- **Key numbers:**
  - Outpatient diagnostic error rate: 5.08% of US adults annually.
  - ~12 million US adults experience an outpatient dx error/year.
  - ~Half potentially harmful (~6M harmful/year).
- **Headline quote:** "rate of outpatient diagnostic errors of 5.08%, or approximately 12 million US adults every year." (Abstract)
- **SAM relevance:** Defines the outpatient TAM denominator for Andy's ambulatory copilot; canonical "12M/year" stat.

### 06 — Singh 2013 — Types and Origins of Diagnostic Errors in Primary Care

- **Source:** `06_Singh2013_primary-care-dx-error.pdf`
- **Citation:** Singh H, Giardina TD, Meyer AND, Forjuoh SN, Reis MD, Thomas EJ. Types and Origins of Diagnostic Errors in Primary Care Settings. JAMA Intern Med. 2013;173(6):418–425. doi:10.1001/jamainternmed.2013.2777.
- **Design / N:** Retrospective record review, 190 confirmed dx errors at 1 VA + 1 large private system, 2006–2007.
- **Key numbers:**
  - 68 unique diagnoses missed across 190 cases.
  - Top missed: pneumonia 6.7%, decompensated CHF 5.7%, acute renal failure 5.3%, primary cancer 5.3%, UTI/pyelonephritis 4.8%.
  - Process breakdowns: patient-practitioner encounter 78.9%; referrals 19.5%; follow-up/tracking 14.7%; test performance/interpretation 13.6%.
  - 43.7% of cases involved >1 process breakdown.
  - Encounter sub-faults: history-taking 56.3%, exam 47.4%, test ordering 57.4%.
- **Headline quote:** "Most missed diagnoses were common conditions in primary care, with pneumonia (6.7%)…" (Abstract)
- **SAM relevance:** Maps the disease mix Andy must cover in PCP-facing product; quantifies that history+exam+test-ordering are dominant fault modes.

### 07 — Pandey 2025 — Under/over-diagnosis of sepsis in the first hour of ED care

- **Source:** `07_Pandey2025_sepsis-under-over-dx.pdf`
- **Citation:** Pandey SR, Knack SKS, Driver BE, et al. Factors and outcomes associated with under- and overdiagnosis of sepsis in the first hour of emergency department care. Acad Emerg Med. 2025;32:204–215. doi:10.1111/acem.15074.
- **Design / N:** Secondary analysis, prospective single-center cohort, n=2,484 undifferentiated critically ill ED medical patients (Sept 2020–May 2022).
- **Key numbers:**
  - 275/2,484 (11%) had explicit discharge dx of sepsis present on arrival.
  - VAS ≥50 at 15 min: sensitivity 0.83 (95% CI 0.78–0.87), specificity 0.85 (0.83–0.86).
  - Missed cases: 48 (17%) at 15 min; 23 (8%) at 60 min.
  - Missed dx → median 48-min (IQR 27–64) antibiotic delay (not independently linked to mortality after severity adj).
- **Headline quote:** "275 (11%) met the primary outcome. … 48 (17%) and 23 (8%) missed cases at 15 and 60 min" (Abstract)
- **SAM relevance:** Quantifies the ED-sepsis miss window that Andy can shrink with auto-rescue from abnormal labs; the 17%→8% lab-driven recovery is exactly Andy's mechanism.

### 08 — Vaghani 2025 — E-triggers to identify diagnostic errors in EDs

- **Source:** `08_Vaghani2025_etriggers-ED.pdf`
- **Citation:** Vaghani V, Gupta A, Mir U, et al. Implementation of Electronic Triggers to Identify Diagnostic Errors in Emergency Departments. JAMA Intern Med. 2025;185(2):143–151. doi:10.1001/jamainternmed.2024.6214.
- **Design / N:** Retrospective medical record review across 1,321 VA sites; e-triggers applied to 8.79M (stroke) + 3.69M (symptom-disease) + 1.85M (other) ED visits; 625 records reviewed.
- **Key numbers:**
  - MOD (missed opportunity in dx) PPV: stroke 47.0%, abdominal pain 25.8%, ED return 11.0%, hospital return 23.0%, symptom-disease dyads 18.0%, test results 52.4%.
  - Of 185 total MODs: 10.8% severe harm, 29.2% moderate harm.
  - 83.1% of MODs (excluding test-result trigger) involved patient–clinician encounter breakdown.
- **Headline quote:** "20 patients experienced severe harm (10.8%), and 54 patients experienced moderate harm (29.2%)." (Abstract)
- **SAM relevance:** Validates e-trigger paradigm (Andy's core architecture) at national VA scale; PPVs justify trigger-driven workflows; harm rates support per-trigger value pricing.

### 09 — Newman-Toker 2019 — Serious misdiagnosis-related harms in malpractice claims: The Big Three

- **Source:** `09_NewmanToker2019_big-three.pdf`
- **Citation:** Newman-Toker DE, Schaffer AC, Yu-Moe CW, et al. Serious misdiagnosis-related harms in malpractice claims: The "Big Three" — vascular events, infections, and cancers. Diagnosis. 2019;6(3):227–240. doi:10.1515/dx-2019-0019.
- **Design / N:** Cross-sectional analysis of CRICO CBS malpractice database (2006–2015), representing 28.7% of US malpractice claims; 11,592 dx-error cases.
- **Key numbers:**
  - 7,379 high-severity harm cases (53.0% death).
  - Big Three = 74.1% of high-severity dx-error harms (vascular 22.8%, infections 13.5%, cancers 37.8%).
  - Top 15 diseases = 47.1% of high-severity cases.
  - Most frequent in each: stroke, sepsis, lung cancer.
  - Clinical judgment factors = 85.7% of causes (range 82.0–88.8%).
- **Headline quote:** "The Big Three diseases accounted for 74.1% of high-severity cases" (Abstract)
- **SAM relevance:** Tells Andy to focus product surface on ~15 diseases to cover ~half of serious harms; supports a tractable initial scope.

### 10 — Saber Tehrani 2013 — 25-yr US malpractice claims for dx errors (stub)

- **Source:** `10_SaberTehrani2013_25yr-malpractice.md`
- **Citation:** Saber Tehrani AS, Lee H, Mathews SC, et al. 25-Year summary of US malpractice claims for diagnostic errors 1986-2010: an analysis from the National Practitioner Data Bank. BMJ Qual Saf. 2013;22(8):672–680. doi:10.1136/bmjqs-2012-001550.
- **Design / N:** Analysis of 350,706 paid US malpractice claims, NPDB, 1986–2010.
- **Key numbers:**
  - Dx errors = 28.6% of paid claims (n=100,249), leading category.
  - Dx errors = 35.2% of total payments.
  - 40.9% of dx-error claims resulted in death vs 23.9% other (p<0.001).
  - $38.8B inflation-adjusted payouts over 25 years; mean $386,849; median $213,250 (IQR $74,545–$484,500).
- **Headline quote:** "Diagnostic errors … were the leading type (28.6%) and accounted for … 35.2% of total payments" (Abstract; stub).
- **SAM relevance:** Liability cost anchor for Andy's payer/health-system ROI story. Stub-derived only — verify against full text before citing.

### 11 — Newman-Toker 2009 — Diagnostic Errors: The Next Frontier for Patient Safety

- **Source:** `11_NewmanToker2009_next-frontier.pdf`
- **Citation:** Newman-Toker DE, Pronovost PJ. Diagnostic Errors—The Next Frontier for Patient Safety. JAMA. 2009;301(10):1060–1062. doi:10.1001/jama.2009.249.
- **Design / N:** Commentary / framework paper.
- **Key numbers:**
  - 40,000–80,000 US hospital deaths/year from misdiagnosis.
  - ~5% of autopsies reveal lethal dx errors where correct dx + treatment could have averted death.
  - Harvard Medical Practice Study: dx errors more common than drug errors (14% vs 9%); more often deemed negligent (75% vs 53%); more often cause serious disability (47% vs 14%).
  - Dx-error tort claims ≈ 2× medication-error claims and largest payouts.
- **Headline quote:** "An estimated 40,000 to 80,000 US hospital deaths result from misdiagnosis annually." (p.1060)
- **SAM relevance:** Foundational citation establishing dx error as the dominant — and previously neglected — patient-safety priority; sets the historical context for Andy's category.

### 12 — Newman-Toker 2022/2023 — AHRQ Systematic Review: Dx Errors in the Emergency Department

- **Source:** `12_NewmanToker2022_AHRQ-ED-systematic-review.pdf`
- **Citation:** Newman-Toker DE, Peterson SM, Badihian S, et al. Diagnostic Errors in the Emergency Department: A Systematic Review. AHRQ Comparative Effectiveness Review No. 258. AHRQ Pub. No. 22(23)-EHC043. Dec 2022 (Errata Aug 2023).
- **Design / N:** Systematic review across ED studies; extrapolation to all US ED visits.
- **Key numbers:**
  - 5.7% of ED visits have ≥1 dx error (95% CI 4.4–7.1).
  - Adverse events from dx error: 2.0% (95% CI 1.0–3.6); serious harms 0.3% (PR 0.1–0.7).
  - With 130M US ED visits/yr: ~7.4M dx errors (PR 5.1–10.2M), ~2.6M dx adverse events (PR 1.1–5.2M), ~371,000 serious harms (PR 142K–909K) including >100K permanent disabilities + 250,000 deaths.
  - Per average ED (25,000 visits/yr): ~1,400 dx errors, 500 adverse events, 75 serious harms, 50 deaths.
  - 15 diseases drive >2/3 of serious harms; 89% multifactorial with cognitive errors dominant.
- **Headline quote:** "7.4 million (5.7%) patients are misdiagnosed … about 370,000 (0.3%) suffer serious harms" (Exec Summary)
- **SAM relevance:** Defines per-ED Andy ROI: ~1,400 errors and 50 deaths preventable per 25k-visit ED; national ED TAM ~7.4M misdiagnoses/yr.

### 13 — Hautz 2019 — Diagnostic error increases mortality and LOS in ED patients

- **Source:** `13_Hautz2019_dx-error-mortality-LOS.pdf`
- **Citation:** Hautz WE, Kämmer JE, Hautz SC, et al. Diagnostic error increases mortality and length of hospital stay in patients presenting through the emergency room. Scand J Trauma Resusc Emerg Med. 2019;27:54. doi:10.1186/s13049-019-0629-z.
- **Design / N:** Prospective observational cohort, n=755 consecutive ED-admitted patients, single tertiary-care center.
- **Key numbers:**
  - Discharge dx differed substantially from admission dx in 12.3% of cases.
  - LOS: 10.29 vs 6.90 days with discrepancy (Cohen's d 0.47; 95% CI 0.26–0.70; P=0.002).
  - In-hospital mortality 8.60% vs 3.78% (OR 2.40; 95% CI 1.05–5.5; P=0.038).
  - Atypical presentation predicted discrepancy (OR 3.04; 95% CI 1.33–6.96).
- **Headline quote:** "discharge diagnosis differed substantially from the admittance diagnosis in 12.3% of cases" (Abstract)
- **SAM relevance:** Direct LOS + mortality dollar-cost levers for Andy's hospital ROI pitch (excess ~3.4 days LOS and ~2.3× mortality OR per missed dx).

### 14 — Esposito 2024 — Recognition patterns of AKI in hospitalized patients

- **Source:** `14_Esposito2024_AKI-recognition-patterns.pdf`
- **Citation:** Esposito P, Cappadona F, Marengo M, et al. Recognition patterns of acute kidney injury in hospitalized patients. Clin Kidney J. 2024;17(8):sfae231. doi:10.1093/ckj/sfae231.
- **Design / N:** Retrospective administrative + lab cohort, n=56,820 adult hospital admissions (Italy).
- **Key numbers:**
  - Overall AKI incidence: 24.5%.
  - 9,498 (16.7%) had undetected/KDIGO-AKI (creatinine criteria positive, not coded).
  - 1,893 (3.3%) full-AKI (coded + sCr); 2,529 (4.4%) HDF-AKI (coded only).
  - 68% AKI under-detection rate overall.
  - All AKI groups had worse outcomes than no-AKI; undetected AKI independently associated with mortality.
- **Headline quote:** "AKI incidence was 24.5%, with a 68% undetection rate." (Abstract)
- **SAM relevance:** AKI is one of Andy's flagship never-detected dx targets — 68% miss rate at scale establishes massive per-hospital opportunity.

### 15 — Wu 2025 — Unexpectedly high rate of unrecognized AKI (14-yr trend)

- **Source:** `15_Wu2025_unrecognized-AKI.pdf`
- **Citation:** Han L, Li H, Luo L, et al. Unexpectedly high rate of unrecognized acute kidney injury and its trend over the past 14 years. Sci Rep. 2025;15:6305. doi:10.1038/s41598-025-88732-8.
- **Design / N:** Retrospective cohort, n=2,790,540 patients, large Chinese public hospital, 2010–2023; 5,080 met AKI criteria.
- **Key numbers:**
  - AKI incidence: 0.18% overall (0.78% inpatient, 0.05% outpatient).
  - Unrecognized AKI rate: 76.3% (75% stage 1, 16.7% stage 2, 8.3% stage 3).
  - Highest unrecognition: orthopedics 94.5%; lowest: ICU 55.77%.
  - Improvement over time: 90.3% (2010–2011) → 70.2% (2022–2023).
  - Recognized vs unrecognized recovery: 8.0 vs 9.0 days (p<0.001).
  - Only 26% of AKI patients receive follow-up within 6 months post-discharge.
- **Headline quote:** "The unrecognized AKI was 76.3%." (Abstract)
- **SAM relevance:** International confirmation that AKI miss rates persist at ~70–76% even with improving trend; supports AKI as durable global target for Andy.

### 16 — Greci 2003 — HbA1c case-finding for diabetes in hospitalized hyperglycemic patients (stub)

- **Source:** `16_Greci2003_HbA1c-case-finding.md`
- **Citation:** Greci LS, Kailasam M, Malkani S, et al. Utility of HbA(1c) levels for diabetes case finding in hospitalized patients with hyperglycemia. Diabetes Care. 2003;26(4):1064–1068. doi:10.2337/diacare.26.4.1064.
- **Design / N:** Prospective case-finding, 508 ED admissions screened, 35 eligible hyperglycemic patients without prior dx.
- **Key numbers:**
  - 21/35 hyperglycemic inpatients without prior dx ultimately diagnosed with diabetes (60%).
  - HbA1c >6.0% = 100% specific (14/14), 57% sensitive (12/21).
  - HbA1c <5.2% effectively excludes diabetes.
- **Headline quote:** "An HbA1c threshold of >6.0% demonstrated 100% specific … and 57% sensitive" (Abstract; stub)
- **SAM relevance:** Foundational evidence that routine labs already reveal undiagnosed diabetes inpatient — proof-of-concept for Andy's lab-mining mechanism. Stub-derived only — verify against full text before citing.

### 17 — Ferris 2009 — High prevalence of unlabeled CKD among inpatients (stub)

- **Source:** `17_Ferris2009_unlabeled-CKD.md`
- **Citation:** Ferris M, Shoham DA, Pierre-Louis M, et al. High prevalence of unlabeled chronic kidney disease among inpatients at a tertiary-care hospital. Am J Med Sci. 2009;337(2):93–97. doi:10.1097/MAJ.0b013e318181288e.
- **Design / N:** Retrospective EHR review, n=9,772 inpatients with sufficient data, NC tertiary-care, 2000–2005.
- **Key numbers:**
  - 431 patients with stage 5 CKD; 6,851 with stage 2–4 CKD.
  - 2,176 (72.5%) of lab-defined CKD patients NOT coded as CKD by ICD-9.
- **Headline quote:** "the number of patients not labeled as having CKD by ICD-9 code was 2,176 (72.5%)." (Abstract; stub)
- **SAM relevance:** Quantifies inpatient under-coding gap for CKD — pure Andy use case. Stub-derived only — verify against full text before citing.

### 18 — Stein 1991 PIOPED — Clinical features of acute PE (stub)

- **Source:** `18_Stein1991_PIOPED.md`
- **Citation:** Stein PD, Terrin ML, Hales CA, et al. Clinical, laboratory, roentgenographic, and electrocardiographic findings in patients with acute pulmonary embolism and no pre-existing cardiac or pulmonary disease. Chest. 1991;100(3):598–603. doi:10.1378/chest.100.3.598. (Also Stein PD, Henry JW. Prevalence of acute PE in a general hospital and at autopsy. Chest. 1995;108(4):978–981.)
- **Design / N:** PIOPED clinical-features cohort (angiographically confirmed PE); 1995 companion: 51,645 hospitalized patients.
- **Key numbers:**
  - 1991 paper: symptom base rates for PE without prior cardiopulmonary disease (dyspnea, pleuritic CP, tachypnea) — not reported in stub.
  - 1995 paper: PE prevalence in hospitalized patients 1.0% (526/51,645; 95% CI 0.9–1.1%).
- **Headline quote:** "Estimated prevalence of acute PE in hospitalized patients was 526 of 51,645 (1.0%…)" (Stub, 1995 paper)
- **SAM relevance:** PE is the canonical leading missed inpatient dx (see #04); base-rate anchor for PE-detection module. Stub-derived only — verify against full text before citing.

### 19 — Gil-Millán 2025 (DIABET-IC) — HFpEF underrecognition in T2D

- **Source:** `19_DIABETIC2025_HFpEF-T2DM.pdf`
- **Citation:** Gil-Millán P, Gimeno-Orna JA, Rodríguez-Padial L, et al. HFpEF as the predominant and underrecognized heart failure phenotype in type 2 diabetes: evidence from the DIABETIC study. Cardiovasc Diabetol. 2025;24:419. doi:10.1186/s12933-025-02995-z.
- **Design / N:** Prospective nationwide DIABET-IC subanalysis, 1,517 T2D patients, 58 Spanish centers, 3-yr follow-up.
- **Key numbers:**
  - 490/1,517 T2D patients had HF at baseline (~32%): HFrEF 50.2%, HFpEF 30.6%, HFmrEF 19.2%.
  - HFpEF = 46.6% of new incident HF cases during follow-up.
  - 4.7% HFpEF progressed to HFrEF.
  - >20% of HFpEF patients had natriuretic peptide levels below diagnostic thresholds (underdiagnosis flag).
- **Headline quote:** "> 20% of HFpEF patients had natriuretic peptide levels below diagnostic thresholds" (Abstract)
- **SAM relevance:** HFpEF in T2D is a high-volume, high-comorbidity Andy target — labs+echo data exist but underdiagnosed.

### 20 — Roten 2021 (STAR-FIB) — AF prevalence (clinical + screen-detected) in hospitalized patients

- **Source:** `20_STARFIB2021_AF-hospitalized.pdf`
- **Citation:** Roten L, Goulouti E, Lam A, et al. Age and Sex Specific Prevalence of Clinical and Screen-Detected Atrial Fibrillation in Hospitalized Patients. J Clin Med. 2021;10:4871. doi:10.3390/jcm10214871.
- **Design / N:** Prospective cohort, hospitalized patients 65–84, source population ~26,035; 795 enrolled, 3× 7-day Holter monitoring.
- **Key numbers:**
  - Clinical AF prevalence: 22.2% (95% CI 18.4–26.1) in source pop; 23.8% males / 19.8% females.
  - Screen-detected AF (cohort): 4.9% overall (95% CI 3.3–6.6); 5.5% M, 4.0% F.
  - Source-population screen-detected AF: 3.8% (4.2% M, 3.2% F).
  - 38 newly diagnosed AF cases in cohort of 795.
- **Headline quote:** "prevalence of clinical AF and of screen-detected AF was 22.2% and 3.8%, respectively" (Abstract)
- **SAM relevance:** Quantifies addressable previously-undiagnosed AF in hospitalized older adults (~3.8%) — direct Andy detection target with anticoagulation downstream value.

### 21 — Naser 2024 — HFpEF underdiagnosis in isolated severe secondary tricuspid regurgitation

- **Source:** `21_Naser2024_TR-HFpEF.pdf`
- **Citation:** Naser JA, Harada T, Reddy YN, et al. Prevalence of HFpEF in Isolated Severe Secondary Tricuspid Regurgitation. JAMA Cardiol. 2025;10(2):182–187. doi:10.1001/jamacardio.2024.3767.
- **Design / N:** Retrospective cross-sectional, n=54 adults with severe isolated STR undergoing exercise RHC at Mayo Clinic, 2006–2023.
- **Key numbers:**
  - HFpEF identified in 40/54 (74%); recognized prior to RHC in only 19/40 (35%).
  - Of 14 without HFpEF, precapillary PH in 10 (71%).
  - Guideline-defined diastolic dysfunction absent in 24/40 (60%) of HFpEF cases.
  - LA emptying fraction AUC 0.90; LA strain AUC 0.91 for HFpEF detection.
- **Headline quote:** "HFpEF was identified in 40 patients (74%) but was recognized prior to RHC in only 19 patients (35%)." (Abstract)
- **SAM relevance:** 65% pre-referral miss rate for HFpEF in a cardiology-rich subspecialty cohort — proves under-recognition persists even at academic centers; Andy can prompt earlier workup.

### 22 — Dolan 2025 — Uncoded CKD prevalence in UK secondary care

- **Source:** `22_UKCKD2025_uncoded-CKD.pdf`
- **Citation:** Dolan S, Anand A, Kalra PA, Stewart S. Uncoded chronic kidney disease prevalence in secondary care: a retrospective audit with population health implications. BMC Nephrol. 2025;26:39. doi:10.1186/s12882-025-03967-x.
- **Design / N:** Retrospective audit, acute medical ward, England, Apr 2022–Feb 2023.
- **Key numbers:**
  - Uncoded CKD prevalence (by discharge eGFR): 58.7% (n=283).
  - 1.1 uncoded CKD cases per bed/month; 13.7 per bed/year.
  - Conversion of uncoded → coded at discharge: only 6.7%.
  - ~1 million estimated undiagnosed CKD patients in England (background).
- **Headline quote:** "Uncoded CKD prevalence using discharge estimated GFR (eGFR) was 58.7%" (Abstract)
- **SAM relevance:** Direct per-bed/year volume metric (13.7) usable in Andy ROI modeling per hospital; reinforces CKD as scalable coding-gap product.

### 24 — Gwira 2024 (NCHS) — Total, Diagnosed, and Undiagnosed Diabetes in US Adults

- **Source:** `24_Gwira2024_NCHS-diabetes.pdf`
- **Citation:** Gwira JA, Fryar CD, Gu Q. Prevalence of Total, Diagnosed, and Undiagnosed Diabetes in Adults: United States, August 2021–August 2023. NCHS Data Brief No. 516. Nov 2024.
- **Design / N:** NHANES cross-sectional survey, US adults age ≥20, Aug 2021–Aug 2023.
- **Key numbers:**
  - Total diabetes prevalence: 15.8% of US adults.
  - Diagnosed diabetes: 11.3%; undiagnosed: 4.5%.
  - Men: total 18.0%, undiagnosed 5.1%; Women: total 13.7%, diagnosed 9.7%.
  - Prevalence increased with age and weight; total/dx prevalence has risen since 1999–2000.
- **Headline quote:** "the prevalence of total diabetes was 15.8%, diagnosed diabetes was 11.3%, and undiagnosed diabetes was 4.5%" (Key findings)
- **SAM relevance:** Outpatient diabetes undiagnosed pool = 4.5% of US adults (~12M people) — direct TAM anchor for Andy's ambulatory undiagnosed-chronic-disease product.

### 25 — NIDDK — Kidney Disease Statistics for the United States

- **Source:** `25_NIDDK_kidney-disease-stats.pdf`
- **Citation:** National Kidney and Urologic Diseases Information Clearinghouse (NIDDK). Kidney Disease Statistics for the United States. (USRDS 2010/2011 Annual Data Reports.)
- **Design / N:** Federal statistical compendium, US population.
- **Key numbers:**
  - "1 in 10 American adults, more than 20 million, have some level of CKD." (CDC source)
  - CKD incidence rising fastest in age ≥65 (recognized CKD in ≥65 more than doubled between 2000 and later years per stat brief).
- **Headline quote:** "One in 10 American adults, more than 20 million, have some level of CKD." (p.1)
- **SAM relevance:** US CKD denominator (>20M) — pairs with #17/#22 under-coding rates to size Andy's CKD opportunity nationally.

### 26 — Jones 2014 — Missed opportunities to diagnose COPD in UK routine care

- **Source:** `26_Jones2014_COPD-routine-care.pdf`
- **Citation:** Jones RCM, Price D, Ryan D, et al. Opportunities to diagnose chronic obstructive pulmonary disease in routine care in the UK: a retrospective study of a clinical cohort. Lancet Respir Med. 2014;2:267–276. doi:10.1016/S2213-2600(14)70008-6.
- **Design / N:** Retrospective UK primary care cohort, n=38,859 COPD patients (GPRD + OPCRD), 1990–2009.
- **Key numbers:**
  - Missed opportunities in 32,900/38,859 (85%) of patients in the 5 yrs immediately preceding dx.
  - 58% in yrs 6–10; 42% in yrs 11–15; 8% in yrs 16–20 prior to dx.
  - 835,000 diagnosed UK COPD patients vs estimated 2.2M living with undiagnosed COPD.
  - Of 6,897 patients with chest x-ray in the 2 yrs pre-dx, only 33% (2,296) also had spirometry.
  - Estimated >£1B/10yr UK NHS savings from earlier dx.
- **Headline quote:** "Opportunities for diagnosis were missed in 32,900 (85%) of 38,859 patients in the 5 years immediately preceding diagnosis" (Findings)
- **SAM relevance:** Quantifies the chronic-disease "data already in chart" miss pattern at scale — Andy's exact bull's-eye in PCP workflows.

### 27 — Turakhia 2018 — Estimated prevalence of undiagnosed AF in the US

- **Source:** `27_Turakhia2018_undiagnosed-AF-US.pdf`
- **Citation:** Turakhia MP, Shafrin J, Bognar K, et al. Estimated prevalence of undiagnosed atrial fibrillation in the United States. PLoS ONE. 2018;13(4):e0195088. doi:10.1371/journal.pone.0195088.
- **Design / N:** Retrospective back-calculation modeling, Optum + CMS Medicare claims, 2004–2010.
- **Key numbers:**
  - Total AF prevalence (diag + undiag): 5.3M Americans in 2009.
  - Undiagnosed AF: 698,900 total (13.1% of all AF cases).
  - Elderly: 535,400 undiagnosed (1.3% of ≥65 population).
  - Working age: 163,500 undiagnosed (0.09%).
  - 77% of undiagnosed had CHADS2 ≥1; 56% had CHADS2 ≥2 (moderate-high stroke risk).
- **Headline quote:** "total AF prevalence in 2009 was 5.3 million of which 0.7 million (13.1% of AF cases) were undiagnosed" (Conclusions)
- **SAM relevance:** ~700K Americans with undiagnosed AF at stroke risk = direct US ambulatory TAM for Andy's AF/stroke-prevention module.

### 28 — Ciemins 2018 (MMWR) — Undiagnosed Hypertension in US Ambulatory Practice

- **Source:** `28_Ciemins2018_MMWR-undiagnosed-HTN.pdf`
- **Citation:** Ciemins EL, Ritchey MD, Joshi VV, Loustalot F, Hannan J, Cuddeback JK. Application of a Tool to Identify Undiagnosed Hypertension — United States, 2016. MMWR Morb Mortal Wkly Rep. 2018;67(29):798–802.
- **Design / N:** Cross-sectional analysis of 8.92M adults across 25 AMGA/Optum One health systems, 2016.
- **Key numbers:**
  - ~11 million US adults with usual source of care have undiagnosed hypertension.
  - Using billing data alone: up to 1 in 8 HTN cases may be undiagnosed.
  - Sample size: 8.92M patients aged 18–85; payer mix 51% commercial / 36% Medicare / 5% Medicaid.
- **Headline quote:** "Approximately 11 million U.S. adults with a usual source of health care have undiagnosed hypertension" (p.798)
- **SAM relevance:** Defines US ambulatory HTN under-dx TAM (11M adults) — high-volume, low-cost detection that Andy can trigger from BP + labs in EHR.




---

## Section B — AI/LLM detection, AKI alert RCTs, cost economics (#29–#46)

# Findings — Section B (Papers #29-#46)

Extracted: 2026-05-24. Source-of-truth notes for Andy TAM/SAM modeling.
Numbers verbatim from abstracts/intros unless otherwise noted. Stub-derived entries flagged.

---

### 29 — Sarvari 2024 — GPT-4 vs PaLM2 diagnosing comorbidities in MIMIC-IV

- **Source:** `29_Sarvari2024_GPT4-PaLM2-MIMIC.pdf`
- **Citation:** Sarvari P, Al-fagih Z, Ghuwel A, Al-fagih O. A systematic evaluation of the performance of GPT-4 and PaLM2 to diagnose comorbidities in MIMIC-IV patients. Health Care Sci. 2024;3:3-18. doi:10.1002/hcs2.79.
- **Design / N:** Retrospective evaluation on 1,000 randomly sampled MIMIC-IV ICU patients (from ~300k pool at BIDMC); LLM prompted with structured EHR text, compared to physician-curated ground-truth diagnoses.
- **Key numbers:**
  - GPT-4 diagnostic hit rate: 93.9% on n=1,000 MIMIC-IV
  - PaLM2 hit rate: 84.7% on same set
  - GPT-4 correctly identified 1,116 unique diagnoses across 1,000 EHRs
  - Cost per case: not reported in abstract
- **Headline quote:** "we estimated the diagnostic hit rate of GPT-4 to be 93.9%" (p.3)
- **SAM relevance:** Anchors the upper-bound LLM recall ceiling on real ICU EHR data. Supports Andy's claim that a frontier LLM can recover ≥9 of 10 documented dx — feeds the "addressable missed-dx fraction LLMs can recover" assumption.

---

### 30 — Haimovich 2025 — Sequential eTrigger + LLM for ED missed dx

- **Source:** `30_Haimovich2025_etrigger-LLM-screening.pdf`
- **Citation:** Marks C, …, Rodman A, Haimovich AD. Scalable screening for emergency department missed opportunities for diagnosis using sequential eTriggers and large language models. medRxiv 2025.10.06.25337201; posted 2025-10-07.
- **Design / N:** Retrospective cohort, 10 EDs (2 academic, 8 community), single US health system. 357 encounters reviewed; sequential eTrigger + Claude Sonnet 4 adjudication using SaferDX.
- **Key numbers:**
  - Traditional eTrigger MOD PPV: 11.0%–18.6% across triggers
  - 72-hr return: LLM sensitivity 85.7% (95% CI 65.4-95.0), specificity 56.8%, PPV 19.8%, NPV 97.0%
  - 10-day ICU return: sensitivity 100% (95% CI 56.6-100), NPV 100%
  - Floor-to-ICU within 24h: sensitivity 55.6%, NPV 86.4%
  - Hybrid ECSC 9-day eTrigger: 110 MODs in 207 encounters (53.1%); blinded sample PPV 45%, NPV 100%
  - Reviewer time: median 5 min/case; LLM-positive-only review cut time by up to 50%
  - Stakeholder rating: clinician feedback actionability 4.1/5, systems-level 1.4/5
- **Headline quote:** "LLM-augmented eTrigger screening offers scalable, efficient MOD detection" (Key Points, p.4)
- **SAM relevance:** Direct precedent for Andy ED-workflow: shows LLM second-pass on eTriggers cuts QI review burden ~50% with near-100% NPV. Validates an entry-wedge for diagnostic-quality oversight in EDs.

---

### 31 — Hager 2024 — Limitations of LLMs in real clinical decision-making

- **Source:** `31_Hager2024_LLM-clinical-limitations.pdf`
- **Citation:** Hager P, Jungmann F, Holland R, et al. Evaluation and mitigation of the limitations of large language models in clinical decision-making. Nat Med. 2024;30:2613-2622. doi:10.1038/s41591-024-03097-1.
- **Design / N:** MIMIC-IV-Ext Clinical Decision Making dataset; 2,400 real ED abdominal-pain patients across 4 pathologies (appendicitis, pancreatitis, cholecystitis, diverticulitis). Reader study: 80-patient subset compared to 4 hospitalists. Tested Llama-2-70B, OASST, WizardLM, Clinical Camel, Meditron (no GPT-4 due to MIMIC data-use terms).
- **Key numbers:**
  - LLMs significantly worse than clinicians (all p<0.001)
  - Gap in mean diagnostic accuracy: 16–25 percentage points below physicians
  - German resident hospitalists mean 87.5% ± 3.7%; senior US hospitalist 92.5%
  - Models fail to follow diagnostic/treatment guidelines and mis-interpret labs
  - Cost per case: not reported in abstract
- **Headline quote:** "LLMs are currently not ready for autonomous clinical decision-making" (abstract)
- **SAM relevance:** Strong evidence Andy must be positioned as copilot, not autonomous. Bounds the value prop: LLMs need human-in-loop and guideline scaffolding — exactly what Andy provides.

---

### 32 — Pi/McInerney 2024 — Interpretable risk prediction with LLMs on EHR notes

- **Source:** `32_Pi2024_truncated-charts-LLM.pdf`
- **Citation:** McInerney DJ, Dickinson W, Flynn LC, Young AC, Young GS, van de Meent J-W, Wallace BC. Towards Reducing Diagnostic Errors with Interpretable Risk Prediction. arXiv:2402.10109v2, 2024-03-19.
- **Design / N:** Method paper. Combines FLAN-T5-XXL evidence extraction with Clinical BERT + Neural Additive Model on longitudinal EHR notes; simulates clinician differential-diagnosis use.
- **Key numbers:**
  - Cites Newman-Toker 795,000 serious harms/year baseline
  - Specific accuracy/F1: not reported in extracted abstract (method-focused paper)
  - "Note bloat" framed as causal driver of dx error
- **Headline quote:** "many diagnostic errors result from information transfer problems" (p.1)
- **SAM relevance:** Validates the technical thesis behind Andy — interpretable evidence surfacing from EHR notes is a tractable, peer-reviewed direction. Useful as a design-pattern citation, not a performance benchmark.

---

### 33 — Albassam 2025 — Majority-voting LLM for unknown dx from notes

- **Source:** `33_Albassam2025_LLM-unknown-dx.pdf`
- **Citation:** Albassam D, Cross A, Zhai C. Leveraging LLMs for Predicting Unknown Diagnoses from Clinical Notes. (Pre-print, 2025.)
- **Design / N:** 240 expert-annotated medication-diagnosis pairs from 20 MIMIC-IV notes; GPT-3.5 Turbo; 18 configurations × random subsets of 5 → 8,568 test cases with majority voting.
- **Key numbers:**
  - Majority voting accuracy: 75%
  - Best single-model configuration: 66%
  - Shorter 2,000-token summaries generally improved accuracy vs 4,000-token
- **Headline quote:** "majority voting achieved 75% accuracy, outperforming the best single configuration (66%)" (abstract)
- **SAM relevance:** Quantifies ensemble lift (+9 pp) — supports an architectural pattern Andy could adopt. Cite as evidence that simple ensembling materially improves medication-dx linkage accuracy.

---

### 34 — Hassoon 2026 — 16 LLMs as diagnostic safety net

- **Source:** `34_Hassoon2026_16-LLMs-safety-net.pdf`
- **Citation:** Hassoon A, Peng X, Irimia R, et al. (incl. Newman-Toker D). Evaluating the AI Potential as a Safety Net for Diagnosis: A Novel Benchmark of Large Language Models in Correcting Diagnostic Errors. medRxiv 2026.02.22.26346832; posted 2026-02-24.
- **Design / N:** 200 standardized vignettes × 20 high-stakes frequently misdiagnosed conditions; 16 LLMs (GPT-o1, Gemini 2.5 Pro, Claude 3.7 Sonnet, etc.); 2,200 demographic/contextual variants for robustness.
- **Key numbers:**
  - Gemini 2.5 Pro correction rate: 55.0% (110/200) — top performer
  - Claude Sonnet 3.5: 48.5%; Sonnet 4: 47.0%
  - DeepSeek V3: 20.0% (worst)
  - Confirmation bias (agreeing with the wrong dx): 11.0%–50.0% of cases across models
  - Persistent failures across models: syphilis, spinal epidural abscess, MI
- **Headline quote:** "top-performing LLMs can intercept approximately half of the human diagnostic errors" (abstract)
- **SAM relevance:** Best directly-relevant benchmark for Andy's core promise (catching physician misdx). Caps realistic miss-recovery at ~50%, supporting conservative SAM assumptions and the need for adversarial, multi-agent workflows.

---

### 35 — Boussina 2025 — COMPOSER-LLM early sepsis prediction

- **Source:** `35_Boussina2025_COMPOSER-LLM.pdf`
- **Citation:** Shashikumar SP, Mohammadi S, Krishnamoorthy R, et al. Development and Prospective Implementation of a Large Language Model based System for Early Sepsis Prediction. medRxiv 2025.03.07.25323589; posted 2025-03-11.
- **Design / N:** UC San Diego. 2,500-encounter retrospective + prospective validation. Open-source LLM augments COMPOSER structured-data model on high-uncertainty cases.
- **Key numbers:**
  - Sensitivity 72.1%
  - PPV 52.9%, F1 0.610
  - False alarms: 0.0087 per patient-hour
  - 62% of false positives had bacterial infections on manual review
  - Outperformed standalone COMPOSER
- **Headline quote:** "integrating LLMs with traditional models can enhance predictive performance" (abstract)
- **SAM relevance:** Concrete deployed-model exemplar for LLM-augmented sepsis detection. Anchors plausible PPV (~50%) for triggered alerts — useful for Andy alert-fatigue economics.

---

### 36 — Sun (Yang) 2025 — LLMs for psychiatric dx, multicenter EHR

- **Source:** `36_Yang2025_psychiatric-LLM.pdf`
- **Citation:** Sun M, Yu J, Long Z, et al. (corresponding: Huang G). Large Language Models for Psychiatric Diagnosis Based on Multicenter Real-World Clinical Records: Comparative Study. JMIR Med Inform 2026;14:e77699. doi:10.2196/77699.
- **Design / N:** 9,923 inpatient EHRs across 6 psychiatric centers in China; all ICD-10 psychiatric categories; GPT-4.0, GPT-3.5, GLM-4-Plus vs physician-confirmed discharge dx.
- **Key numbers:**
  - GPT-4.0 strict accuracy: 71.7% overall
  - GPT-4.0 weighted F1 (lenient): 0.881
  - Older adults: up to 79.5% accuracy; lower in adolescents
  - High-prevalence disorders (mood, schizophrenia spectrum) best performance
- **Headline quote:** "GPT-4.0 achieved the highest overall strict diagnostic accuracy (71.7%)" (abstract)
- **SAM relevance:** Demonstrates LLM dx accuracy across an entire ICD chapter (psychiatry) at scale. Supports SAM extension into specialty inpatient settings beyond ED/ICU; flags age-stratified performance gaps to surface in product positioning.

---

### 37 — Buhr / Sarvari 2025 — 21 LLMs benchmarked on MIMIC-IV

- **Source:** `37_Buhr2025_21LLMs-MIMIC.pdf`
- **Citation:** Sarvari P, Al-fagih Z. Rapidly Benchmarking Large Language Models for Diagnosing Comorbid Patients: Comparative Study Leveraging the LLM-as-a-Judge Method. JMIRx Med 2025;6:e67661. doi:10.2196/67661.
- **Design / N:** 21 LLMs (Google/OpenAI/Meta/Mistral/Cohere/Anthropic), 3 prompts × 2 temperatures, 1,000 random MIMIC-IV admissions; LLM-as-a-judge evaluation; RAG variant on GPT-4o.
- **Key numbers:**
  - Gemini 2.5: hit rate 97.4% (95% CI 97.0-97.8), top performer (judged by GPT-4.1)
  - GPT-4.1 top under GPT-4-Turbo judging
  - RAG improved GPT-4o (05-13) by +0.8% (p<.006)
  - Significant prompt variation; temperature ~no effect
- **Headline quote:** "Gemini 2.5 was the top performer with a hit rate of 97.4%" (abstract)
- **SAM relevance:** Updated frontier benchmark — supports the "modern LLMs recover ≥95% of documented dx on ICU charts" assumption underpinning Andy's recall ceiling. Validates RAG modestly helps; prompt engineering is the bigger lever.

---

### 38 — Google AMIE 2025 — Conversational diagnostic AI vs PCPs

- **Source:** `38_GoogleAMIE2025_conversational-ddx.pdf`
- **Citation:** Tu T, Schaekermann M, Palepu A, et al. Towards conversational diagnostic artificial intelligence. Nature 2025;642:442-…. doi:10.1038/s41586-025-08866-7. Published 2025-04-09.
- **Design / N:** Randomized, double-blind crossover OSCE-style study. 159 case scenarios (Canada/UK/India); 20 PCPs vs AMIE in text-based consultations with validated patient-actors; specialist + patient-actor evaluations.
- **Key numbers:**
  - AMIE outperformed PCPs on 30/32 specialist-rated axes and 25/26 patient-actor axes
  - Superior diagnostic accuracy (specific deltas in body, not abstract)
  - Modality: synchronous text chat
- **Headline quote:** "AMIE demonstrated greater diagnostic accuracy and superior performance" (abstract)
- **SAM relevance:** Strongest published head-to-head showing an LLM dx system can match or exceed PCPs in OSCE-style encounters. Used to justify primary-care SAM expansion thesis — though the unfamiliar text-chat modality caveats apply.

---

### 39 — Wilson 2021 — AKI EHR alert RCT (Yale-New Haven, 6 hospitals)

- **Source:** `39_Wilson2021_AKI-alert-RCT.pdf`
- **Citation:** Wilson FP, Martin M, Yamamoto Y, et al. Electronic health record alerts for acute kidney injury: multicenter, randomized clinical trial. BMJ 2021;372:m4786. doi:10.1136/bmj.m4786.
- **Design / N:** Double-blind, multicenter parallel RCT. 6,030 adult inpatients with KDIGO-defined AKI across 6 hospitals (4 teaching, 2 non-teaching), Yale-New Haven, CT/RI.
- **Key numbers:**
  - Primary composite (AKI progression/dialysis/death @14d): 21.3% alert vs 20.9% usual care (RR 1.02, 95% CI 0.93-1.13, p=0.67) — null
  - Non-teaching hospitals (n=765, 13%): RR 1.49 (95% CI 1.12-1.98, p=0.006) — worse with alerts
  - Non-teaching mortality: 15.6% alert vs 8.6% usual care (p=0.003)
  - Background: AKI in ~15% inpatients, documented in <50% of cases
- **Headline quote:** "Alerts did not reduce the risk of our primary outcome" (abstract)
- **SAM relevance:** Critical cautionary precedent. Pure pop-up alerts fail and can harm. Andy must differentiate via workflow integration, specificity, and embedded order sets — not just notification.

---

### 40 — Wu/Li 2024 — AKI alert + care bundle RCT (Nanjing)

- **Source:** `40_WuLi2024_AKI-alert-bundle.pdf`
- **Citation:** Li T, Wu B, Li L, et al.; Mao H (corresponding). Automated Electronic Alert for the Care and Outcomes of Adults With Acute Kidney Injury: A Randomized Clinical Trial. JAMA Netw Open. 2024;7(1):e2351710. doi:10.1001/jamanetworkopen.2023.51710.
- **Design / N:** Single-center double-blind RCT, tertiary teaching hospital in Nanjing China, 2019-08 to 2021-12. 2,208 adults with hospital-acquired AKI (KDIGO); randomized 1:1 alert vs usual care.
- **Key numbers:**
  - Primary: max ΔeGFR @7d 3.7 (-6.4 to 19.3) alert vs 2.9 (-9.2 to 16.9) usual care; p=0.24 — null
  - IV fluids: 82.6% alert vs 61.8% usual (p<.001)
  - NSAID exposure: 5.0% alert vs 11.0% usual (p<.001)
  - AKI documented at discharge: 49.9% alert vs 27.3% usual (p<.001)
  - No difference in patient-centered outcomes (death, dialysis, AKI progression, AKI recovery)
- **Headline quote:** "the electronic AKI alert did not improve kidney function or other patient-centered outcomes" (abstract)
- **SAM relevance:** Second RCT confirming alerts change behavior (more fluids, less NSAIDs, more documentation) but don't move hard outcomes alone. Reinforces Andy's positioning: bundled, intelligent intervention > naive alerting.

---

### 41 — Paoli 2018 — US sepsis epidemiology and costs

- **Source:** `41_Paoli2018_sepsis-epidemiology-cost.pdf`
- **Citation:** Paoli CJ, Reynolds MA, Sinha M, Gitlin M, Crouser E. Epidemiology and Costs of Sepsis in the United States — An Analysis Based on Timing of Diagnosis and Severity Level. Crit Care Med. 2018;46:1889-1897. doi:10.1097/CCM.0000000000003342.
- **Design / N:** Retrospective Premier Healthcare Database (~20% of US inpatient discharges); 2,566,689 adult sepsis cases, Jan 2010 – Sep 2016.
- **Key numbers:**
  - Mean per-hospitalization cost: $16,324 (sepsis w/o organ dysfunction), $24,638 (severe sepsis), $38,298 (septic shock)
  - Sepsis present on admission: $18,023; NOT present on admission: $51,022 (≈2.8× higher)
  - Overall mortality 12.5% → 5.6% / 14.9% / 34.2% by severity
  - 2013 US sepsis hospital costs: >$24 billion, ~$18,244 per hosp; 13% of total US hospital costs, 3.6% of stays
  - ~970,000 US sepsis admissions annually
  - LOS: 4.5 / 6.5 / 16.5 days by severity
- **Headline quote:** "Sepsis cases not diagnosed until after admission … had a higher economic burden" (abstract)
- **SAM relevance:** Single best dollar-anchor for Andy sepsis-module value prop: catching sepsis at admission vs in-hospital saves ~$33k per case ($51,022 - $18,023). Multiply by sepsis-not-on-admission volume to size TAM.

---

### 42 — Silver 2017 — US cost of AKI (NIS 2012)

- **Source:** `42_Silver2017_AKI-cost.pdf`
- **Citation:** Silver SA, Long J, Zheng Y, Chertow GM. Cost of Acute Kidney Injury in Hospitalized Patients. J Hosp Med. 2017;12:70-76. doi:10.12788/jhm.2683.
- **Design / N:** 2012 National Inpatient Sample; 29,763,649 adult hospitalizations without ESRD; 3,031,026 with AKI; 106,515 AKI-D (dialysis).
- **Key numbers:**
  - Unadjusted excess hospitalization cost: $7,933 per AKI case (95% CI $7,608-$8,258); +3.2 days LOS
  - Adjusted excess cost: $1,795 per AKI case (95% CI $1,692-$1,899); +1.1 days
  - AKI requiring dialysis (unadj): $42,077 (95% CI $39,820-$44,335); +11.5 days LOS
  - AKI-D adjusted: $11,016 excess; +3.9 days
  - In-hospital mortality with AKI: 20-25%; AKI-D >50%
  - AKI affects ~20% of hospitalized patients; incidence rising ~10%/yr
  - Costs comparable to stroke, pancreatitis, pneumonia
- **Headline quote:** "AKI is associated with excess hospitalization costs and prolonged LOS" (abstract, p.70)
- **SAM relevance:** Foundational US-anchor for AKI cost modeling. $1,795 adjusted excess × ~3M AKI hospitalizations/yr ≈ ~$5.4B addressable cost pool — direct TAM input for Andy AKI module.

---

### 43 — Wen 2018 — AKI under-recognition

- **Source:** `43_Wen2018_AKI-underrecognition.pdf`
- **Citation:** *Citation not verifiable — the PDF in repo is mis-named.* The file actually contains: Martin JP, Li Q. Altering Compliance of a Load Carriage Device in the Medial-Lateral Direction Reduces Peak Forces While Walking. Sci Rep 2018;8:13775. (Unrelated biomechanics paper.)
- **Design / N:** **Extraction failed — wrong PDF.** The intended Wen 2018 AKI under-recognition paper was not present in this file.
- **Key numbers:** Not available — wrong source file.
- **Headline quote:** N/A
- **SAM relevance:** Re-download required before this can be cited. Andy AKI under-recognition support currently rests on Wilson 2021 (#39), Esposito 2024 (#14), and Wu 2025 (#15).

---

### 44 — Al-Jaghbeer 2018 — AKI CDSS multicenter impact *(stub-derived)*

- **Source:** `44_AlJaghbeer2018_AKI-CDSS.md` (paywall — JASN)
- **Citation:** Al-Jaghbeer M, Dealmeida D, Bilderback A, Ambrosino R, Kellum JA. Clinical Decision Support for In-Hospital AKI. J Am Soc Nephrol. 2018 Feb;29(2):654-660. doi:10.1681/ASN.2017070765.
- **Design / N:** Multicenter pre/post CDSS implementation; 528,108 patients (12 mo pre, 24 mo post); 64,512 with AKI.
- **Key numbers:**
  - Mortality 10.2% → 9.4% (OR 0.91, 95% CI 0.86-0.96, p=0.001)
  - LOS 9.3 → 9.0 days
  - Adjusted mortality OR 0.76 (95% CI 0.70-0.83)
  - Adjusted dialysis OR 0.66 (95% CI 0.61-0.72)
- **Headline quote:** Not available from stub (paywalled).
- **SAM relevance:** Best published evidence an AKI CDSS moves hard outcomes (mortality, dialysis, LOS) at scale. Outcome bar against which Andy's AKI module is benchmarked. **Stub-derived only — verify against full text before citing.**

---

### 45 — Khan 2021 — Medical expenditures prior to diabetes dx

- **Source:** `45_Khan2021_diabetes-expenditures.pdf`
- **Citation:** Khan T, Yang J, Wozniak G. Trends in Medical Expenditures Prior to Diabetes Diagnosis: The Early Burden of Diabetes. Population Health Management. 2021;24(1):46-…. doi:10.1089/pop.2019.0143.
- **Design / N:** Retrospective claims analysis, Truven Health MarketScan Commercial Claims; commercially insured patients newly diagnosed with diabetes in 2014 vs propensity-matched controls; 5-year lookback.
- **Key numbers:**
  - Excess spending over 5 years pre/dx: $8,941 per case (matched model)
  - Of which ~$4,828 in year of diagnosis
  - Compound annual growth rate per-capita spend 2010-2014: 14.3% (cases) vs ~5.3% (controls) — ~9 pp higher
  - US 2017 diabetes cost: $237B + $90B reduced productivity
  - Diagnosed diabetes per-capita medical: ~$16,750/yr (~2.3× non-diabetic); ~$9,600 attributable
- **Headline quote:** "rise in medical spending associated with diabetes begins well in advance of the first … diagnosis" (abstract)
- **SAM relevance:** Quantifies the pre-diagnosis cost ramp Andy can intercept. ~$4,828 in dx-year excess × undiagnosed diabetes population (≈8.7M US adults, NIDDK) frames a "find-it-earlier" SAM lane beyond inpatient.

---

### 46 — Walen 2020 — Delayed diagnosis of PE *(stub-derived)*

- **Source:** `46_Walen2020_PE-delayed-dx.md` (paywall — Respiration/Karger)
- **Citation:** Walen S, Damoiseaux RAMJ, Uil SM, van den Berg JWK. Delayed Diagnosis in Pulmonary Embolism: Frequency, Patient Characteristics, and Outcome. Respiration. 2020;99(7):589-597. doi:10.1159/000508396.
- **Design / N:** Per stub: cohort describing frequency, demographics, outcomes of delayed PE dx. Related cohort (Mansella 2020): 44/226 PE cases delayed (19.5%).
- **Key numbers:**
  - Delayed PE diagnosis in ~20% of cases (from related cohort; specific Walen numbers not in stub)
  - Chest pain / DVT symptoms → earlier dx
- **Headline quote:** Not available from stub (paywalled).
- **SAM relevance:** PE is a top-missed inpatient diagnosis (cf. Gunderson #04). ~20% delay rate frames addressable signal for an Andy PE-trigger module. **Stub-derived only — verify against full text before citing.**

---

## Section C — DRG/payment, market/revenue, CDI penetration (#47–#60)

# Section C — DRG / Payment, Market / Revenue, CDI Penetration (papers #47–#60)

Findings extracted by Andy literature pass. Sources: peer-reviewed = high confidence; OIG / CMS = high; vendor / press-release = low; industry survey = medium.

---

### 47 — Gluckman 2020 — DRG shifts to MCC outpace true severity

- **Source:** `47_Gluckman2020_DRG-trends.pdf`
- **Citation:** Gluckman TJ, Spinelli KJ, Wang M, et al. Trends in Diagnosis Related Groups for Inpatient Admissions and Associated Changes in Payment From 2012 to 2016. JAMA Netw Open. 2020;3(12):e2028470. doi:10.1001/jamanetworkopen.2020.28470.
- **Design / N:** Retrospective cohort, all-payer National Inpatient Sample, 62,167,976 hospitalizations across top-20 reimbursed DRG families, 2012–2016. Peer-reviewed (high confidence).
- **Key numbers:**
  - Top-20 DRG families = 12.9M hospitalizations in 2016 (36.0% of all US hospitalizations) and ≥$115.4B in payment.
  - 15/20 (75%) DRG families had a significant increase in % assigned to MCC tier.
  - PCI with MCC: 17.9% (2012) → 25.2% (2016).
  - Hip/femur with MCC: 17.1% → 19.4%.
  - DRG-shift–attributable payment increase: **≥$1.2 billion** (incremental, holding case mix constant).
  - Risk-adjusted mortality decreased in 8 of 19 families; comorbidity scores stable or decreased in 80% — i.e., MCC growth not explained by true severity.
  - HF DRG 291 (w/MCC) pays roughly 2× DRG 293 (no CC/MCC).
- **Headline quote:** "observed DRG shifts were associated with at least $1.2 billion in increased payment" (p.1)
- **SAM relevance:** Documents a real, recurring, multi-billion-dollar revenue lever from MCC-tier capture across the top 20 DRGs — the exact dollar pool Andy's evidence-grounded diagnosis suggestions can defensibly tap (without the upcoding tail risk).

---

### 48 — HHS-OIG 2021 — Highest-severity Medicare inpatient stays drive half of IPPS spend

- **Source:** `48_HHSOIG2021_expensive-stays.pdf`
- **Citation:** HHS Office of Inspector General. Trend Toward More Expensive Inpatient Hospital Stays in Medicare Emerged Before COVID-19 and Warrants Further Scrutiny. Data Brief OEI-02-18-00380, February 2021.
- **Design / N:** Analysis of 100% Medicare Part A inpatient claims, FY2014–FY2019. Government report (high confidence).
- **Key numbers:**
  - FY2019: 8.7M Medicare inpatient stays; $109.8B total Medicare IPPS spend.
  - Highest-severity (MCC-tier) stays: 3.5M (~40% of stays) but **$54.6B = 49.7% of inpatient spend**.
  - Average payment per highest-severity stay: **$15,500**.
  - High-severity stay count +19% FY14→FY19; low -22%, medium -12%.
  - Payments for highest-severity stays +24% (~+$10B) over 6 years.
  - Avg LOS for highest-severity stays fell 6.9 → 6.4 days (suggests upcoding, not true sicker patients).
  - ~30% of highest-severity stays were >20% shorter than mean LOS for that MS-DRG; >50% had only one qualifying complication.
  - Worked example (pneumonia): DRG 193 (MCC) $8,505 vs DRG 195 (no CC) $4,175 — ≈$4,330 MCC uplift per stay.
  - 761 MS-DRGs across 335 base DRGs in FY2019.
- **Headline quote:** "nearly half of all Medicare spending on inpatient hospital stays" (p.3)
- **SAM relevance:** Anchors Andy's hospital wedge: nearly half of US inpatient Medicare dollars (~$55B/yr) ride on the MCC severity flag for a single complication — exactly the layer Andy's diagnostic capture targets.

---

### 49 — CMS 2020 — IPPS FY2021 Final Rule (stub of larger reg)

- **Source:** `49_CMS2020_IPPS-FY2021.pdf` (21KB Small Entity Compliance Guide — full rule is in Federal Register Vol. 85, No. 182, p.58432)
- **Citation:** Centers for Medicare & Medicaid Services. Medicare Program; Hospital Inpatient Prospective Payment Systems for Acute Care Hospitals … Final Policy Changes and Fiscal Year 2021 Rates. CMS-1735-F, Fed Reg Vol 85 No 182, p.58432, Sept 18, 2020.
- **Design / N:** Federal rulemaking (high confidence for stated CMS policy; stub document only).
- **Key numbers:**
  - Estimated avg operating payment for IPPS hospitals **+2.5%** in FY2021.
  - Finalized a market-based MS-DRG relative weight methodology beginning **FY2024**.
  - SBA small-business threshold for hospitals: revenues ≤$38.5M/yr (CMS assumes "great majority" of participating hospitals qualify).
  - Per-DRG weights / payment rates not enumerated in this stub — full rule needed.
- **Headline quote:** "operating payment for IPPS hospitals will increase by about 2.5 percent" (p.2)
- **SAM relevance:** Confirms the macro IPPS payment update lever (~2.5%/yr) and the FY2024 transition to market-based DRG weights — both shape the size of the addressable per-admission uplift pool. Stub-derived only — verify specific DRG weights against full Federal Register text before citing.

---

### 50 — CMS 2023 — MA CY2024 Rate Announcement (V28 HCC model phase-in)

- **Source:** `50_CMS2023_MA-CY2024-rate.pdf`
- **Citation:** Centers for Medicare & Medicaid Services. Announcement of Calendar Year (CY) 2024 Medicare Advantage Capitation Rates and Part C and Part D Payment Policies. March 31, 2023.
- **Design / N:** CMS final rate notice (high confidence).
- **Key numbers:**
  - FY2020 MA program cost cited elsewhere as $314B of $780B total Medicare (per HHS-OIG #51).
  - National Per Capita MA Growth Percentage CY2024: **1.60%**; FFS Growth Percentage: **2.45%**.
  - New 2024 CMS-HCC risk model phased in over 3 years: 67%/33% blend (2020/2024 models) in CY2024 → 33%/67% in CY2025 → 100% 2024 model in CY2026.
  - 2024 model recalibrated with 2018 diagnosis + 2019 expenditure data (vs current 2014/2015); ICD-10 native.
  - 2024 CMS-HCC normalization factor: 1.015.
  - Statutory MA coding-pattern adjustment held at minimum **5.90%** for CY2024.
  - Bid-to-benchmark ratios (EGWP, CY2024): 78.5% / 77.2% / 76.6% / 76.8% across the four applicable percentages.
- **Headline quote:** "less susceptible to discretionary coding, which can lead to excess payments to MA plans" (p.1)
- **SAM relevance:** V28 transition explicitly tightens which HCCs pay — every code Andy captures has to be one that survives V28. Defines the moving target for the payer-side risk-adjustment market Andy serves.

---

### 51 — HHS-OIG 2021 — $9.2B in MA payments from chart-review + HRA only

- **Source:** `51_HHSOIG2021_chartreview-9B.pdf`
- **Citation:** HHS Office of Inspector General. Some Medicare Advantage Companies Leveraged Chart Reviews and Health Risk Assessments To Disproportionately Drive Payments. OEI-03-17-00474, September 2021.
- **Design / N:** Analysis of 2016 MA encounter data, 162 MA companies. Government report (high confidence).
- **Key numbers:**
  - **$9.2 billion** in 2017 MA risk-adjusted payments driven by diagnoses reported ONLY via chart reviews and HRAs (no other service record).
  - 20 of 162 MA companies disproportionately drove these payments (each >25% above their enrollment share).
  - One company alone: 40% of these payments while enrolling only 22% of MA beneficiaries; ~1/3 of all chart-review-only payments and >50% of HRA-only payments.
  - In 2020: 25M Medicare beneficiaries (40%) were in MA.
  - FY2020 MA cost: $314B of $780B total Medicare.
- **Headline quote:** "20 of the 162 MA companies drove a disproportionate share of the $9.2 billion" (p.i)
- **SAM relevance:** Quantifies the payer-side "diagnoses-found-nowhere-else" market at ~$9B/yr — the precise gap Andy fills with evidence-anchored capture that survives audit. Defines both the opportunity and the regulatory headwind.

---

### 52 — Meyers & Trivedi 2021 — MA chart reviews = +$2.3B/yr

- **Source:** `52_MeyersTrivedi2021_MA-chart-reviews.pdf`
- **Citation:** Meyers DJ, Trivedi AN. Medicare Advantage Chart Reviews Are Associated with Billions in Additional Payments for Some Plans. Med Care. 2021 Feb;59(2):96–100. doi:10.1097/MLR.0000000000001412.
- **Design / N:** Cross-sectional, 100% 2015 MA encounter files; 14,021,692 beneficiaries across 510 MA contracts. Peer-reviewed (high confidence).
- **Key numbers:**
  - Chart reviews → **+$2.30B** in MA payments (3.7% of MA spend) in 2015.
  - 4.5% of MA enrollees had HCC change from chart review; mean HCC delta +0.028 (4.1%).
  - Top decile of contracts = **42%** of $2.3B uplift.
  - Top-decile contract avg HCC increase: 10.0%; top-quintile contracts averaged 17.2% risk-score lift from chart review.
  - Per-contract mean uplift: $6.16M total / **$231.80 per capita** ; top-quintile mean +$15.67M per contract.
  - Top company-level reimbursement uplift: $481,245,082.
  - 92% of top-quintile chart-review contracts were for-profit (vs 61.1% of zero-review contracts).
  - State variation: Puerto Rico +14.9%, Delaware +13.1%; Montana 0.7%.
- **Headline quote:** "a $2.3 billion increase in payments to plans, a 3.7 percent increase" (p.96)
- **SAM relevance:** Independent peer-reviewed sizing of the chart-review uplift channel — ~$232 per MA member per year — directly translatable into Andy's per-member economics for MA payer customers.

---

### 53 — Meyers/Trivedi 2024 — MA HRAs contribute up to $12B/yr (stub)

- **Source:** `53_MeyersTrivedi2024_HRA-12B.md` (Health Affairs paywall; stub only)
- **Citation:** Meyers DJ, Mor V, Rahman M, Trivedi AN. Medicare Advantage Health Risk Assessments Contribute Up To $12 Billion Per Year To Risk-Adjusted Payments. Health Aff. 2024 May;43(5):614–622. doi:10.1377/hlthaff.2023.00787.
- **Design / N:** 2019 MA encounter data analysis. Peer-reviewed (high confidence) — but extraction stub-derived only.
- **Key numbers:**
  - 44.4% of MA beneficiaries had ≥1 HRA.
  - +12.8% mean HCC score uplift among those with an HRA.
  - Up to **$12.3 billion/yr** in aggregate MA payment attributable to HRA-driven coding.
- **Headline quote:** "Contribute Up To $12 Billion Per Year To Risk-Adjusted Payments" (title)
- **SAM relevance:** Updates the 2021 chart-review estimate (~$2.3B) by adding the HRA channel — together a ~$12B+/yr coding-driven MA payment pool Andy can credibly arbitrate with evidence-grounded capture. Stub-derived only — verify against full text before citing.

---

### 54 — Streamline Health 2023 — DRG change rate 10% → 18% (stub / vendor)

- **Source:** `54_StreamlineHealth2023_DRG-case-study.md`
- **Citation:** Streamline Health customer case study (Nov 2023). Vendor marketing.
- **Design / N:** Single customer case study; methodology not disclosed. **Confidence: low (vendor / press-release).**
- **Key numbers:**
  - DRG change rate **10% → 18%** post pre-bill DRG validation tooling.
- **Headline quote:** "DRG change rate increasing from 10% to 18%" (stub)
- **SAM relevance:** Competitive benchmark for the per-discharge DRG-validation lift Andy must match or beat. Stub-derived only — verify against full case study before citing.

---

### 55 — ACDIS 2024 — CDI Week Industry Overview Survey (stub / industry)

- **Source:** `55_ACDIS2024_CDI-week-survey.md`
- **Citation:** ACDIS. 2024 CDI Week Industry Overview Survey. 14th annual; >800 respondents. **Confidence: medium (industry self-report).**
- **Design / N:** Self-reported survey of CDI professionals (n>800).
- **Key numbers:**
  - 36.13% of CDI roles based in acute-care hospitals (down from 40.06% in 2023) — workflow diversifying outpatient.
  - 70.45% RN credentialed; 70.32% CCDS credentialed.
  - 73.44% report query response rates 91–100%.
  - 29.69% query 31–40% of cases reviewed.
  - ~64% of CDI programs participate in denials management.
  - 47.16% review pediatric cases.
- **Headline quote:** "CDI roles diversifying beyond inpatient" (stub paraphrase)
- **SAM relevance:** Profiles the CDI buyer persona and current workflow density — direct input to Andy's per-CDI-FTE pricing and seat-count sizing. Stub-derived only — verify against full ACDIS report before citing.

---

### 56 — ClarisHealth — Payment-integrity contingency ~15% (stub / vendor)

- **Source:** `56_ClarisHealth_PI-contingency-rate.md`
- **Citation:** ClarisHealth blog, "Payment Integrity Leaders Reveal What Will Move the Industry Forward." **Confidence: low (vendor blog, no primary survey).**
- **Design / N:** Industry commentary; n not stated.
- **Key numbers:**
  - Industry-average payment-integrity contingency fee: ~**15%** (actual often higher).
  - ClarisHealth claim: ~50% reduction in contingency fees when audits internalized on their platform.
- **Headline quote:** "average payment integrity vendor contingency rate ~15%" (stub)
- **SAM relevance:** Sets the price umbrella — a software-priced Andy payment-integrity wedge has wide margin under a 15% contingency benchmark. Stub-derived only — verify against industry primary source before citing.

---

### 57 — SmarterDx — $2.0–2.5M net new revenue / 10,000 discharges (stub / vendor)

- **Source:** `57_SmarterDx_revenue-per-discharge.md`
- **Citation:** SmarterDx vendor collateral and 2024 funding announcement (PRNewswire, Flare Capital). **Confidence: low (vendor self-report).**
- **Design / N:** Vendor-reported aggregate from undisclosed customer base.
- **Key numbers:**
  - **$2.0–2.5M** net new annual revenue per 10,000 patient discharges → **$200–250 per discharge**.
  - Guaranteed 5:1 ROI from Day 1.
  - 60+ health systems, 250+ hospital sites (2024).
- **Headline quote:** "$2.0–2.5M in realized annual net new revenue per 10,000 patient discharges" (stub)
- **SAM relevance:** Closest direct competitor benchmark — Andy must hit or beat ~$200–250/discharge to be credible to a hospital CFO. Stub-derived only — verify against vendor collateral before citing.

---

### 58 — AHIMA 2018 — CDI Toolkit (penetration baseline)

- **Source:** `58_AHIMA2018_CDI-toolkit.pdf`
- **Citation:** American Health Information Management Association. AHIMA Clinical Documentation Integrity (CDI) Toolkit — Beginners' Guide. ©AHIMA 2021 (cites AHIMA 2018 CDI Survey Report). ISBN 978-1-58426-866-6.
- **Design / N:** Toolkit citing AHIMA 2018 CDI Survey (n=157 CDI professional respondents). **Confidence: medium (industry survey).**
- **Key numbers:**
  - **89.81%** of 2018 survey respondents reported a CDI program at their organization.
  - 78.98% of respondents were from hospital settings.
- **Headline quote:** "89.81 percent had a CDI program within their organization" (p.5)
- **SAM relevance:** Establishes that CDI is already near-universal in hospital HIM departments — Andy is augmenting an entrenched workflow, not creating a new buyer category.

---

### 59 — AHIMA / TrustHCS 2013 — State of HIM CDI adoption (stub)

- **Source:** `59_AHIMA2013_state-of-HIM.md`
- **Citation:** AHIMA & TrustHCS. 2013 State of HIM / ICD-10 readiness survey, >300 HIM professionals at 293 facilities. **Confidence: medium (industry survey).**
- **Design / N:** Industry survey (n≈300 HIM professionals).
- **Key numbers:**
  - ~**66%** (two-thirds) of hospitals had an in-house CDI program in 2013.
  - 41% of remaining facilities planned to launch CDI in 2013.
  - User's index cited "96% at >350-bed hospitals" — NOT independently confirmed in the stub's source excerpts.
- **Headline quote:** "two-thirds of hospitals already supporting an in-house CDI initiative" (stub)
- **SAM relevance:** Historical anchor: CDI already mainstream by 2013, especially at larger hospitals — Andy's CDI augmentation has a mature buyer base. Stub-derived only — verify the 96% figure against the original AHIMA report before citing.

---

### 60 — Black Book 2018 — 65% of >200-bed hospitals outsource CDI (stub)

- **Source:** `60_BlackBook2018_CDI-outsourcing.md`
- **Citation:** Black Book Market Research. New Generation CDI Enhances Patient Care and Reduces Financial Risk. October 2018; survey n=2,920 health leaders. **Confidence: low (market-research press release).**
- **Design / N:** Self-reported survey of 2,920 health leaders.
- **Key numbers:**
  - **65%** of hospitals >200 beds outsource CDI audit/review/programming in 2018 (up from **24%** in 2015) — ~2.7× growth in 3 years.
  - 91% of >150-bed hospitals outsourcing CDI in Q3 reported **>$2.1M minimum** revenue / reimbursement uplift.
- **Headline quote:** "65% of hospitals >200 beds outsource CDI audit/review/programming" (stub)
- **SAM relevance:** Critical GTM signal — hospital CDI is an already-outsourced workflow, so Andy faces a buyer culture that accepts third-party CDI software and vendors. ~$2.1M+ per-hospital uplift sets the per-account revenue expectation. Stub-derived only — verify against Black Book primary report before citing.

---

*End Section C.*

---

## Section D — HFpEF, CKD undiagnosed, malpractice, NAM, misc (#61–#72)

# Section D Findings — HFpEF, CKD, Malpractice, Macro (papers #61-#72)

### 61 — van Riet 2014 — Unrecognized HF in elderly with exertional dyspnea (primary care)

- **Source:** `61_vanRiet2014_unrecognized-HF.pdf`
- **Citation:** van Riet EES, Hoes AW, Limburg A, Landman MAJ, van der Hoeven H, Rutten FH. Prevalence of unrecognized heart failure in older persons with shortness of breath on exertion. Eur J Heart Fail. 2014;16(7):772-777.
- **Design / N:** Cross-sectional selective screening study in Dutch primary care; N=585 patients aged >=65 with exertional dyspnea in prior 12 months, no prior HF diagnosis.
- **Key numbers:**
  - New HF diagnosis: 92/585 = 15.7% (95% CI 12.9-19.0)
  - HF-PEF: 12.0% (70/585); HF-REF: 2.9% (17/585); isolated right-sided: 0.9%
  - Of new HF cases, 76.1% were HF-PEF
  - Overall HF prevalence (new + known) in elderly dyspnea cohort: 32.8% (95% CI 30.8-34.9)
  - Mean age 74.1 (SD 6.3); 54.5% female
- **Headline quote:** "unrecognized heart failure is common with a prevalence of 15.7%" (p.775)
- **SAM relevance:** Anchors the underdiagnosis rate for HFpEF in symptomatic elderly seen in primary care — supports sizing the "missed HFpEF" addressable population that an AI copilot could surface at the GP visit.

### 62 — Redfield 2003 — Burden of systolic/diastolic dysfunction in the community

- **Source:** `62_Redfield2003_systolic-diastolic-dysfunction.pdf`
- **Citation:** Redfield MM, Jacobsen SJ, Burnett JC Jr, Mahoney DW, Bailey KR, Rodeheffer RJ. Burden of systolic and diastolic ventricular dysfunction in the community. JAMA. 2003;289(2):194-202.
- **Design / N:** Cross-sectional, random sample of N=2,042 Olmsted County, MN residents aged >=45 (1997-2000); Doppler echocardiography + chart review (Framingham criteria).
- **Key numbers:**
  - Validated CHF prevalence: 2.2% (95% CI 1.6-2.8); 44% had EF >50%
  - Any diastolic dysfunction: 28.1% (mild 20.8% + moderate 6.6% + severe 0.7%)
  - Moderate/severe diastolic dysfunction with normal EF: 5.6% (95% CI 4.5-6.7)
  - Any systolic dysfunction (EF <=50%): 6.0%; moderate/severe (EF <=40%): 2.0%
  - "Less than half" of those with moderate/severe systolic OR diastolic dysfunction had recognized CHF
  - Mild diastolic dysfunction HR for all-cause mortality: 8.31 (95% CI 3.00-23.1)
- **Headline quote:** "less than half had recognized CHF" (p.194 abstract)
- **SAM relevance:** Foundational community prevalence numbers — supports a ~6% adult >=45 prevalence of unrecognized diastolic dysfunction, the dominant pool of missable HFpEF in Andy's TAM.

### 63 — van Riet 2016 — Systematic review of HF/LVD prevalence in older adults

- **Source:** `63_vanRiet2016_HF-prevalence-time.pdf`
- **Citation:** van Riet EES, Hoes AW, Wagenaar KP, Limburg A, Landman MAJ, Rutten FH. Epidemiology of heart failure: the prevalence of heart failure and ventricular dysfunction in older adults over time. A systematic review. Eur J Heart Fail. 2016;18(3):242-252.
- **Design / N:** Systematic review; 28 articles from 25 study populations, community-dwelling adults aged >=60 with echocardiographic diagnosis.
- **Key numbers:**
  - Median prevalence systolic LVD: 5.5% (range 3.3-9.2%)
  - Median prevalence "isolated" diastolic LVD: 36.0% (range 15.8-52.8%)
  - "All type" HF median prevalence: 11.8% (range 4.7-13.3%)
  - HFpEF median: 4.9% (range 3.8-7.4%); HFrEF median: 3.3% (range 2.4-5.8%)
  - Adult-population HF most-cited estimate: 2% (1-3%); age >=65: 5-9%
- **Headline quote:** "HFpEF being more common than HFrEF" (p.242)
- **SAM relevance:** Gives Andy a defensible global denominator: ~12% HF prevalence in adults 60+, with HFpEF the dominant and most-underdiagnosed subtype — key for prioritizing HFpEF detection module.

### 64 — Groenewegen 2020 — Contemporary epidemiology of heart failure (review)

- **Source:** `64_Groenewegen2020_HF-epidemiology.pdf`
- **Citation:** Groenewegen A, Rutten FH, Mosterd A, Hoes AW. Epidemiology of heart failure. Eur J Heart Fail. 2020;22(8):1342-1356.
- **Design / N:** Narrative review of community-based and registry studies of HF.
- **Key numbers:**
  - 64.3 million people living with HF worldwide
  - Known-HF prevalence in developed countries: 1-2% of general adult population
  - Calculated total HF prevalence including unrecognized cases: ~4.2% (about 2x registry rate)
  - HF prevalence age >=60: 11.8% (median, community studies)
  - Up to 76% of HFpEF cases can remain undetected
  - ICD-10 HF code sensitivity 68.6%, specificity 99.3% vs chart review
- **Headline quote:** "may remain undetected in over half of the cases" (p.1344)
- **SAM relevance:** Anchors the "2x undercount" framing for HF — registries see 1-2% but true prevalence ~4.2%, meaning Andy's addressable HF detection market is double what claims data suggests.

### 65 — Tangri 2023 — REVEAL-CKD: undiagnosed stage 3 CKD across 6 countries

- **Source:** `65_Tangri2023_REVEAL-CKD.pdf` (visual abstract only in file)
- **Citation:** Tangri N et al. Prevalence of Undiagnosed Stage 3 Chronic Kidney Disease in France, Germany, Italy, Japan and the USA: Results from the Multinational Observational REVEAL-CKD Study. BMJ Open. 2023;13:e067386.
- **Design / N:** Multinational observational study; adults >=18 with >=2 consecutive eGFR 30-<60 mL/min/1.73m2, >=90 days apart (stage 3 CKD).
- **Key numbers:**
  - Prevalence of undiagnosed stage 3 CKD by country:
    - France: 95.5%
    - Germany: 84.3%
    - Italy: 77%
    - Japan: 92.1%
    - US (Explorys LCED): 61.6%
    - US (TriNetX): 64.3%
  - Factors associated with undiagnosed CKD (ORs): female sex 1.29-1.77; stage 3a vs 3b 1.81-3.66; no DM history 1.26-2.77; no HTN history 1.35-1.78
- **Headline quote:** "61.6%" undiagnosed US stage 3 CKD (visual abstract)
- **SAM relevance:** Direct US undiagnosis rate (~62-64%) for stage 3 CKD — multiplies against ~37M US CKD prevalence to size Andy's "find the missing CKD" opportunity in primary care.

### 66 — CDC 2024 — Chronic Kidney Disease in the United States (factsheet)

- **Source:** `66_CDC2024_CKD-factsheet.pdf`
- **Citation:** Centers for Disease Control and Prevention. Chronic Kidney Disease in the United States. Atlanta, GA: U.S. Department of Health and Human Services, CDC; 2026 (updated March 2026; data from NHANES Aug 2021-Aug 2023).
- **Design / N:** National factsheet derived from NHANES 2021-2023, USRDS 2025.
- **Key numbers:**
  - 14% of US adults aged 18+ have CKD = ~37 million people
  - 87% (about 9 in 10) of US adults 20+ with CKD do NOT know they have it
  - Prevalence by age: 6% (18-44), 13% (45-64), 34% (65+)
  - 38% of adults with diabetes have CKD; 41% of T2D; 49% of T1D
  - 21% of adults with hypertension have CKD
  - 11% of adults with prediabetes have CKD
  - ESKD 2023: ~831,000 living with ESKD (67% dialysis, 33% transplant); 131,564 new starts
- **Headline quote:** "About 9 in 10 (87%) adults aged 20 or older with CKD did not know" (p.1)
- **SAM relevance:** Bedrock US numbers — 37M CKD patients, 87% unaware. Combined with #65, Andy's CKD detection TAM ~= 37M x 0.87 ≈ 32M undiagnosed.

### 67 — Coverys 2018 — Diagnostic Accuracy: Room for Improvement (claims report)

- **Source:** `67_Coverys2018_dx-accuracy.pdf`
- **Citation:** Hanscom R, Small M, Lambrecht A. Diagnostic Accuracy: Room for Improvement. A Dose of Insight. Coverys; 2018. Based on analysis of 10,618 closed claims 2013-2017.
- **Design / N:** Closed-claims analysis; N=10,618 Coverys medical professional liability claims, 2013-2017.
- **Key numbers:**
  - Diagnosis-related: 33% of claims and 47% of indemnity paid (#1 cause; nearly equal to next 5 categories combined)
  - 54% of dx-related claims are high-severity; 36% result in death
  - 53% of dx-related claims involve poor clinical decision-making (risk management issue)
  - Top dx-step indemnity drivers (in $M): H&P/evaluation $109M; ordering of tests $101M; physician follow-up $94M; receipt/transmittal of results $22M; performance of tests $10M; referral mgmt $50M; follow-up with patient $28M
  - Healthcare contact rate: 84% of US adults, 93% of children annually
- **Headline quote:** "diagnosis-related events are the single largest root cause" (p.1)
- **SAM relevance:** Quantifies the malpractice carrier value-prop for Andy — dx errors drive ~47% of indemnity dollars. A copilot reducing missed dx by even 10% has direct insurer-side ROI.

### 68 — Coverys 2025 — Hidden in Plain Sight: Office-Based Practice Dx Errors

- **Source:** `68_Coverys2025_office-based.pdf`
- **Citation:** Siegal D, Icenhower M, Small M, et al. Hidden in Plain Sight: Exposing the Drivers of Diagnostic Error. Part Two: Office-Based Practice. Coverys; August 2025.
- **Design / N:** Closed-claims analysis; 6,009 events closed 2020-2024; 1,442 office-based; 552 office-based dx-error events.
- **Key numbers:**
  - Office/clinic = 34% of events and 38% of indemnity paid (highest care-setting share)
  - Of office-based events, 38% (552/1,442) involve missed/wrong/delayed dx
  - Dx-related = 26% of events, 27% events, 42% of indemnity paid
  - **Average indemnity per dx-related claim: $661,000 vs $323,000 for non-dx claims (>2x)**
  - Top missed dx: Cancer 45% (prostate, lung, breast, colorectal); Infection 14%
  - Top services: Internal/Family Med 41% events, 45% indemnity; Surgical specialties 23%/22%
- **Headline quote:** "$661,000. This is more than twice the average indemnity" (p.~5)
- **SAM relevance:** Per-claim $661K dx-error indemnity is the headline carrier ROI number for Andy. Combined with claim counts, drives malpractice-insurer SAM sizing.

### 69 — Pfeffer/Shah/Borlaug 2019 — HFpEF in perspective (review)

- **Source:** `69_Shah2020_HFpEF-perspective.pdf` (filename suggests "Shah2020"; actual: Pfeffer/Shah/Borlaug 2019, PMC release date 2020)
- **Citation:** Pfeffer MA, Shah AM, Borlaug BA. Heart Failure with Preserved Ejection Fraction: In Perspective. Circ Res. 2019;124(11):1598-1617.
- **Design / N:** Narrative review.
- **Key numbers:**
  - Approximately half (~50%) of HF patients have LVEF that is not markedly abnormal (i.e., HFpEF)
  - 1 in 5 men and women over 40 will develop HF during their lifetime
  - Mortality during an HF hospitalization: ~4%
  - 30-day post-discharge mortality after HF hospitalization: 10%
  - HF is among most frequent reasons for urgent hospitalization in Medicare
- **Headline quote:** "Approximately half of patients with signs and symptoms of heart failure" (abstract)
- **SAM relevance:** Cements the "HFpEF = half of HF" claim for Andy's HF subtype slicing, and the 1-in-5 lifetime risk anchors lifetime-detection economics.

### 70 — NAM 2015 — Improving Diagnosis in Health Care (book, exec summary)

- **Source:** `70_NAM2015_improving-diagnosis.pdf` (read pages 1-25 of 472-page book)
- **Citation:** National Academies of Sciences, Engineering, and Medicine. Improving Diagnosis in Health Care. Washington, DC: National Academies Press; 2015.
- **Design / N:** Consensus expert committee report.
- **Key numbers:**
  - "5 percent of U.S. adults who seek outpatient care each year experience a diagnostic error" (the canonical "1 in 20" stat)
  - Diagnostic errors contribute to ~10% of patient deaths (postmortem studies)
  - Diagnostic errors account for 6-17% of hospital adverse events
  - "Most people will experience at least one diagnostic error in their lifetime"
  - "$100B+/year" claim: NOT found in pages 1-25 read; not surfaced in executive summary chapter we sampled
- **Eight goals (verbatim from report):**
  1. Facilitate more effective teamwork in the diagnostic process among health care professionals, patients, and their families
  2. Enhance health care professional education and training in the diagnostic process
  3. Ensure that health information technologies support patients and health care professionals in the diagnostic process
  4. Develop and deploy approaches to identify, learn from, and reduce diagnostic errors and near misses in clinical practice
  5. Establish a work system and culture that supports the diagnostic process and improvements in diagnostic performance
  6. Develop a reporting environment and medical liability system that facilitates improved diagnosis by learning from diagnostic errors and near misses
  7. Design a payment and care delivery environment that supports the diagnostic process
  8. Provide dedicated funding for research on the diagnostic process and diagnostic errors
- **Headline quote:** "most people will experience at least one diagnostic error in their lifetime" (exec summary)
- **SAM relevance:** Authoritative macro framing for Andy's pitch — 1-in-20 outpatient error rate is the headline TAM-multiplier. The 8 goals (especially Goals 3 and 4) are the explicit policy hooks Andy's product addresses.

### 71 — HCCI 2024 — 2022 Health Care Cost and Utilization Report

- **Source:** `71_HCCI2024_cost-report.pdf`
- **Citation:** Health Care Cost Institute. 2022 Health Care Cost and Utilization Report. April 2024.
- **Design / N:** Analysis of de-identified commercial ESI claims (CVS/Aetna, Humana, BHI), under-65 ESI population, 2018-2022.
- **Key numbers:**
  - Per-person ESI spending 2022: $6,711 (up from $5,656 in 2018; +19% / +$1,055)
  - Average out-of-pocket per person 2022: >$850
  - Prices grew 14% over 2018-2022; utilization grew 4%
  - Inpatient admissions DOWN 11% over 5 years
  - Annual spending change 2020-21: +14.9% (COVID rebound)
- **Headline quote:** "per person spending among people with ESI exceeded $6,700" (Exec Summary)
- **SAM relevance:** ESI per-person spend baseline for Andy unit economics on commercial-insured book.
- **DISCREPANCY FLAGGED:** The expected "294% of Medicare" commercial-vs-Medicare price ratio is NOT in this report. This 2022 HCCUR covers only ESI per-person spend and does not benchmark commercial prices vs Medicare. The "294%" stat likely comes from a separate RAND Hospital Price Transparency Study (e.g., RAND 4.0/5.0), not from HCCI. Recommend re-sourcing.

### 72 — Kievit 2018 — Selective HF screening in elderly: prediction-model meta-analysis

- **Source:** `72_Kievit2018_HF-screening-elderly.pdf`
- **Citation:** Kievit RF, Gohar A, Hoes AW, et al. Efficient selective screening for heart failure in elderly men and women from the community: A diagnostic individual participant data meta-analysis. Eur J Prev Cardiol. 2018;25(4):437-446.
- **Design / N:** IPD meta-analysis of 4 primary-care screening cohorts (STRETCH, UHFO-DM, UHFO-COPD, TREE); N=1,941 participants >60 y; 462 diagnosed with HF.
- **Key numbers:**
  - HF detected in 462/1,941 = 23.8% of high-risk elderly community screening sample
  - Five-predictor clinical model: age, ischaemic heart disease history, exertional dyspnea, BMI, lateral/broadened apex beat
  - C-statistic (clinical model only): 0.70-0.82 across cross-validation
  - C-statistic with NT-proBNP added: 0.89 (95% CI 0.86-0.92), up from 0.76 (clinical alone)
  - No significant sex interaction
- **Headline quote:** "c-statistic increasing from 0.76 ... to 0.89" (abstract)
- **SAM relevance:** Validates that a 5-item clinical + 1 biomarker model achieves c=0.89 for HF in elderly — direct precedent for Andy's AKI/HF-detection module performance benchmarks and screening cost-effectiveness arguments.

---

## Verification queue

These items need attention before being used in any external-facing claim:

1. **#43 Wen2018_AKI-underrecognition.pdf** — Wrong PDF in folder; current file is a biomechanics paper (Martin & Li, Sci Rep 2018, load carriage). Re-download from https://www.nature.com/articles/s41598-018-32175-x
2. **#71 HCCI 2024** — "294% of Medicare" stat is NOT in the downloaded HCCI document. The figure is almost certainly from a RAND Hospital Price Transparency Study. Re-source.
3. **#70 NAM 2015** — "$100B+/year" cost claim not surfaced in executive summary (pages 1–25). May be in Ch. 1 or 3; verify before quoting.
4. **#65 Tangri 2023** — Downloaded PDF is the visual abstract only, not full paper. All key percentages were captured but verify before quoting verbatim.
5. **#69 Shah2020** — Filename says Shah 2020 but the paper is Pfeffer/Shah/Borlaug, Circ Res 2019 (PMC release 2020). Update authorship in any citation.
6. **#49 IPPS FY2021** — Downloaded PDF is the 21KB CMS fact-sheet stub, not the full IPPS Final Rule. For Table 5 / DRG weights, use the Federal Register version: https://www.federalregister.gov/documents/2020/09/18/2020-19637/
7. **#21 Naser 2024** — Substituted for the EMJ news piece originally cited. Verify it contains the "74% HFpEF / 35% previously identified" figures.
8. **#18 PIOPED** — Two candidate citations (Stein 1991 vs Stein/Henry 1995) — pick one.
9. **Citation author corrections caught while building stubs:** #16 is Greci 2003 *Diabetes Care* (not JCEM 2008); #17 first author is Ferris M (not Hsu CY); #53 authors are Meyers DJ, Mor V, Rahman M, Trivedi AN (not James HO et al.).
10. **Stubs needing fuller-text verification:** #02, #04, #10, #16, #17, #18, #44, #46 — all extracted from abstract only.

---

## Section E — Expansion evidence (Round 2: SAM-gap fillers)

These 10 papers were added specifically to close evidence gaps in the SAM calculation: AKI prevalence (US/global), CKD awareness, HFpEF US prevalence, AF detection gap, and malpractice per-condition apportionment.

### 73 — Susantitaphong 2013 — World incidence of AKI: a meta-analysis

- **Source:** `CJN.00710113.pdf`
- **Citation:** Susantitaphong P, Cruz DN, Cerda J, Abulfaraj M, Alqahtani F, Koulouridis I, Jaber BL, for the Acute Kidney Injury Advisory Group of the ASN. World incidence of AKI: a meta-analysis. Clin J Am Soc Nephrol. 2013;8(9):1482–1493. doi:10.2215/CJN.00710113.
- **Design / N:** Systematic review + random-effects meta-analysis of 312 cohort studies (n=49,147,878), 2004–2012, hospital-based; 154 studies (n=3,585,911) using KDIGO-equivalent definitions.
- **Key numbers:**
  - Pooled hospitalized-AKI incidence (KDIGO, adults): 21.6% (95% CI 19.3–24.1).
  - Pooled hospitalized-AKI incidence (KDIGO, children): 33.7% (95% CI 26.9–41.3).
  - Pooled AKI-associated mortality (adults): 23.9% (95% CI 22.1–25.7).
  - 1 in 5 adults and 1 in 3 children worldwide experience AKI during a hospital episode.
- **Headline quote:** "pooled incidence rates of AKI were 21.6% in adults" (Abstract, p.1482)
- **SAM relevance:** Unlocks AKI inpatient DRG cell — provides the foundational global hospitalized-AKI rate (KDIGO ~22%) used as the denominator for US AKI inpatient prevalence in SAM ladder; pairs with Hoste (ICU 57%) and Esposito (68% undetection) to size addressable AKI miss volume.

### 74 — Hoste 2015 — AKI-EPI multinational ICU study (stub-derived)

- **Source:** `02b_Hoste2015_AKI-EPI.md` (stub; full PDF paywalled)
- **Citation:** Hoste EAJ, Bagshaw SM, Bellomo R, et al. Epidemiology of acute kidney injury in critically ill patients: the multinational AKI-EPI study. Intensive Care Med. 2015;41(8):1411–1423. doi:10.1007/s00134-015-3934-7.
- **Design / N:** International cross-sectional prospective study, 97 ICUs, 1,802 patients, KDIGO criteria.
- **Key numbers:**
  - AKI incidence in ICU: 57.3% (95% CI 55.0–59.6) of 1,802 patients.
  - Stage 2 mortality adjusted OR: 2.945 (95% CI 1.382–6.276; p=0.005).
  - Stage 3 mortality adjusted OR: 6.884 (95% CI 3.876–12.228; p<0.001).
- **Headline quote:** "1032 ICU patients out of 1802 [57.3%; 95% CI 55.0–59.6] had AKI" (Abstract; stub)
- **SAM relevance:** Unlocks AKI ICU sub-cell — the canonical ICU-specific KDIGO AKI rate (57.3%) anchors the high-acuity portion of Andy's AKI SAM (~3.3M US ICU AKI cases/yr at ~5.7M ICU admits × 57.3%).

### 75 — Esposito 2024 — AKI recognition patterns in hospitalized patients

- **Source:** `sfae231.pdf` (CITATION MISMATCH: expected Cammarata 2024; file is actually Esposito et al. 2024 CKJ — DOI 10.1093/ckj/sfae231 belongs to Esposito's recognition-patterns paper, which is already entry #14 in Section A. This is effectively a duplicate of #14.)
- **Citation:** Esposito P, Cappadona F, Marengo M, et al. Recognition patterns of acute kidney injury in hospitalized patients. Clin Kidney J. 2024;17(8):sfae231. doi:10.1093/ckj/sfae231.
- **Design / N:** Single-center retrospective cohort, Italy, 56,820 hospitalized adults (2016–2019), AKI defined by both administrative coding and extended-KDIGO serum-creatinine criteria.
- **Key numbers:**
  - Overall AKI incidence: 24.5% (13,920/56,820).
  - AKI undetection rate: 68.2% (KDIGO-AKI not coded on HDF).
  - Full-AKI (sCr + coded): 3.3% (1,893); HDF-AKI only: 4.4%; KDIGO-AKI undetected: 16.7% (9,498).
  - Undetection by ward: medical 73%, surgical 86%, ICU 81%, ED 22%.
  - Per-case $ impact: not reported in sections read.
- **Headline quote:** "AKI incidence was 24.5%, with a 68% undetection rate" (Abstract, p.1)
- **SAM relevance:** Unlocks AKI DRG-uplift cell — directly quantifies the coding-gap multiplier (68% miss) applied to KDIGO AKI volume to size revenue-recovery TAM via CDI/HCC uplift.

### 76 — Plantinga 2008 — Patient awareness in chronic kidney disease

- **Source:** `nihms-88834.pdf`
- **Citation:** Plantinga LC, Boulware LE, Coresh J, Stevens LA, Miller ER 3rd, Saran R, Messer KL, Levey AS, Powe NR. Patient awareness of chronic kidney disease: trends and predictors. Arch Intern Med. 2008;168(20):2268–2275. doi:10.1001/archinte.168.20.2268.
- **Design / N:** Cross-sectional analysis of NHANES 1999–2004, n=2,992 US adults ≥20y with CKD stages 1–4.
- **Key numbers:**
  - Overall CKD awareness (stages 1–4): 6.0%.
  - Stage 3 awareness: 7.8% (1,314 participants).
  - Stage 4 awareness: ≈40% (fewer than half).
  - Stage 3 awareness trend: 4.7% (1999–2000) → 8.9% (2001–02) → 9.2% (2003–04); p=0.037.
  - Stages 1 and 2: <half the awareness of stage 3.
- **Headline quote:** "only 6.0% reported being told that they had weak or failing kidneys" (p.2)
- **SAM relevance:** Unlocks CKD outpatient never-detected cell — quantifies the patient-side awareness gap (~94% of CKD stages 1–4 unaware) that feeds Andy's outpatient under-diagnosis TAM in primary care.

### 77 — Tuot 2011 — CKD awareness among individuals with clinical markers

- **Source:** `cjn1838.pdf`
- **Citation:** Tuot DS, Plantinga LC, Hsu CY, Jordan R, Burrows NR, Hedgeman E, Yee J, Saran R, Powe NR. CKD awareness among individuals with clinical markers of kidney dysfunction. Clin J Am Soc Nephrol. 2011;6(8):1838–1844. doi:10.2215/CJN.00730111.
- **Design / N:** Cross-sectional NHANES 1999–2008, n=1,852 US adults with eGFR <60 mL/min/1.73m².
- **Key numbers:**
  - Overall CKD awareness among eGFR <60: 9%.
  - 90% of individuals with 2–4 clinical markers of CKD were unaware of disease.
  - 84% of individuals with ≥5 clinical markers were unaware.
  - Albuminuria associated with 4.0× higher awareness odds (95% CI 2.11–7.39) independent of eGFR.
  - Each additional clinical marker: adjusted OR 1.3 (p=0.05) for awareness.
- **Headline quote:** "90% of individuals with two to four markers of CKD…were unaware" (Abstract)
- **SAM relevance:** Unlocks CKD provider-side missed-dx cell — demonstrates that even patients with multiple lab abnormalities are not flagged with CKD, sizing Andy's primary-care CKD detection TAM.

### 78 — Owan 2006 — Trends in HFpEF prevalence and outcome (Olmsted County)

- **Source:** `NEJMoa052256.pdf`
- **Citation:** Owan TE, Hodge DO, Herges RM, Jacobsen SJ, Roger VL, Redfield MM. Trends in prevalence and outcome of heart failure with preserved ejection fraction. N Engl J Med. 2006;355(3):251–259.
- **Design / N:** Retrospective single-institution cohort, Mayo Clinic Hospitals (Olmsted County), 1987–2001, 6,076 HF patients (4,596 with echocardiography).
- **Key numbers:**
  - Overall HFpEF share of HF discharges: 47% (53% reduced EF).
  - Community-patient HFpEF share: 55% vs referral 45% (P<0.001).
  - HFpEF share trend: 38% → 47% → 54% across three 5-year periods.
  - Adjusted HR for death (HFpEF vs HFrEF): 0.96 (P=0.01); survival improved over time only for HFrEF.
- **Headline quote:** "47 percent had a preserved ejection fraction" (Abstract)
- **SAM relevance:** Unlocks HFpEF SAM cell — establishes that ~half of US HF is preserved-EF (the under-detected/under-treated subtype), justifying the HFpEF outpatient missed-dx slice of Andy's HF TAM.

### 79 — Martin et al. 2024 — AHA Heart Disease and Stroke Statistics

- **Source:** `martin-et-al-2024-2024-heart-disease-and-stroke-statistics-a-report-of-us-and-global-data-from-the-american-heart.pdf`
- **Citation:** Martin SS, Aday AW, Almarzooq ZI, et al. 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Association. Circulation. 2024;149(8):e347–e913. doi:10.1161/CIR.0000000000001209.
- **Design / N:** Annual AHA statistical update synthesizing NHANES, USRDS, GBD, and registry data through 2023.
- **Key numbers:**
  - **US HF prevalence (NHANES 2017–2020):** 6.7M Americans ≥20y; projected to >8M by 2030 (+46% from 2012).
  - HF hospital discharges 2020: 1,111,500. HF any-mention mortality 2021: 421,938.
  - **US AF prevalence (2015):** 6.6M individuals (medical claims analysis); projected from 5.2M (2010) to 12.1M (2030).
  - **Undiagnosed AF (2009 Medicare/commercial claims):** 698,900 (~13.1%) of 5.3M US AF cases undiagnosed; 535,400 in ≥65y, 163,500 in 18–64y.
  - Global AF prevalence (2021): 52.55M (95% UI 43.49–63.74M).
  - **US CKD prevalence (NHANES 2017–2020):** 14.0% overall; 9% in adults <65y; 33.2% in adults ≥65y.
  - US ESRD prevalence 2020: 807,920 (2,271 per million).
- **Headline quote:** "6.7 million Americans ≥20 years of age had HF" (Ch. 22, p.e808)
- **SAM relevance:** Unlocks multiple SAM cells simultaneously — gold-standard US denominators for HF (6.7M), AF (6.6M with 698K undiagnosed), and CKD (14% × ~258M adults = ~36M); single citation that anchors three of Andy's largest disease-area SAM rows.

### 80 — Sgreccia 2021 — Asymptomatic vs symptomatic AF: outcomes meta-analysis

- **Source:** `jcm-10-03979.pdf`
- **Citation:** Sgreccia D, Manicardi M, Malavasi VL, Vitolo M, Valenti AC, Proietti M, Lip GYH, Boriani G. Comparing outcomes in asymptomatic and symptomatic atrial fibrillation: a systematic review and meta-analysis of 81,462 patients. J Clin Med. 2021;10(17):3979. doi:10.3390/jcm10173979.
- **Design / N:** Systematic review + meta-analysis, 10 studies, 81,462 AF patients (21,007 asymptomatic, 60,455 symptomatic), ≥6-month follow-up.
- **Key numbers:**
  - Asymptomatic AF share: 26% (21,007/81,462); ≈one-third per intro citation.
  - All-cause mortality OR (asx vs sx): 1.03 (95% CI 0.81–1.32) — no difference.
  - CV death OR: 0.87 (95% CI 0.54–1.39).
  - Stroke OR: 1.22 (95% CI 0.77–1.93); stroke/TE OR: 1.06 (95% CI 0.86–1.31).
- **Headline quote:** "21,007 (26%) were asymptomatic, while 60,455 (74%) were symptomatic" (Abstract)
- **SAM relevance:** Unlocks asymptomatic-AF detection cell — establishes that ~26% of AF is silent yet carries identical stroke/mortality risk, justifying a screening-based detection TAM (≈1.7M silent AF cases in US given AHA 6.6M denominator).

### 81 — Schaffer 2017 — Rates and characteristics of paid US malpractice claims by specialty

- **Source:** `jamainternal_schaffer_2017_oi_170009.pdf`
- **Citation:** Schaffer AC, Jena AB, Seabury SA, Singh H, Chalasani V, Kachalia A. Rates and characteristics of paid malpractice claims among US physicians by specialty, 1992-2014. JAMA Intern Med. 2017;177(5):710–718. doi:10.1001/jamainternmed.2017.0311.
- **Design / N:** Comprehensive NPDB analysis, 280,368 paid claims linked to physician specialty, ~19.9M physician-years, 1992–2014.
- **Key numbers:**
  - Mean compensation per paid claim: $329,565 (overall, 2014 USD).
  - Mean payment increased 23.3% from $286,751 (1992–96) to $353,473 (2009–14).
  - Paid-claims rate declined 55.7% (20.1 → 8.9 per 1000 physician-years).
  - **Diagnostic error was the most common allegation: 31.8% of paid claims (35,349/111,066).**
  - Dx-error share by specialty: pathology 87.0%, radiology 83.9%, emergency medicine high; anesthesiology 3.5% (lowest).
  - Catastrophic claims (>$1M): 7.6% of paid claims; 32.1% involved patient death.
- **Headline quote:** "Diagnostic error was the most common type of allegation, present in 31.8%" (Abstract)
- **SAM relevance:** Unlocks malpractice-savings SAM cell — provides the per-claim dollar anchor ($329K mean) and the diagnostic-error apportionment (31.8% of paid claims) used to size Andy's avoidable-malpractice savings TAM by specialty.

### 82 — Saber Tehrani 2018 — Diagnosing stroke in acute dizziness/vertigo (FILE MISMATCH)

- **Source:** `nihms937144.pdf` (CITATION MISMATCH: this PDF is Saber Tehrani 2018 *Stroke* paper on dizziness/vertigo diagnosis, NOT the 2013 BMJ Qual Saf 25-year malpractice paper stubbed at Section A #10. This does NOT supersede stub #10 — the malpractice paper still needs separate download.)
- **Citation:** Saber Tehrani AS, Kattah JC, Kerber KA, Gold DR, Zee DS, Urrutia VC, Newman-Toker DE. Diagnosing stroke in acute dizziness and vertigo: pitfalls and pearls. Stroke. 2018;49(3):788–795. doi:10.1161/STROKEAHA.117.016979.
- **Design / N:** Narrative review of ED dizziness/vertigo diagnosis, synthesizing prior US population-based and registry estimates.
- **Key numbers:**
  - 4.4 million US ED visits/year for dizziness/vertigo (4% of all ED chief symptoms).
  - 3–5% of dizziness ED visits attributable to stroke (≈130,000–220,000/yr).
  - Annual cost of US dizziness ED workup: >$10 billion.
  - Estimated 45,000–75,000 strokes initially missed in this population annually.
  - 90% of isolated posterior-circulation TIAs not recognized at first contact.
  - Discharged "benign dizziness" patients have 50× increased stroke-hospitalization risk in next 7 days.
  - Misdiagnosis disproportionately affects age <50, women, and minorities.
- **Headline quote:** "perhaps 45,000–75,000 are initially missed" (p.2)
- **SAM relevance:** Unlocks ED stroke-miss sub-cell of Big-Three vascular dx-error TAM — quantifies the addressable annual volume (45K–75K missed strokes) and cost denominator ($10B dizziness workup spend) for Andy's ED triage module. NOTE: stub #10 (Saber Tehrani 2013 malpractice) still needs separate full-text download.

