# DDx Results — model: `opus`

**Cases scored:** 37

| Metric | Hits | Rate |
|---|---|---|
| hit@1 | 30/37 | 81% |
| hit@3 | 35/37 | 95% |
| hit@5 | 36/37 | 97% |

**Tokens** — input: 67,838 · output: 20,084

## Per-case detail

### Case 01 — abdominal_pain_consult

**Gold terms:** abdominal pain, lower quadrant, abdominal, sigmoid, diverticulitis, tenderness

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | acute sigmoid diverticulitis | 7-8 day history of LLQ abdominal pain with focal tenderness and palpable mass/fullness in left lower quadrant in a 71-year-old, partially treated with Cipro/Flagyl. |
| 2 | sigmoid colon carcinoma | Elderly female with persistent LLQ pain, palpable mass, anorexia, obstipation, elevated alkaline phosphatase, and colonoscopy 5 years ago raises concern for colonic malignancy. |
| 3 | diverticular abscess | Persistent LLQ pain with palpable fullness/mass and obstipation despite outpatient oral antibiotics suggests a walled-off complication of diverticulitis. |
| 4 | partial large bowel obstruction | Obstipation with last BM two days ago, anorexia, and palpable LLQ mass suggest a partially obstructing sigmoid lesion. |
| 5 | ovarian or adnexal mass | Postmenopausal female on Premarin with palpable LLQ mass and grade 4 pelvic prolapse warrants consideration of an adnexal pathology despite prior hysterectomy. |

### Case 03 — consult_chest_pain_1

**Gold terms:** chest pain 1, chest pain, emergency room, dull ache, precordial, shortness of breath

**Result:** hit at rank **2**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Anxiety-related non-cardiac chest pain | Stress-triggered episodic chest pain with no exertional relation, normal EKG/cardiac enzymes/CXR, prior negative nuclear perfusion scan, and home medications Paxil and BuSpar suggesting underlying anxiety disorder. |
| 2 | Coronary artery vasospasm (Prinzmetal angina) | Prior catheterization showed a right coronary artery finding thought to be spasm, with recurrent precordial pressure unrelated to exertion in an active smoker. |
| 3 | Gastroesophageal reflux disease | Episodic dull retrosternal pressure without exertional component in a smoker, with normal cardiac workup, is commonly attributable to esophageal etiology. |
| 4 | Musculoskeletal/costochondral chest pain | Intermittent precordial discomfort over several days without diaphoresis or exertional trigger and a completely benign cardiopulmonary exam supports a chest wall origin. |
| 5 | Stable atypical angina / early coronary artery disease | Multiple risk factors (active smoking, borderline hyperlipidemia on pravastatin, strong paternal CAD history) warrant consideration despite prior negative perfusion imaging. |

### Case 04 — consult_syncope

**Gold terms:** hypertension, hyperlipidemia, shortness of breath, coronary artery disease, seizure activity, seizure disorder

**Result:** hit at rank **2**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Orthostatic hypotension secondary to Parkinson's disease (autonomic dysfunction) | Recently diagnosed Parkinson's disease is commonly associated with autonomic dysfunction causing orthostatic syncope, and the patient is also on propranolol which can potentiate hypotension. |
| 2 | Medication-induced syncope (propranolol/Flomax) | Patient is on propranolol (bradycardia/hypotension risk) and Flomax (alpha-blocker causing orthostatic hypotension), a common combination precipitating syncope in elderly patients. |
| 3 | Cardiac arrhythmia (e.g., paroxysmal AV block or sinus pause) | Sudden syncope without prodromal chest pain or palpitations in a 69-year-old with hypertension, displaced PMI, and beta-blocker use raises concern for transient bradyarrhythmia not captured on resting EKG. |
| 4 | Seizure (unprovoked, possibly secondary) | Patient reportedly had seizure-like activity prior to the syncopal event, warranting consideration of a primary seizure despite unremarkable head CT. |
| 5 | Vasovagal (neurocardiogenic) syncope | Syncope without antecedent chest pain, palpitations, or focal neurologic findings, with negative cardiac enzymes and unremarkable head CT, is consistent with a neurally-mediated etiology. |

### Case 06 — cough_abdominal_pain

**Gold terms:** cough abdominal pain, abdominal pain, cough, pneumonia, body aches, bronchitis

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Community-acquired pneumonia | Fever 100.1, cough, body aches, coarse bilateral basal breath sounds, and prior pneumonia history in an elderly former heavy smoker. |
| 2 | Acute bronchitis | Two-day dry cough with subjective fevers/chills and body aches without focal consolidation findings. |
| 3 | Influenza | Acute onset of generalized body aches, dry cough, fevers/chills, and nausea over two days. |
| 4 | Musculoskeletal chest/abdominal wall strain (cough-induced) | Right-sided abdominal pain occurring only with coughing, with soreness on palpation but no rebound or guarding. |
| 5 | Sepsis with dehydration | Fever with marked tachycardia (HR 144) and dry mucous membranes suggest systemic infection with volume depletion. |

### Case 08 — er_report_chest_pain_fever

**Gold terms:** er report chest pain fever, chest pain, fever, hypertension, acute myocardial infarction, urinary tract infection

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute uncomplicated urinary tract infection with systemic febrile response | Positive nitrites, leukocyte esterase, 5-10 WBC/hpf, 1+ bacterial rods on UA, leukocytosis of 12,200, and 2 days of fever on outpatient nitrofurantoin therapy. |
| 2 | Atypical (non-cardiac) chest pain | Substernal chest discomfort with normal EKG, three negative troponins, CK-MB 1.0, BNP 26, normal stress test, and AMI ruled out during admission. |
| 3 | Stable angina / coronary artery disease risk | Substernal pain with nausea, diaphoresis, and dizziness in a 48-year-old diabetic, hypertensive, hyperlipidemic woman with strong family history of early CAD in father and brother in their 40s. |
| 4 | Gastroesophageal reflux disease | Substernal chest discomfort with negative cardiac workup, on Zantac, and chronic NSAID (Mobic) use predisposing to upper GI symptoms. |
| 5 | Musculoskeletal/cervical strain | Neck and head discomfort with normal lumbar puncture, no neurologic deficits, known arthritis on Mobic, and nonfocal neurologic exam. |

