# Diagnostic Criteria Source Tracker

Tracks Tier 1–3 sources we've scraped into `criteria_db.json`.

Status legend: ✅ done • 🟡 partial (some conditions captured) • ⬜ pending • ⏭ skip (out of scope for adult inpatient MIMIC).

---

## Tier 1 — Specialty societies / international consortia

### Cardiovascular
- ✅ **ACC / AHA / HRS** — HTN, HF (incl. HFrEF/HFmrEF/HFpEF/HFimpEF phenotypes), AF, ACS, HCM, lipids, aortic disease, NYHA, GRACE, TIMI, hypertensive emergency, AHA Jones rheumatic fever 2015, CCS angina, Killip, Forrester, WPW pattern
- ✅ **ESC / ERS** — MI (4th Universal Def), PE 2019, PH 2022, ACS 2023, pericarditis 2015/2025, IE (Duke-ISCVID 2023), syncope 2018 classification, valvular heart disease 2021 (AS / MR / AR / MS severity thresholds), ventricular arrhythmia/SCD 2022 (ICD LVEF thresholds), HCM Risk-SCD
- ✅ **ARVC Task Force 2010** — Marcus modified TFC
- ⬜ **STS / EuroSCORE II** — surgical risk (low priority for inpatient med)
- ⬜ **TAVR/TAVI eligibility tiers** (qualitative — already implied in valvular HD)

### Pulmonary / sleep / critical care
- ✅ **ATS / ERS** — IPF (2018), sarcoidosis
- 🟡 **IDSA / ATS** — CAP, HAP/VAP, TB. Gaps: NTM, HP, bronchiectasis
- ✅ **GOLD** — COPD + exacerbation
- ✅ **GINA** — asthma
- ✅ **SCCM/ESICM** — Sepsis-3, qSOFA, SOFA
- ✅ **SCAI** — cardiogenic shock stages
- ✅ **AASM** — OSA (ICSD-3)

### Renal
- ✅ **KDIGO** — AKI, CKD, CKD-MBD, anemia in CKD, BP target, AKD 2024, nephrotic syndrome, HRS
- ✅ **NKF / ASN** — CKD-EPI 2021
- ⬜ **ISN/RPS** — lupus nephritis classification
- ⬜ **KDIGO** — glomerular disease patterns (FSGS, MN, MCD, IgA)

### Hepatic
- ✅ **AASLD** — ALF (King's), decompensated cirrhosis, SBP, HRS, HE, ACLF, alcoholic hepatitis, HCC (BCLC), PBC, PSC, AIH, HBV, HCV, MASLD, hemochromatosis (2011), DILI (RUCAM + Hy's)
- ⬜ **AASLD** — Wilson disease, α1-AT deficiency, vascular liver disorders (Budd-Chiari)

### GI
- ✅ **Rome Foundation** — IBS (Rome IV), functional dyspepsia, globus
- ✅ **ACG** — celiac (2023), EoE (2025), Barrett's (2022) + Prague C&M, H. pylori (2017), gastroparesis (2022), SIBO (2020), Oakland LGIB (2023), GERD (Lyon 2.0)
- ✅ **AGA** — microscopic colitis (2016), IDA GI workup (2020)
- ✅ **ECCO / ESGAR** — IBD diagnosis
- ✅ **Tokyo Guidelines** — cholecystitis (TG18), cholangitis (TG18)
- ✅ **Forrest** — UGIB stigmata; **Glasgow-Blatchford** — pre-endoscopy risk; **Chicago Classification 4.0** — achalasia; **Marsh** — celiac histology
- ✅ **Foundational** — Atlanta pancreatitis, BISAP, Ranson, Alvarado, Hinchey, M-ANNHEIM/TIGAR-O chronic pancreatitis