### Case 106 — feeling_dizzy_er_visit

**Gold terms:** feeling dizzy, hypertension, tachycardia, smoking, dizzy, heart rate

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | early alcohol withdrawal syndrome | Daily heavy alcohol use (5 glasses wine/day) with last drink the prior evening, presenting with palpitations, tachycardia (HR 121), and hypertension (195/83); patient herself reports being 'close to withdrawal.' |
| 2 | hypertensive urgency due to medication noncompliance | Known hypertensive off medications for months presenting with BP 195/83 and dizziness, responsive to beta-blockade. |
| 3 | sinus tachycardia secondary to sympathetic hyperactivity | EKG confirms sinus tachycardia at 121 without ischemic changes, consistent with adrenergic surge from withdrawal/untreated HTN. |
| 4 | alcoholic liver disease (compensated) | Facial telangiectasias and chronic heavy daily alcohol intake suggest underlying liver disease, though LFTs are currently normal. |
| 5 | hypokalemia | Serum potassium of 3.4 in the setting of chronic alcohol use may contribute to palpitations and arrhythmogenic risk. |

### Case 115 — gen_med_consult_10

**Gold terms:** gen med  10, hemoglobin a1c, diarrhea, diabetes mellitus type ii, hypertension, hypercholesterolemia

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Rheumatoid arthritis | Symmetric polyarthralgia with doughy swelling of bilateral MCP joints and wrists, decreased mobility, and chronic anemia (Hgb 10.5) in an elderly female unresponsive to NSAIDs. |
| 2 | Osteoarthritis (polyarticular) | Age 77 with diffuse joint pain involving hands and wrists, slow movement, and history of osteoporosis without erythema or systemic inflammatory features. |
| 3 | Polymyalgia rheumatica | Elderly woman with diffuse musculoskeletal pain, decreased mobility, fatigue/depressive symptoms, and anemia of chronic disease, though distribution is more distal than typical. |
| 4 | Hyperparathyroidism (recurrent/persistent) | Persistent borderline-high calcium (10.8) after prior parathyroidectomy with diffuse bone/joint pain, osteoporosis, and depressive symptoms. |
| 5 | Major depressive disorder | Patient restarted Zoloft for depressed mood, hypersomnia, and feeling 'not herself,' which can amplify diffuse somatic/joint pain complaints. |

### Case 118 — gen_med_consult_12

**Gold terms:** gen med  12, history of diabetes, dyspnea on exertion, uncertain etiology, weak, syncope

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | anemia (likely chronic, possibly iron deficiency) | 75-year-old woman with progressive weakness, shakiness, and dyspnea on exertion with normal O2 saturation, clear lungs, no edema, and history of peptic ulcer disease suggesting possible chronic GI blood loss. |
| 2 | stable coronary artery disease / chronic ischemic heart disease | Self-reported underlying heart disease, family history of CAD, nonspecific ST-segment changes on ECG, and exertional dyspnea in an elderly patient with hypertension and diabetes. |
| 3 | congestive heart failure (HFpEF) | Elderly woman with hypertension, diabetes, family history of CHF, and progressive exertional dyspnea, though absence of edema, JVD, and clear lungs makes this less typical. |
| 4 | recurrent pulmonary embolism | Prior PE four years ago with worsening exertional dyspnea, though normal O2 saturation at rest and with exertion lowers likelihood. |
| 5 | uncontrolled type II diabetes mellitus with hyperglycemia or hypoglycemia | Known diabetic not currently taking medications, presenting with weakness, shakiness, and confusion, classic symptoms of glycemic dysregulation. |

### Case 119 — gen_med_consult_14

**Gold terms:** gen med  14, left otalgia, otalgia, serous otitis, atopic dermatitis, serous

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | left serous otitis media with effusion | Left TM with effusion on exam, three weeks of left otalgia and decreased hearing that is improving. |
| 2 | acute or chronic left maxillary sinusitis | Left-sided sinus pressure, referred upper tooth pain (dental evaluation negative), and history of recurrent sinusitis. |
| 3 | eustachian tube dysfunction | Subacute unilateral ear fullness, hearing loss, and middle ear effusion in the setting of sinus symptoms. |
| 4 | temporomandibular joint dysfunction | Persistent left-sided jaw pain and chronic left-sided headache without dental pathology. |
| 5 | atopic dermatitis flare | Scattered erythematous plaques with lichenification on the nuchal region and popliteal fossae, with prior good response to Cutivate. |

### Case 120 — gen_med_consult_15

**Gold terms:** gen med  15, tearfulness, mood swings, menopause, postsurgical menopause, mood swings and tearfulness

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | major depressive disorder | Patient presents with months of worsening tearfulness, dysthymic mood, insomnia, and difficulty concentrating impairing work function, with prior good response to Wellbutrin. |
| 2 | surgical menopause-related mood disorder | Status post TAH with BSO in 2003 with abrupt loss of ovarian hormones can precipitate mood swings, tearfulness, and insomnia. |
| 3 | adjustment disorder with depressed mood | Mood swings and tearfulness over recent months affecting work performance could reflect a reactive process, though no clear stressor is documented. |
| 4 | generalized anxiety disorder | Insomnia, difficulty concentrating, and emotional lability can reflect underlying anxiety, and her history of OCD-spectrum overeating suggests anxiety vulnerability. |
| 5 | hypothyroidism | Depressed mood, insomnia, and poor concentration in a 50-year-old female warrant thyroid evaluation despite no thyromegaly on exam. |