### Infectious disease
- ✅ **IDSA** — CAP, UTI, CAUTI, CDI, IE (Duke-ISCVID 2023), bacterial meningitis, SSTI, HAP/VAP, TB, strep pharyngitis, asymptomatic bacteriuria, vertebral osteomyelitis (2015), Lyme (2020), invasive candidiasis (2016), invasive aspergillosis (2016), coccidioidomycosis (2016), COVID-19 diagnostics, febrile neutropenia, CRBSI, diabetic foot infection (IWGDF/IDSA 2023)
- ⬜ **IDSA** — cryptococcosis (2010 — paywalled), histoplasmosis, blastomycosis, prosthetic joint infection (AAOS-hosted), STIs
- ⬜ **EORTC / MSGERC** — invasive fungal disease

### Endocrine / metabolic
- ✅ **ADA** — diabetes, DKA, HHS, hypoglycemia, inpatient glycemic target (NICE-SUGAR)
- ✅ **Endocrine Society / ESE** — SIADH, adrenal insufficiency (primary + central), Cushing, primary aldo, hyperprolactinemia, acromegaly, thyroid storm, pheochromocytoma/paraganglioma, primary hyperparathyroidism (Fourth Workshop), male hypogonadism, hypopituitarism (incl. adult GHD + central hypothyroidism), CAH 21-OHD, PCOS, Paget's, vitamin D 2024
- ✅ **ATA** — hypothyroidism
- ✅ **GLIM / ASPEN** — malnutrition, refeeding (ASPEN 2020)
- ⬜ **Endocrine Society** — gestational DM, hyperthyroidism/Graves, MEN1/2, adrenal incidentaloma

### Hematology / oncology
- ✅ **ASH** — HIT (4Ts), ITP (2019), sickle cell, iron deficiency, TTP (PLASMIC), Khorana
- ✅ **IMWG** — multiple myeloma (SLiM-CRAB 2014)
- ✅ **iwCLL** — CLL (2018)
- ✅ **WHO / ICC** — polycythemia vera, ET/PMF driver mutations
- ✅ **ELN** — AML 2022 risk
- ✅ **Lugano** — lymphoma staging & response (2014); **IPI/R-IPI/NCCN-IPI** — DLBCL
- ✅ **PETHEMA / Sanz** — APL risk
- ✅ **Cairo-Bishop** — TLS lab + clinical criteria
- ✅ **Histiocyte Society** — HLH-2004; **Fardet** — H-Score
- ✅ **Merck Manual / Frontiers** — B12 deficiency cutoffs, hyperviscosity
- ✅ **AJCC TNM 8** — colorectal, breast (anatomic), prostate, NSCLC, melanoma, gastric, esophageal, pancreatic, RCC, bladder. ⬜ Endometrial, cervical, ovarian, head & neck, hepatocellular (covered via BCLC)
- ⬜ **NCCN** — neutropenic fever broader, oncologic emergencies (TLS captured, ALC/spinal cord compression / SVC syndrome / hypercalcemia of malignancy not yet)
- ⬜ **ACCP CHEST 2021** — VTE anticoagulation duration

### Rheumatology
- ✅ **ACR / EULAR** — RA (2010), SLE (2019), gout (2015), fibromyalgia (2016), GCA (2022), GPA/MPA/EGPA (2022), Sjögren (2016), systemic sclerosis (2013), PMR (2012), APS (2023), Takayasu (2022), IgA vasculitis (EULAR/PRINTO/PRES), IgG4-RD (2019)
- ✅ **Bohan & Peter (1975) + EULAR/ACR 2017** — myositis
- ✅ **CASPAR (2006)** — psoriatic arthritis
- ✅ **ASAS** — axSpA 2009, peripheral SpA 2011
- ✅ **Modified New York (1984)** — ankylosing spondylitis
- ✅ **Yamaguchi (1992)** — adult-onset Still's
- ✅ **Alarcón-Segovia** — MCTD
- ✅ **ILAR Edmonton 2001** — juvenile idiopathic arthritis (JIA)
- ✅ **ISG / ICBD** — Behçet
- ⬜ **ACR/EULAR** — PAN (1990 ACR, no 2022 update), Felty, Cogan, relapsing polychondritis (no validated society criteria)