### Case 121 — gen_med_consult_16

**Gold terms:** gen med  16, short-term memory loss, anxiety, short term memory loss, memory loss, stress issues

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Major depressive disorder with cognitive symptoms (pseudodementia) | Patient is on Zoloft 100 mg daily, has been widowed 11 years after traumatic loss of husband in MVA, and reports 5-10 years of significant stress with subjective memory complaints. |
| 2 | Generalized anxiety disorder / chronic stress-related cognitive impairment | She describes her T-Mobile job as 'very demanding and high stress' with difficulty absorbing technical information and deadlines, suggesting stress-induced concentration difficulties. |
| 3 | Adjustment disorder with chronic occupational stress | Memory concerns coincide with demanding new job requiring technical learning and customer service protocols she feels overwhelmed by. |
| 4 | Mild cognitive impairment (MCI) | 60-year-old presenting with subjective short-term memory loss warrants consideration of early MCI, though objective neurologic exam is normal. |
| 5 | Medication-induced cognitive impairment | Patient is on multiple CNS-active medications including Zoloft, Zyrtec (anticholinergic), and HCTZ which could contribute to subjective cognitive complaints. |

### Case 132 — gen_med_consult_31

**Gold terms:** gen med  31, cerebrovascular accident, recurrent urinary tract infection, diabetes, hypoglycemia, neuropathy

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | hypoglycemic encephalopathy | Found unresponsive with blood glucose of 40 due to poor PO intake while on Humulin N 30 units BID, with persistent altered mental status even after D50 administration. |
| 2 | urosepsis / complicated urinary tract infection | Chronic indwelling Foley catheter, recurrent UTIs, recently started Cipro, urine with 20 WBCs and initial cloudy appearance, with altered mental status as the presenting symptom in this elderly patient. |
| 3 | acute kidney injury (likely prerenal/septic) | BUN 48 and creatinine 2.8 with poor PO intake, Lasix use, and possible underlying infection, which can also impair drug clearance and worsen encephalopathy. |
| 4 | acute ischemic stroke (recurrent CVA) | Worsening aphasia beyond baseline, decreased consciousness, and right-sided weakness (3-4/5) in a patient with prior right CVA, atrial fibrillation, and subtherapeutic INR of 1.1 on Coumadin. |
| 5 | medication-induced toxic encephalopathy | Polypharmacy with multiple CNS-active agents (Percocet QID, Neurontin, Flexeril, Reglan) in setting of acute kidney injury (Cr 2.8) likely causing drug accumulation. |

### Case 133 — gen_med_consult_34

**Gold terms:** gen med  34, chronic abdominal, evaluation, chronic, epigastric, bowel

**Result:** **MISS**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Pancreatic neuroendocrine tumor with hepatic metastases | Young patient with extensive pancreatic body/tail mass, innumerable bilobar liver masses, chronic epigastric pain radiating to back, weight loss, and diarrhea suggests a functional or non-functional pNET (e.g., gastrinoma/VIPoma) given the indolent presentation in a 23-year-old. |
| 2 | Pancreatic adenocarcinoma with hepatic metastases | Pancreatic body/tail mass invading left kidney with numerous liver metastases, 20-lb weight loss, epigastric pain radiating to back, and guaiac-positive stool fit pancreatic carcinoma despite the patient's young age. |
| 3 | Pancreatic solid pseudopapillary neoplasm or acinar cell carcinoma | Large pancreatic mass with metastatic liver disease in a young patient raises consideration of these rarer pancreatic neoplasms that occur in younger adults. |
| 4 | Lymphoma (pancreatic/hepatic involvement) | Young male with B-symptoms (weight loss, poor appetite), hepatomegaly with irregular border, multiple liver lesions, pancreatic mass, and possible splenic involvement is consistent with extranodal lymphoma. |
| 5 | Metastatic germ cell tumor | Young male with extensive retroperitoneal/pancreatic mass and innumerable liver metastases warrants consideration of germ cell malignancy, although testicular exam was unremarkable an extragonadal primary is possible. |

### Case 134 — gen_med_consult_35

**Gold terms:** gen med  35, fluticasone nasal inhaler, confusion and hallucinations, blood pressure, temperature, abdomen

**Result:** hit at rank **2**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | pheochromocytoma | Episodic hypertension (186/101), tachycardia, night sweats, weight loss, lightheadedness, hyperdynamic precordium, and abdominal/femoral bruits with new psychiatric symptoms suggest catecholamine excess. |
| 2 | hyperthyroidism (thyrotoxicosis) with thyroid storm | Tachycardia, hypertension, low-grade fever, weight loss, anxiety, insomnia, hyperdynamic precordium, and acute psychosis are classic for thyrotoxicosis. |
| 3 | Cushing syndrome | Hypertension, acneiform truncal eruption, psychiatric disturbance with euphoria/psychosis, and hyperadrenergic features suggest cortisol excess. |
| 4 | primary psychotic disorder (first-episode schizophrenia/schizophreniform) | Age 27, family history of psychiatric illness, paranoid delusions of being poisoned, and auditory/visual hallucinations fit a primary psychotic illness. |
| 5 | neurosyphilis | Young immigrant from Brazil presenting with subacute confusion, disorientation, hallucinations, euphoric mood, and impaired executive function is consistent with general paresis. |

### Case 135 — gen_med_consult_36

**Gold terms:** gen med  36, decreased range of motion, coughing up blood, chest, interstitial, infiltrates

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Eosinophilic granulomatosis with polyangiitis (Churg-Strauss syndrome) | Long-standing allergic rhinitis, migratory polyarthralgias, pulmonary infiltrates with hemoptysis, and pauci-immune crescentic glomerulonephritis with prominent eosinophilic interstitial infiltrate strongly suggest EGPA. |
| 2 | Granulomatosis with polyangiitis (Wegener's) | Upper airway symptoms, scleritis/ocular involvement, pulmonary infiltrates with hemoptysis, and pauci-immune crescentic GN fit a classic ANCA-associated vasculitis presentation. |
| 3 | Microscopic polyangiitis | Pulmonary-renal syndrome with hemoptysis, pauci-immune crescentic glomerulonephritis on biopsy, and absence of immune deposits on immunofluorescence is characteristic of MPA. |
| 4 | Anti-GBM disease (Goodpasture syndrome) | Pulmonary hemorrhage with hemoptysis, ground-glass infiltrates, and crescentic glomerulonephritis with rust-colored urine raise concern, though pauci-immune pattern and arthralgias make it less likely. |
| 5 | Systemic lupus erythematosus with pulmonary-renal involvement | Young African American woman with polyarthralgias, ocular symptoms, hematuria, and pulmonary hemorrhage could suggest SLE, though absent immune complex deposition on biopsy argues against it. |

### Case 136 — gen_med_consult_37

**Gold terms:** gen med  37, liver biopsy, dark urine, generalized weakness, lymph nodes, granulomatous

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | cholangiocarcinoma or pancreatic head adenocarcinoma with biliary obstruction | Painless jaundice with dark urine, 26-pound weight loss, anorexia, hepatomegaly, and RUQ tenderness in a 40-year-old suggests malignant biliary obstruction. |
| 2 | hepatocellular carcinoma | Hepatomegaly with palpable liver edge 3 cm below costal margin, splenomegaly, jaundice, weight loss, and family history of cirrhosis in brother raise concern for HCC, possibly on undiagnosed chronic liver disease. |
| 3 | viral hepatitis (acute or chronic hepatitis B or C) | Jaundice, dark urine, fatigue, anorexia, low-grade constitutional symptoms, hepatomegaly with splenomegaly support viral hepatitis, particularly in Hispanic male demographic with familial cirrhosis. |
| 4 | lymphoma (e.g., non-Hodgkin lymphoma) with hepatic involvement | B-symptoms (night sweats, fever, weight loss), bilateral inguinal lymphadenopathy with 2 cm node, hepatosplenomegaly suggest lymphoproliferative disease. |
| 5 | primary sclerosing cholangitis or autoimmune hepatitis | Cholestatic picture with jaundice, hepatomegaly, splenomegaly, and prior cholecystectomy in setting of constitutional symptoms warrants consideration of autoimmune biliary/hepatic disease. |

### Case 138 — gen_med_consult_39

**Gold terms:** gen med  39, abdominal pain, nausea, vomiting, fever, altered mental status

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute adrenal crisis due to bilateral adrenal hemorrhage (Waterhouse-Friderichsen syndrome) | CT shows a 3.5cm R adrenal mass and edematous L adrenal with retroperitoneal/perinephric stranding, plus hypotension refractory to IVF, hyponatremia (Na 127), hyperkalemia tendency, fever, altered mentation, and family history of Addison's disease. |
| 2 | Septic shock with bacteremia (likely meningococcal or other gram-negative source) | Fever 102.9, HR 145, BP 99/50 after 4L IVF, leukocytosis 15.6 with 16% bands, altered mental status, and adrenal findings suggestive of Waterhouse-Friderichsen pattern. |
| 3 | Extensive acute deep vein thrombosis of right lower extremity with possible paradoxical embolism | Doppler shows total DVT of distal external iliac, common femoral, profunda, femoral, and greater saphenous veins with R calf/thigh swelling, and TEE reveals a PFO with right-to-left shunt. |
| 4 | Antiphospholipid syndrome / hypercoagulable state with adrenal vein thrombosis | Massive unprovoked iliofemoral DVT plus bilateral adrenal abnormalities and family history of SLE raise concern for APS-related adrenal infarction/hemorrhage. |
| 5 | Bacterial meningoencephalitis secondary to complicated sinusitis | Pansinusitis with acute and chronic features on MRI, fever, altered mental status, lethargy, and disorientation prompted LP and empiric ceftriaxone in the ER. |

### Case 14 — gen_med_h_p_2

**Gold terms:** gen med h p 2, weakness, malaise, dyspnea on exertion, weight loss, atypical pneumonia

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Pneumocystis jirovecii pneumonia in the setting of advanced HIV/AIDS | Hypoxemia (pO2 46 on room air), bilateral interstitial infiltrates, oral thrush, cachexia, generalized lymphadenopathy, and high-risk sexual exposure in Haiti (1982) strongly suggest PCP in an AIDS patient. |
| 2 | Disseminated tuberculosis | Fever 101.6°F, weight loss of 15 lbs, bilateral pulmonary infiltrates, generalized lymphadenopathy (including epitrochlear), and likely immunocompromise raise concern despite negative PPD in 1994 (anergy possible). |
| 3 | Disseminated histoplasmosis | Cachexia, fever, bilateral interstitial infiltrates, hepatic involvement (AST 131, bilirubin 2.4), generalized lymphadenopathy, and skin nodules in a likely AIDS host fit disseminated endemic mycosis. |
| 4 | Kaposi sarcoma with pulmonary involvement | Multiple subcutaneous nodules on the chest wall, pale palms, lymphadenopathy, and bilateral pulmonary infiltrates in a man with Haitian homosexual exposure history are classic for AIDS-associated KS. |
| 5 | Non-Hodgkin lymphoma (AIDS-related) | Marked diffuse lymphadenopathy including epitrochlear nodes, B-symptoms (weight loss, fever), elevated total protein with hepatic transaminitis, and subcutaneous nodules suggest lymphomatous infiltration. |

### Case 143 — gen_med_consult_47

**Gold terms:** gen med  47, inflammatory, degenerative, fever, lumbar spine, sacroiliac joint

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Septic sacroiliitis (pyogenic SI joint infection) | Severe unilateral left sacroiliac pain with high fever (104°F), pain on any movement/positioning, and localized SI joint tenderness in a febrile elderly patient is classic for septic sacroiliitis. |
| 2 | Brucellosis | Patient lives on a ranch in Mexico raising goats and cattle (classic exposure), with fever, chills, sacroiliitis, lymphadenopathy, and febrile agglutinins were ordered—brucellosis has a strong predilection for the SI joint. |
| 3 | Vertebral osteomyelitis/discitis with paraspinal or epidural abscess | Fever with focal lumbosacral pain, new hyperglycemia, and prior sacral abscess history raise concern, though current MRI was unremarkable—evolving infection is still possible. |
| 4 | Psoas or pelvic abscess | Spiking fevers, severe pelvic/hip pain worsened by movement, bilateral inguinal lymphadenopathy, and new-onset hyperglycemia suggest a deep pelvic suppurative process despite initial imaging. |
| 5 | Endocarditis with septic embolic seeding to sacroiliac joint | Persistent high fevers with chills, new musculoskeletal focus of infection, and ongoing blood cultures in an elderly patient raise suspicion for bacteremia from an endovascular source. |

### Case 147 — gen_med_consult_51

**Gold terms:** gen med  51, abdominal pain, nausea, vomiting, small bowel obstruction, nausea and vomiting

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Adhesive small bowel obstruction | 89-year-old with multiple prior abdominal surgeries (colon resection, cholecystectomy, appendectomy), 20 prior SBO episodes, presenting with postprandial abdominal pain, nausea, vomiting, distention, hypoactive bowel sounds, and dilated fluid-filled loops on CT. |
| 2 | Partial small bowel obstruction | CT shows dilated fluid-filled loops without a clear transition point, and patient experienced temporary pain relief after vomiting, consistent with incomplete obstruction. |
| 3 | Paralytic ileus | Diffuse abdominal tenderness with hypoactive bowel sounds, distention, and dilated loops on CT without obvious mechanical obstruction support a functional ileus. |
| 4 | Mesenteric ischemia | Elderly patient on antihypertensives with severe 8/10 abdominal pain disproportionate to benign exam findings, leukocytosis (WBC 12.1), and hemoconcentration (Hgb 16.9/Hct 52.1) raise concern for ischemia. |
| 5 | Recurrent or metachronous colon carcinoma with obstruction | Remote history of colon cancer with partial resection, advanced age, and presentation with bowel dilatation warrants consideration of malignant recurrence as an obstructive etiology. |

### Case 16 — flank_pain_consult

**Gold terms:** flank pain, unable to urinate, urinary tract infection, flank

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute pyelonephritis | Left flank pain with 3+ bacteriuria on urinalysis and focal ileus on CT in the left upper quadrant suggest renal/perirenal inflammation. |
| 2 | Uncomplicated urinary tract infection (cystitis) | Difficulty urinating combined with 3+ bacteria on urinalysis in a female patient supports a lower UTI. |
| 3 | Recently passed ureteral calculus | Acute left flank pain with associated localized ileus that has now improved, despite no stone seen on current CT, is consistent with a recently passed stone. |
| 4 | Localized paralytic ileus | CT demonstrated focal ileus in the left upper quadrant without obstruction, free air, or bowel wall thickening. |
| 5 | Musculoskeletal flank pain / renal contusion sequela | History of prior left kidney bruising from an MVA and localized flank tenderness with benign abdomen and normal hematocrit could reflect musculoskeletal pain. |

### Case 24 — lightheaded_dizziness

**Gold terms:** lightheaded dizziness, passing out, echocardiogram, cardiac catheterizatio, normal sinus rhythm, cardiac enzyme

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | paroxysmal supraventricular tachycardia | Transient palpitations with racing heart and chest fluttering that resolved by ER arrival with normal sinus rhythm on EKG, classic for self-terminating PSVT in a 50-year-old female. |
| 2 | vasovagal presyncope | Lightheadedness and near-syncope without actual loss of consciousness, with normal vital signs and benign exam, fits a neurocardiogenic etiology. |
| 3 | perimenopausal vasomotor symptoms | 50-year-old female with episodic palpitations, lightheadedness, and prior negative cardiac workup (normal cath and echo) is consistent with perimenopausal autonomic symptoms. |
| 4 | premature atrial or ventricular contractions (ectopy) | Sensation of fluttering and palpitations with otherwise normal EKG and incomplete RBBB suggests transient ectopic beats not captured at presentation. |
| 5 | anxiety/panic attack | Episodic palpitations, lightheadedness, and shortness of breath with completely normal cardiac workup including prior normal catheterization and echocardiogram supports a somatic anxiety etiology. |

### Case 27 — dysphagia_hematemesis

**Gold terms:** dysphagia hematemesis, gi prophylaxis, hiv medications, alcohol abuse, weight, prophylaxis

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Esophageal food bolus impaction with underlying achalasia | CT shows diffuse esophageal dilatation with retained food after eating eggplant parmigiana, with acute dysphagia and globus sensation, classic for food impaction in a dilated/achalasic esophagus. |
| 2 | Mallory-Weiss tear | Hematemesis occurring after forceful vomiting against an obstructed esophagus is consistent with a mucosal tear at the gastroesophageal junction. |
| 3 | Esophageal candidiasis | Untreated HIV (off ART for 2-3 months) with new dysphagia and food impaction raises concern for opportunistic esophagitis causing strictures or dysmotility. |
| 4 | Esophageal stricture or malignancy | Marked esophageal dilatation with retained food suggests chronic distal obstruction; mild anemia (Hgb 10.4) and HIV/HCV history raise concern for an underlying stricture or neoplasm. |
| 5 | Boerhaave syndrome (esophageal perforation) | Severe constant 8/10 chest/back pain with hematemesis after vomiting warrants consideration, though absence of mediastinal air on CT makes this less likely. |

### Case 29 — lower_quadrant_pain

**Gold terms:** lower quadrant pain, right lower quadrant pain, white blood cell count, lower quadrant, bilirubin, quadrant

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | acute appendicitis | Classic presentation with 24-hour RLQ pain, fever 38.7, leukocytosis 20,000, positive Rovsing and obturator signs; CT non-visualization of the appendix does not rule it out. |
| 2 | tubo-ovarian abscess or pelvic inflammatory disease | Sexually active premenopausal female with RLQ pain, fever 38.7, leukocytosis, and pyuria (WBC 10-25) without dysuria raises concern for adnexal/pelvic infection. |
| 3 | ovarian torsion or hemorrhagic ovarian cyst | Sudden severe stabbing RLQ pain in a premenopausal woman with irregular menses and positive obturator sign suggests an adnexal pathology. |
| 4 | right ureterolithiasis (nephrolithiasis) | RLQ pain radiating to the right flank with hematuria on UA (blood 50, RBCs 2-5) is suggestive of a ureteral stone. |
| 5 | ectopic pregnancy | Premenopausal sexually active woman with irregular menses (1-2 months between cycles), unilateral RLQ pain, and prior tubal pregnancy history places her at high risk. |

### Case 32 — dizziness_recurrent

**Gold terms:** dizziness recurrent, recurrent dizziness, shortness of breath, rotational sensation, earache, headaches

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Benign paroxysmal positional vertigo (BPPV) | Rotational vertigo triggered by positional changes (arising from bed/chair, rolling over, looking up) lasting minutes is classic for BPPV. |
| 2 | Orthostatic hypotension/presyncope | Patient describes near-syncope with positional change and is on multiple antihypertensives (Diovan, Coreg, furosemide) plus diuretic therapy that can precipitate orthostasis. |
| 3 | Vertebrobasilar insufficiency | Elderly woman with atrial fibrillation, prior stroke, HTN, DM, and dizziness provoked by neck movement (turning right/left, looking up) raises concern for posterior circulation ischemia. |
| 4 | Medication-induced dizziness | She held Percocet and Ultram due to suspicion they were exacerbating dizziness, and remains on multiple CNS/cardiovascular agents (Coreg, Diovan, furosemide, Amaryl) that can cause dizziness. |
| 5 | Meniere's disease | Episodic vertigo accompanied by right-sided tinnitus suggests a peripheral cochleovestibular disorder such as Meniere's. |

### Case 34 — neuro_consult_leg_weakness

**Gold terms:** neuro  leg weakness, hyperckemia, emg and nerve, nerve conduction studies, leg weakness, leg

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | L5-S1 radiculopathy | Asymmetric right lower extremity weakness in L5/S1 distribution (ankle dorsiflexion, eversion, toe flexion), absent ankle jerks, steppage gait, and chronic back pain with degenerative changes on CT. |
| 2 | Common peroneal (fibular) neuropathy | Right ankle dorsiflexion and eversion weakness with a positive Tinel's sign at the right fibular head and steppage gait. |
| 3 | Amyotrophic lateral sclerosis (ALS) | Asymmetric leg weakness with muscle atrophy of right hamstrings/calf/quadriceps, fasciculations in both calves, hyperCKemia, and inability to do toe raises bilaterally suggesting more diffuse motor neuron involvement. |
| 4 | Diabetic/alcoholic length-dependent peripheral polyneuropathy | History of diabetes and heavy alcohol use with diminished vibratory sense at toes, absent ankle jerks, distal tingling, and bilateral Tinel's signs at elbows suggesting susceptibility to compressive neuropathies. |
| 5 | Inclusion body myositis | Middle-aged male with asymmetric distal lower extremity weakness, muscle atrophy, persistently elevated CK (500-1000) independent of statin use, and chronic indolent course. |

### Case 36 — h_p_weakness

**Gold terms:** h p weakness, weakness, arm weakness, speech difficulties, headache, visual changes

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | acute ischemic stroke of left middle cerebral artery territory | Sudden-onset right arm/hand weakness 2/5, right facial droop, and expressive (Broca's) aphasia with preserved comprehension localize to the left MCA distribution. |
| 2 | cardioembolic stroke secondary to aortic stenosis | Moderate-to-severe aortic stenosis with 4/6 systolic ejection murmur radiating to carotids and EKG ST-T changes raise concern for an embolic source despite NSR. |
| 3 | intracerebral hemorrhage | Hypertension history with acute focal neurologic deficit (right hemiparesis, aphasia) cannot be excluded until the pending head CT returns. |
| 4 | urinary tract infection with sepsis-associated encephalopathy/toxic-metabolic focal deficit | Urinalysis with 608 WBCs, history of chronic UTIs with similar drainage, BUN 52, and glucose 220 could unmask or mimic focal deficits in an elderly patient. |
| 5 | transient ischemic attack / evolving lacunar syndrome | Vascular risk factors (HTN, diabetes on Lantus/Actos/glipizide, CKD) with acute focal motor and language deficits warrant consideration, though persistent symptoms favor completed stroke. |

### Case 41 — hematuria_er_visit

**Gold terms:** voiding, constipation, hematuria, foley catheter, nausea, vomiting

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Recurrent bladder cancer with hematuria | 85-year-old with known history of bladder cancer presenting with painless gross hematuria, the classic presentation for bladder malignancy recurrence. |
| 2 | Benign prostatic hyperplasia with hematuria | Patient has documented enlarged prostate on Flomax and Proscar, with prior difficulty voiding; BPH commonly causes painless hematuria from friable prostatic vessels. |
| 3 | Hemorrhagic cystitis | Recent Levaquin course and Foley placement with UA showing many red cells and prior voiding difficulty raises suspicion for bladder mucosal inflammation/bleeding. |
| 4 | Urinary tract infection / cystitis | Recent urinary symptoms, instrumentation, and current Foley with red cells on UA; culture pending to confirm. |
| 5 | Nephrolithiasis or upper tract urothelial bleeding | Elevated BUN/creatinine (27/1.9) with hematuria could reflect upper urinary tract pathology, though absence of pain makes stones less typical. |

### Case 42 — left_lower_quadrant_pain_er_visit

**Gold terms:** left lower quadrant pain, bowel movement, constipation, fetal heart, nausea, vomiting

**Result:** hit at rank **2**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | opioid-seeking behavior / substance use disorder | Patient appears sedated and falls asleep mid-sentence while dramatically requesting pain medication, has track marks on bilateral arms, and history of multiple positive urine drug screens including opiates and benzodiazepines. |
| 2 | constipation / fecal impaction | No bowel movement in two weeks, stool palpated in rectum on exam, left lower quadrant pain, and history of irritable bowel syndrome. |
| 3 | urinary retention | Patient reports not voiding in 24 hours with high specific gravity (1.024) and ketones on urinalysis suggesting dehydration/retention in a gravid uterus. |
| 4 | dehydration with starvation ketosis | Greater than 88 ketones on UA with 24 hours of nausea/vomiting and decreased intake in a pregnant patient. |
| 5 | asymptomatic bacteriuria in pregnancy | Cath urinalysis shows many bacteria though without WBCs or nitrites, in a patient with prior history of three UTIs and possible Macrobid use. |

### Case 43 — syncope_er_visit

**Gold terms:** ejection fraction, coronary artery bypass grafting, coronary artery disease, v/q scan, bypass grafting, artery bypass

**Result:** hit at rank **3**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Vasovagal syncope | Classic prodrome of abdominal discomfort, nausea, and diaphoresis preceding loss of consciousness with rapid recovery upon laying flat with leg elevation and no post-event confusion. |
| 2 | Orthostatic hypotension | Patient is on multiple antihypertensives (lisinopril, Toprol, Lasix) with documented history of postural hypotension managed by her cardiologist. |
| 3 | Bradyarrhythmia-induced syncope | Heart rate 50-60s on telemetry with right bundle-branch block on EKG in a patient on amiodarone and beta-blocker (Toprol), raising concern for conduction system disease. |
| 4 | Recurrent pulmonary embolism | Patient reports current syncope feels similar to prior PE presentation; she is no longer anticoagulated (only IVC filter and aspirin) after Coumadin-induced GI bleed. |
| 5 | Paroxysmal atrial fibrillation with rapid ventricular response or pause | Known history of paroxysmal AF on amiodarone could cause transient hemodynamic compromise leading to syncope, though current rhythm is sinus. |

### Case 44 — syncope_er_visit_1

**Gold terms:** syncope  1, residual deficit, headache, ct scan, syncopal episode, stress test

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Vasovagal syncope | Brief loss of consciousness with rapid spontaneous recovery and no residual neurologic deficit in a 75-year-old, with unremarkable cardiac exam. |
| 2 | Orthostatic/hypertensive-related syncope | New hypertension (172/91) with labile BP and recent initiation of hydrochlorothiazide raise concern for volume/pressure-mediated transient hypoperfusion. |
| 3 | Cardiac arrhythmia (e.g., paroxysmal AV block or bradyarrhythmia) | Sudden syncope without prodrome in an elderly patient with nondiagnostic inferior Q-waves on EKG suggests possible underlying conduction disease. |
| 4 | Silent myocardial ischemia/infarction | Nondiagnostic Q-waves in inferior leads and new hypertension in a 75-year-old warrant evaluation for ischemic event despite absence of chest pain. |
| 5 | Transient ischemic attack | Brief loss of consciousness with associated headache in an elderly hypertensive patient raises concern for cerebrovascular etiology. |

### Case 48 — bilateral_hip_pain

**Gold terms:** consult - history and phy, bilateral hip pain, femoroacetabular, impingement, hip

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | femoroacetabular impingement (cam-type) | X-ray suggests exostosis on the superior femoral neck, groin pain with activity, and painful clicking/popping in the right hip are classic for FAI. |
| 2 | acetabular labral tear | Mechanical popping/clicking, anterior groin pain, and suspected FAI morphology predispose to and commonly coexist with labral pathology. |
| 3 | early osteoarthritis of the hip | Imaging shows minimal degenerative changes in the joint with chronic activity-related groin pain bilaterally over 2 years. |
| 4 | greater trochanteric pain syndrome (trochanteric bursitis) | Lateral hip pain bilaterally during walking, though absence of trochanteric tenderness makes this less likely. |
| 5 | alcohol-induced avascular necrosis of the femoral head | Heavy daily alcohol use (3-5 drinks) with chronic progressive bilateral hip/groin pain raises concern, though plain films currently show no osteonecrotic changes. |

### Case 49 — consult_jaw_pain

**Gold terms:** consult - history and phy, jaw pain, mandible, numbness and tingling, teeth and tongue, nasal septum

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Mandibular (V3) and lingual nerve neuropathy secondary to occult oral/oropharyngeal malignancy | 53-year-old with 30-year smokeless tobacco use presenting with persistent unilateral numbness of the left jaw, lateral tongue, and buccal mucosa with loss of taste — concerning for perineural invasion despite normal dental and visual exam. |
| 2 | Trigeminal neuropathy (idiopathic/isolated mandibular branch) | Objective decreased sensation in V3 distribution (jaw, lateral tongue, buccal mucosa) for two months without identifiable structural lesion on exam or nasopharyngoscopy. |
| 3 | Numb chin syndrome (mental nerve neuropathy) | Persistent unilateral numbness extending from angle of jaw to lip in a heavy long-term tobacco user — classic red flag presentation warranting malignancy workup. |
| 4 | Oral leukoplakia/premalignant lesion with nerve involvement | 30-year chewing tobacco history with new sensory disturbance localized to the left lateral tongue and buccal mucosa, the typical site of smokeless tobacco–related lesions. |
| 5 | Post-infectious/medication-related (Avelox) neuropathy | Recent throat infection and ongoing fluoroquinolone (Avelox) therapy, which is associated with peripheral neuropathy, temporally correlates with the sensory symptoms. |

### Case 65 — itchy_rash_er_visit

**Gold terms:** urticaria, pruritus, lip swelling, allergic reaction, itchy rash, torso

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute idiopathic urticaria | Sudden-onset pruritic, blanching, confluent erythematous rash on torso with papular/macular lesions on arms and buttocks, without identifiable trigger. |
| 2 | Allergic contact dermatitis | Recent exposure to insulation material while working a couple of days ago could have sensitized skin in contact areas of torso and arms. |
| 3 | Irritant contact dermatitis (fiberglass exposure) | Patient was removing insulation recently; fiberglass commonly causes pruritic papular rash on torso and arms. |
| 4 | Drug or food-induced allergic reaction | Patient has multiple known drug allergies (penicillin, ampicillin, morphine, toradol) suggesting atopic predisposition, though no clear new exposure reported. |
| 5 | Cholinergic urticaria | Diffuse pruritic papular rash on torso and arms in a young male without other triggers could represent a physical urticaria variant. |

### Case 66 — jaw_pain_er_visit

**Gold terms:** jaw pain, dental appointment, ellis type ii fracture, ellis type, dental fracture, toothache

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Symptomatic irreversible pulpitis of tooth #18 | Dental fracture at tooth #18 with tenderness and pain radiating to the jaw and ear is classic for pulpal inflammation referring along the mandibular branch of the trigeminal nerve. |
| 2 | Periapical (apical) periodontitis of tooth #18 | Tenderness localized to the fractured tooth #18 with radiating jaw pain suggests inflammation extending to the periapical tissues, even without visible swelling or fluctuance. |
| 3 | Cracked tooth syndrome | Known dental fracture at tooth #18 several months old now causing new pain radiating toward the ear is consistent with progression of a cracked tooth. |
| 4 | Temporomandibular joint (TMJ) disorder | Unilateral jaw pain radiating to the left ear without ear pathology, lymphadenopathy, or oropharyngeal findings can reflect TMJ dysfunction, possibly secondary to altered occlusion from the fractured tooth. |
| 5 | Trigeminal neuralgia (mandibular branch, V3) | Pain radiating from the lower jaw toward the ear in the V3 distribution without infection, swelling, or systemic findings raises consideration of a neuropathic etiology. |

### Case 78 — asbestos_exposure_hemoptysis

**Gold terms:** asbestos exposure hemoptysis, mesothelioma, acute bronchitis, pleural effusion, thoracentesis, risk for mesothelioma

**Result:** hit at rank **4**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Supratherapeutic anticoagulation-related pulmonary hemorrhage | Patient on Coumadin with INR 3.7 (supratherapeutic) presenting with hemoptysis and blood-tinged sputum. |
| 2 | Acute decompensated congestive heart failure with pulmonary edema | Known CHF with EF 40%, bibasilar crackles, worsening dyspnea, and chest x-ray showing pleural effusion. |
| 3 | Pulmonary embolism | Atrial fibrillation, peripheral cyanosis, hemoptysis, and dyspnea raise concern despite anticoagulation, especially with elevated PT/INR not excluding embolic event. |
| 4 | Bronchogenic carcinoma or mesothelioma | 80-year-old with significant asbestos exposure, hemoptysis, and left-sided pleural effusion on chest x-ray. |
| 5 | Pneumonia with parapneumonic effusion | Cough with sputum production, decreased breath sounds at left base, and left-sided opacification concerning for pleural effusion, though absence of fever and normal WBC make this less likely. |

### Case 92 — chest_wall_lump_consult

**Gold terms:** chest wall lump, ct of the chest, chest wall, chest, tenderness, axillae

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Chondrosarcoma of the costal cartilage | Slowly enlarging, tender, hard 2-cm mass at the costosternal cartilage in a 56-year-old smoker, with ultrasound showing bone/cartilage origin — classic presentation for costal chondrosarcoma. |
| 2 | Costochondritis (Tietze syndrome) | Localized tender costosternal swelling worsened with deep inspiration is characteristic of Tietze syndrome, though the year-long progressive enlargement is atypical. |
| 3 | Healed/healing rib or costochondral fracture with callus formation | Patient reported a car fell on his chest 6 years ago, and ultrasound shows the mass relates to bone, consistent with exuberant fracture callus. |
| 4 | Chondroma (benign cartilaginous tumor of costal cartilage) | A slow-growing, hard, well-localized mass arising from costosternal cartilage is consistent with a benign enchondroma/chondroma. |
| 5 | Metastatic carcinoma to rib (e.g., from occult lung primary) | 56-year-old with two-pack-per-day smoking, chronic cough, family history of cancer, and a progressively enlarging tender bony chest wall mass raises concern for metastatic disease. |