### Neurology
- ✅ **AAN / international** — MS (McDonald 2017), Parkinson (MDS 2015), GBS (Brighton), brain death (AAN 2023), Bell's palsy, CAM delirium
- ✅ **ILAE** — status epilepticus (2015), seizure type classification (2017)
- ✅ **IHS** — migraine, tension, cluster (ICHD-3)
- ✅ **Friedman (2013)** — IIH
- ✅ **NINDS** — NIHSS
- ✅ **NIA-AA 2018** — Alzheimer ATN biomarker framework
- ✅ **Petersen 1999** — MCI
- ✅ **DLB Consortium 2017** — dementia with Lewy bodies
- ✅ **MDS-PSP 2017** — progressive supranuclear palsy
- ✅ **Gilman 2008** — multiple system atrophy
- ✅ **Rascovsky 2011** — bvFTD
- ✅ **MGFA 2000** — myasthenia gravis classification
- ✅ **van Swieten 1988** — modified Rankin Scale
- ✅ **Hemphill 2001** — ICH score
- ✅ **Johnston 2007** — ABCD² TIA score
- ✅ **Barber 2000** — ASPECTS
- ✅ **IRLSSG 2014** — restless legs
- ✅ **Bárány Society / AAO-HNS 2015** — Ménière's
- ✅ **AAO-HNS 2017** — BPPV / Dix-Hallpike
- ✅ **Hunt-Hess / WFNS** — SAH grading
- ✅ **Caine (1997)** — Wernicke encephalopathy
- ⬜ **El Escorial / Awaji** — ALS criteria (verbatim category text not retrieved)
- ⬜ **Boston Criteria 2.0** — CAA (Lancet Neurol behind 403)
- ⬜ **CIDP EFNS/PNS**, **narcolepsy ICSD-3**, **NIA-AA 2011 clinical AD**

### Psychiatry / substance use
- ✅ **APA DSM-5/5-TR** — MDD, GAD, AUD, schizophrenia, bipolar I/II, PTSD, panic disorder, OCD, anorexia, bulimia, BED, borderline PD, opioid use disorder, autism spectrum, schizoaffective
- ⬜ **DSM-5-TR** — adult ADHD (paraphrased only), DSM delirium block, acute stress disorder (inconsistent counts), adjustment disorder, antisocial PD, neurocognitive disorders detail
- ⬜ **ICD-11** alternative

### Allergy / immunology
- ✅ **WAO 2020** — anaphylaxis
- ⬜ **AAAAI / EAACI** — food allergy, chronic urticaria, mastocytosis

### Dermatology, ophthalmology, urology
- ⬜ Not yet swept (low-priority for MIMIC adult inpatient)

### Orthopedics / trauma
- ✅ **Ottawa / NEXUS / Canadian C-Spine** — imaging decision rules
- ✅ **Larach** — malignant hyperthermia (AAGBI)
- ⬜ **Gustilo-Anderson** — open fracture, **AVN ARCO**

### Ob/Gyn
- ✅ **ACOG** — preeclampsia/eclampsia (2020)
- ⬜ **ACOG / IADPSG / Carpenter-Coustan** — gestational DM (Endocrine Society retired this)

### Anesthesia / pain
- ✅ AAGBI / MHAUS — malignant hyperthermia

---

## Tier 2 — Reference compilations
- 🟡 **Merck Manual** — electrolyte definitions, B12 cutoffs
- 🟡 **StatPearls (NCBI)** — Wolff-Parkinson-White, used as DSM mirror; multiple
- 🟡 **AAFP** — used opportunistically
- 🟡 **Frontiers/PMC reviews** — hyperviscosity, MS criteria validation

---

## Tier 3 — Government / regulatory / public health
- ✅ **USPSTF** — lung cancer screening (2021), AAA (2019), statin primary prevention (2022), aspirin CVD (2022), HCV (2020), CRC (2021), breast cancer (2024), cervical cancer (2018), prediabetes/T2DM (2021), osteoporosis (2018), adult depression (2023)
- ✅ **CDC / CSTE NNDSS case definitions** — COVID-19 (2023), gonorrhea (2014), primary/secondary syphilis (2018), Lyme (2022), pertussis (2020), measles (2013), acute HBV (2012), acute HCV (2020), legionellosis (2005), salmonellosis (2017)
- ✅ **CDC** — TB diagnosis (with IDSA), HIV laboratory algorithm (2014)
- ⬜ **CSTE** — chlamydia (too thin), MIS-A/MIS-C (404), mumps/rubella, anaplasmosis/ehrlichiosis, Q fever, babesiosis, shigellosis, STEC, listeriosis, CRE, C. auris
- ⬜ **USPSTF gaps** — latent TB screening, hypertension screening criteria, GDM screening, unhealthy alcohol SBIRT, hepatitis B universal screening
- ⬜ **CDC NHSN** — CLABSI 2024, SSI, VAE
- ⬜ **NIH** — NIH Stroke Scale ✅; bone health consensus, ARDS Network

---

## Tier 4 — Foundational papers (incorporated where canonical)
Wells DVT/PE, BISAP, Ranson, Alvarado, Hinchey, Child-Pugh, MELD-Na, Glasgow-Blatchford, ISTH DIC, Berlin ARDS, Atlanta pancreatitis, ADD-RS, GRACE, TIMI, CHA₂DS₂-VASc, HAS-BLED, Khorana, PERC, PLASMIC, Hunter, Caine, Brighton, NIHSS, Centor, CSRS, Forrest, Killip, Forrester, CCS angina, MGFA, mRS, ICH score, ABCD², ASPECTS, Petersen MCI, Cairo-Bishop TLS, HLH-2004, H-Score, Sanz APL, IPI lymphoma, Yamaguchi Still's, Marsh celiac, Prague C&M Barrett's

---

## Coverage snapshot (current)
- **Total conditions in `criteria_db.json`: 298** (up from 52 at start of brute-sweep)
- **Wave 1 contribution (8 parallel agents):** IDSA 10 + AASLD 1 (hemochromatosis consolidated) + Endocrine 11 + ACR/EULAR 10 + ASH heme-onc 13 + AAN/MDS 15 + ACG/AGA 13 + DSM 13 = ~86 new entries
- **Wave 2 contribution (3 parallel agents):** AJCC TNM 11 + ESC remaining cardio 13 + CDC/USPSTF 21 = 45 new entries
- **Net brute-sweep yield: ~131 new criteria entries** added by parallel-agent harvest across ~14 specialty domains in 2 waves
- **Hard-rule compliance verified per agent**: all entries carry verbatim quote + resolvable source URL; no fabricated cutoffs

## Remaining gaps if you want a Wave 3
- **Onc:** endometrial/cervical/ovarian/head & neck TNM, NCCN oncologic emergencies (spinal cord compression, SVC syndrome, hypercalcemia of malignancy), ACCP CHEST 2021 VTE duration
- **Hepatology:** Wilson, α1-AT, Budd-Chiari, portal vein thrombosis
- **Renal:** ISN/RPS lupus nephritis, KDIGO glomerular pattern criteria
- **Rheum:** PAN (1990 ACR), Felty, Cogan, relapsing polychondritis — most lack society criteria
- **Neuro:** El Escorial/Awaji ALS, Boston CAA 2.0, CIDP EFNS/PNS, narcolepsy ICSD-3
- **Endo:** gestational DM (IADPSG/Carpenter-Coustan via ACOG), Graves, MEN1/2, adrenal incidentaloma (ESE 2023)
- **Tier 3:** CDC chlamydia/mumps/rubella/anaplasmosis/babesiosis/shigellosis/STEC/listeriosis case definitions; USPSTF latent TB, hypertension, GDM screening
- **Specialty domains not yet swept:** dermatology (AAD), ophthalmology (AAO), urology (AUA), obstetrics beyond preeclampsia
