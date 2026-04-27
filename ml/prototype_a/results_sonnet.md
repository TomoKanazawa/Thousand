# DDx Results — model: `sonnet`

**Cases scored:** 37

| Metric | Hits | Rate |
|---|---|---|
| hit@1 | 31/37 | 84% |
| hit@3 | 35/37 | 95% |
| hit@5 | 35/37 | 95% |

**Tokens** — input: 47,392 · output: 15,881

## Per-case detail

### Case 01 — abdominal_pain_consult

**Gold terms:** abdominal pain, lower quadrant, abdominal, sigmoid, diverticulitis, tenderness

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute diverticulitis | 7-8 day history of left lower quadrant pain, palpable fullness/mass in LLQ, prior antibiotic treatment with Cipro and Flagyl, and obstipation are classic for sigmoid diverticulitis in a 71-year-old female. |
| 2 | Colon carcinoma (sigmoid/descending colon) | Palpable LLQ mass in a 71-year-old with persistent abdominal pain, anorexia, and obstipation raises concern for colorectal malignancy, especially with last colonoscopy 5 years ago. |
| 3 | Large bowel obstruction | Obstipation symptoms with last bowel movement two days ago, anorexia, and persistent abdominal pain suggest possible partial or early large bowel obstruction, potentially secondary to diverticulitis or malignancy. |
| 4 | Pelvic organ prolapse with bowel entrapment or complication | Known grade 4 bladder prolapse with minimal left flank tenderness and LLQ fullness could represent a prolapse-related complication contributing to the obstructive and pain symptoms. |
| 5 | Urinary tract infection or urosepsis (left-sided) | Minimal left flank tenderness, elevated glucose, and allergy to Macrodantin suggest a history of recurrent urinary issues; a left-sided UTI or early urosepsis could be contributing, though WBC is not elevated. |

### Case 03 — consult_chest_pain_1

**Gold terms:** chest pain 1, chest pain, emergency room, dull ache, precordial, shortness of breath

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Vasospastic angina (Prinzmetal angina) | Prior cardiac catheterization showed a suspected right coronary artery lesion thought to be spasm, and current symptoms of pressure-type chest pain are stress-related rather than exertional, consistent with vasospasm. |
| 2 | Anxiety disorder with somatic chest pain | Patient is prescribed Paxil and BuSpar (indicating pre-existing anxiety/depression), symptoms occur specifically under stress, and workup including cardiac enzymes, EKG, chest x-ray, and prior nuclear perfusion scan are all negative. |
| 3 | Stable angina / coronary artery disease | Multiple coronary risk factors are present including active smoking, borderline hyperlipidemia, and family history of fatal CAD (father), supporting atherosclerotic etiology despite prior normal perfusion scan. |
| 4 | Musculoskeletal chest pain (costochondritis) | Pressure-type precordial discomfort with negative cardiac workup (normal EKG, negative enzymes, unremarkable chest x-ray) and no exertional or positional aggravating factors described raises a musculoskeletal etiology. |
| 5 | Gastroesophageal reflux disease (GERD) / esophageal spasm | Stress-related dull pressure chest discomfort without diaphoresis or exertional component and negative cardiac evaluation are consistent with an esophageal or acid-related source, even though epigastric symptoms are denied. |

### Case 04 — consult_syncope

**Gold terms:** hypertension, hyperlipidemia, shortness of breath, coronary artery disease, seizure activity, seizure disorder

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Neurally mediated (vasovagal) syncope | 69-year-old with syncope and no preceding cardiac symptoms (no chest pain, palpitations), normal cardiac enzymes, and normal CT head makes a reflex-mediated mechanism the most common etiology to consider. |
| 2 | Orthostatic hypotension-induced syncope | Patient is on propranolol (a beta-blocker) and Flomax (an alpha-blocker), both of which predispose to orthostatic hypotension, and he has recently diagnosed Parkinson's disease, which is independently associated with autonomic dysfunction. |
| 3 | Cardiac arrhythmia-induced syncope | Displaced PMI suggesting possible left ventricular enlargement in a hypertensive patient, nonspecific ST-T changes on EKG, and elevated heart rate of 93 raise concern for an underlying arrhythmic etiology despite negative cardiac enzymes. |
| 4 | Seizure disorder | The patient himself reported possible seizure activity prior to the syncopal episode, and leukocytosis (WBC 14) with an elevated ammonia level of 69 could contribute to metabolic encephalopathy lowering the seizure threshold. |
| 5 | Hepatic encephalopathy with altered consciousness | Elevated ammonia level of 69 in the context of syncope and possible seizure-like activity suggests early hepatic encephalopathy as a contributing or alternative cause, even though liver enzymes are within normal limits. |

### Case 06 — cough_abdominal_pain

**Gold terms:** cough abdominal pain, abdominal pain, cough, pneumonia, body aches, bronchitis

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Community-acquired pneumonia | Fever (100.1°F), dry cough, coarse breath sounds bilaterally at the bases, oxygen saturation of 95% on room air, and history of prior pneumonia are consistent with a new pneumonia episode. |
| 2 | Influenza | Generalized body aches, dry cough, subjective fevers and chills, and nausea in a 76-year-old with 44 pack-year smoking history strongly suggest an influenza-like illness. |
| 3 | Pleuritis (pleurisy) | Right-sided abdominal pain that occurs only with coughing, along with a history of prior pleurisy, suggests pleuritic chest/lower chest pain being referred to the abdomen. |
| 4 | Atrial tachycardia or new-onset atrial fibrillation | Heart rate of 144 on presentation is significantly elevated and warrants evaluation for a primary arrhythmia potentially triggered by an underlying infectious or pulmonary process. |
| 5 | Pulmonary embolism | Tachycardia (pulse 144), decreased oxygen saturation (95%), respiratory rate of 20, and history of phlebitis raise concern for a thromboembolic event. |

### Case 08 — er_report_chest_pain_fever

**Gold terms:** er report chest pain fever, chest pain, fever, hypertension, acute myocardial infarction, urinary tract infection

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Urinary tract infection with systemic inflammatory response | Urinalysis showed positive nitrites, leukocyte esterase, 5-10 WBCs/hpf, and 1+ bacteria rods in the setting of two days of increasing fever (T 99.4°F) and leukocytosis (WBC 12,200), explaining the febrile presentation. |
| 2 | Non-cardiac chest pain (atypical/musculoskeletal or UTI-related) | Substernal chest discomfort with nausea and diaphoresis occurred in the context of active infection, yet troponin was negative on three occasions, EKG was normal, and stress test was normal, ruling out ACS as the etiology. |
| 3 | Acute coronary syndrome (ruled out) | Substernal chest pain with diaphoresis, nausea, and dizziness in a diabetic, hypertensive, postmenopausal woman with strong family history of early CAD (father and brother in their 40s) warranted urgent evaluation, though serial troponins <0.1 and normal stress test exclude this diagnosis. |
| 4 | Hypertensive urgency | Admission blood pressure of 137/60 in a known hypertensive patient presenting with chest pain, headache, and neck discomfort raised concern for elevated pressure as a contributing factor to her symptoms. |
| 5 | Viral or aseptic meningitis (ruled out) | New-onset neck and head discomfort prompted lumbar puncture; CSF showed 11 red cells (likely traumatic tap), glucose 75, protein 67, and white count 0, effectively excluding infectious meningitis. |

### Case 106 — feeling_dizzy_er_visit

**Gold terms:** feeling dizzy, hypertension, tachycardia, smoking, dizzy, heart rate

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Alcohol withdrawal syndrome | Patient drinks ~5 glasses of wine daily, last drink was yesterday evening, and presented with tachycardia (HR 121) and hypertension (195/83), classic early withdrawal signs, with today being her first near-withdrawal episode. |
| 2 | Hypertensive urgency | Known hypertensive patient noncompliant with medications for several months presenting with BP 195/83, which responded to IV metoprolol. |
| 3 | Alcohol use disorder | Patient consumes approximately 5 glasses of wine daily, has facial telangiectasia on exam, elevated platelets (488,000), and mild anemia (Hgb 12.4), consistent with chronic heavy alcohol use. |
| 4 | Sinus tachycardia secondary to autonomic dysregulation | EKG confirmed sinus tachycardia (HR 121) without acute ST changes, occurring in the context of alcohol withdrawal and uncontrolled hypertension, reflecting sympathetic overdrive. |
| 5 | Essential hypertension, uncontrolled | Established diagnosis of hypertension with documented medication noncompliance for several months contributing to presenting BP of 195/83. |

### Case 115 — gen_med_consult_10

**Gold terms:** gen med  10, hemoglobin a1c, diarrhea, diabetes mellitus type ii, hypertension, hypercholesterolemia

**Result:** hit at rank **2**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Osteoarthritis (polyarticular) | 77-year-old female with diffuse joint pain involving hands, wrists, and reduced mobility, with doughiness of MCP joints and wrists on exam but no significant erythema or swelling, consistent with degenerative joint disease. |
| 2 | Rheumatoid arthritis | Bilateral MCP joint and wrist involvement with doughiness on exam in an elderly female raises concern for inflammatory arthritis, particularly given the symmetric distribution and ongoing pain despite NSAID therapy. |
| 3 | Hyperparathyroidism (persistent/recurrent) | History of parathyroidectomy with still-borderline elevated calcium, and current serum calcium of 10.8 mg/dL, which can cause diffuse arthralgias, bone pain, and musculoskeletal symptoms. |
| 4 | Hypothyroidism-related arthropathy | Patient is on Synthroid for hypothyroidism and reports sleeping all the time and diffuse joint pain; undertreated or suboptimally treated hypothyroidism can cause myalgias, arthralgias, and fatigue. |
| 5 | Anemia of chronic disease contributing to fatigue and functional decline | Hemoglobin of 10.5 g/dL and hematocrit of 35.4% in the setting of chronic disease (diabetes, hypertension, prior infection) may be compounding her reduced mobility and overall sense of malaise. |

### Case 118 — gen_med_consult_12

**Gold terms:** gen med  12, history of diabetes, dyspnea on exertion, uncertain etiology, weak, syncope

**Result:** hit at rank **2**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Anemia | Longstanding weakness, exertional dyspnea, and pallor not noted but history of peptic ulcer disease raises concern for chronic blood loss causing anemia in a 75-year-old female. |
| 2 | Congestive heart failure | History of underlying heart disease, strong family history of CHF, exertional dyspnea, hypertension, and nonspecific ST-segment changes on ECG are consistent with heart failure even without current edema or JVD. |
| 3 | Coronary artery disease / chronic stable angina | History of heart disease, hypertension, hyperlipidemia, type II diabetes, family history of CAD, and nonspecific ST-segment changes on ECG support underlying coronary artery disease presenting with exertional symptoms. |
| 4 | Hypothyroidism | Weakness, fatigue, confusion, and cognitive impairment in a 75-year-old female with no remembered medications are classic features of hypothyroidism, which is common and underdiagnosed in elderly women. |
| 5 | Chronic thromboembolic disease / pulmonary hypertension | Prior history of pulmonary embolism four years ago combined with progressive exertional dyspnea raises concern for chronic thromboembolic pulmonary hypertension contributing to her symptoms. |

### Case 119 — gen_med_consult_14

**Gold terms:** gen med  14, left otalgia, otalgia, serous otitis, atopic dermatitis, serous

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Otitis media with effusion | Left TM with effusion on exam, left otalgia, and reported difficulty hearing that has improved are classic features of otitis media with effusion. |
| 2 | Temporomandibular joint (TMJ) dysfunction | Left-sided jaw pain persisting after dental evaluation found no dental cause, combined with ipsilateral otalgia, strongly suggests TMJ dysfunction. |
| 3 | Chronic sinusitis | History of recurrent sinusitis, left-sided sinus pressure, referred dental/tooth pain, and chronic left-sided headache are consistent with chronic sinusitis. |
| 4 | Eustachian tube dysfunction | Left-sided effusion, otalgia, and transient hearing loss in the setting of sinus pressure suggest Eustachian tube dysfunction contributing to the middle ear findings. |
| 5 | Atopic dermatitis (flare requiring management) | Known history of atopic dermatitis with physical exam showing scattered erythematous plaques with lichenification on the nuchal region and behind the knees, requiring refill of Cutivate cream. |

### Case 120 — gen_med_consult_15

**Gold terms:** gen med  15, tearfulness, mood swings, menopause, postsurgical menopause, mood swings and tearfulness

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Surgical menopause with mood disorder | Patient underwent TAH with BSO in 2003 causing surgical menopause; she now presents with mood swings, tearfulness, insomnia, and difficulty concentrating consistent with estrogen deficiency sequelae, even in the absence of hot flashes/night sweats. |
| 2 | Major depressive disorder | Patient presents with dysthymic mood, tearfulness on exam, insomnia, difficulty concentrating, and functional impairment at work lasting several months, meeting core criteria for a depressive episode. |
| 3 | Dysthymic disorder (persistent depressive disorder) | Chronic, gradually worsening low mood over several months with insomnia and concentration difficulties in the context of prior treatment for mood-related symptoms (Wellbutrin prescribed previously) suggests a persistent depressive condition. |
| 4 | Hypothyroidism | Mood disturbance, tearfulness, difficulty concentrating, and insomnia are classic manifestations of hypothyroidism, and the chart notes absence of thyromegaly but does not document thyroid function testing to rule this out. |
| 5 | Bipolar II disorder (depressive phase) | Rapid mood swings noted prominently in the HPI alongside depressive symptoms (tearfulness, insomnia, concentration difficulties) raise consideration of a bipolar spectrum disorder, particularly Bipolar II with hypomanic episodes. |

### Case 121 — gen_med_consult_16

**Gold terms:** gen med  16, short-term memory loss, anxiety, short term memory loss, memory loss, stress issues

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Stress-related cognitive dysfunction (stress-induced memory impairment) | Patient reports short-term memory difficulties in the setting of exceeding stress over 5–10 years, a high-demand job at T-Mobile, and widowhood for 11 years, with no focal neurological findings on exam. |
| 2 | Major depressive disorder with cognitive symptoms | Current use of Zoloft 100 mg daily suggests an existing mood disorder, and depression commonly presents with subjective memory complaints and difficulty absorbing new information, as described. |
| 3 | Mild cognitive impairment (MCI) | Age 60 with subjective short-term memory loss and difficulty learning new technical skills/protocols raises concern for early MCI, even in the absence of focal neurological deficits. |
| 4 | Hypothyroidism | Memory impairment, difficulty concentrating, and cognitive slowing are classic features of hypothyroidism, and no thyroid function tests are documented in this chart for a 60-year-old female with these complaints. |
| 5 | Medication-related cognitive side effects | HCTZ can cause electrolyte disturbances (e.g., hyponatremia) contributing to cognitive symptoms, and Zyrtec (cetirizine) has mild anticholinergic properties that may impair memory, particularly in older adults. |

### Case 132 — gen_med_consult_31

**Gold terms:** gen med  31, cerebrovascular accident, recurrent urinary tract infection, diabetes, hypoglycemia, neuropathy

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Catheter-associated urinary tract infection with septic encephalopathy | Indwelling Foley catheter, history of recurrent UTIs, recent hospitalization for UTI 3 weeks ago, urine showing 20 WBCs, and acutely worsened mental status/decreased consciousness are consistent with urosepsis-related encephalopathy. |
| 2 | Hypoglycemic encephalopathy | Blood sugar was found to be 40 by paramedics in the setting of poor PO intake and insulin use (Humulin N 30 units twice daily plus Avandia), directly preceding the acute altered mental status episode. |
| 3 | Opioid/polypharmacy-induced encephalopathy | Patient is on Percocet 2 tablets four times daily, Neurontin 600 mg BID, Flexeril TID, and Reglan, representing a high sedative/CNS-depressant burden in a 74-year-old with baseline cognitive impairment from prior CVA. |
| 4 | Acute-on-chronic kidney injury with uremic encephalopathy | Creatinine of 2.8 and BUN of 48 indicate significant renal impairment, likely worsened by concurrent ibuprofen use and possible infection, which can contribute to metabolic encephalopathy. |
| 5 | Ischemic stroke (new or recurrent) | Prior right-sided CVA with baseline aphasia, atrial fibrillation (a known cardioembolic risk factor), and subtherapeutic anticoagulation (INR 1.1 on Coumadin) raise concern for a new or recurrent thromboembolic cerebrovascular event explaining acutely worsened aphasia and decreased consciousness. |

### Case 133 — gen_med_consult_34

**Gold terms:** gen med  34, chronic abdominal, evaluation, chronic, epigastric, bowel

**Result:** **MISS**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Metastatic pancreatic adenocarcinoma | CT shows an extensive mass in the pancreatic body and tail with peripancreatic extension, left kidney invasion, and too-numerous-to-count bilobar liver masses up to 8 cm, consistent with advanced pancreatic cancer with hepatic metastases. |
| 2 | Pancreatic neuroendocrine tumor (non-functioning) with hepatic metastases | Large pancreatic body/tail mass with bilobar liver metastases and possible splenic lesions in a 23-year-old fits a neuroendocrine tumor; patient denied flushing, making a non-functioning NET plausible. |
| 3 | Primary hepatic malignancy (hepatocellular carcinoma) with pancreatic involvement | Bilobar liver masses with an enlarged liver (16 cm span, 6 cm below costal margin) and irregular border could suggest a primary hepatic malignancy, though the dominant pancreatic mass makes a pancreatic primary more likely. |
| 4 | Lymphoma (non-Hodgkin) with pancreatic and hepatic involvement | A 23-year-old male with 20-pound weight loss, diarrhea, epigastric pain, and multi-organ involvement (pancreas, bilobar liver, possible spleen) is consistent with systemic lymphoma. |
| 5 | Metastatic germ cell tumor (non-seminomatous) with retroperitoneal and visceral spread | Young male (23 years old) with a large retroperitoneal/peripancreatic mass, hepatic lesions, and significant weight loss raises concern for a non-seminomatous germ cell tumor with visceral metastases. |

### Case 134 — gen_med_consult_35

**Gold terms:** gen med  35, fluticasone nasal inhaler, confusion and hallucinations, blood pressure, temperature, abdomen

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Pheochromocytoma | Severe hypertension (186/101 mmHg), tachycardia (110-122 bpm), weight loss, night sweats, lightheadedness, anxiety, abdominal bruit, and bilateral femoral bruits are classic features of a catecholamine-secreting tumor, which can also cause neuropsychiatric symptoms including hallucinations and confusion. |
| 2 | Cushing's syndrome (hypercortisolism) | Psychiatric symptoms including hallucinations, paranoia, and mood elevation combined with hypertension, acneiform eruption over the back and trunk, and weight loss are consistent with excess glucocorticoid exposure, potentially exacerbated by the prescribed Fluticasone. |
| 3 | First-episode psychosis (Brief psychotic disorder or early schizophrenia) | A 27-year-old man presenting with auditory and visual hallucinations, paranoid ideation (fear of being poisoned, fear family will harm him), disorganized behavior, and elevated/euphoric mood in the context of significant psychosocial stress warrants this consideration, though the prominent medical findings make a primary psychiatric etiology less likely. |
| 4 | Renovascular hypertension with hypertensive encephalopathy | Bilateral femoral bruits and abdominal bruit suggest renal artery stenosis or vascular disease causing severe hypertension (186/101 mmHg), which at this level can produce confusion, hallucinations, and neuropsychiatric symptoms. |
| 5 | CNS vasculitis or autoimmune encephalitis | Subacute onset of confusion, hallucinations, paranoia, disorientation, and low-grade fever (100.8°F) in a young man without prior psychiatric history raises concern for autoimmune or inflammatory CNS processes such as anti-NMDA receptor encephalitis. |

### Case 135 — gen_med_consult_36

**Gold terms:** gen med  36, decreased range of motion, coughing up blood, chest, interstitial, infiltrates

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Granulomatosis with polyangiitis (GPA, Wegener's granulomatosis) | Pauci-immune crescentic glomerulonephritis on biopsy, hemoptysis with bilateral pulmonary infiltrates and hilar lymphadenopathy, migratory polyarthritis, worsened upper airway symptoms (rhinitis), and bilateral scleritis/conjunctivitis form a classic multi-system ANCA vasculitis picture. |
| 2 | Microscopic polyangiitis (MPA) | Pauci-immune crescentic glomerulonephritis with no immune deposits (negative IF), hemoptysis, and systemic inflammation are hallmarks of MPA, though absence of prominent upper airway granulomatous disease slightly favors GPA. |
| 3 | Eosinophilic granulomatosis with polyangiitis (EGPA, Churg-Strauss syndrome) | The prominent eosinophilic interstitial infiltrate on renal biopsy, history of chronic allergic rhinitis, and multi-organ vasculitis involvement raise consideration of EGPA, though asthma is absent. |
| 4 | Systemic lupus erythematosus with lupid nephritis and pulmonary hemorrhage | Young African American woman with polyarthritis, hematuria, hemoptysis, bilateral pulmonary infiltrates, and serositis-like presentation fits SLE; however, pauci-immune (IF-negative) biopsy pattern argues against the immune-complex deposition typical of lupus nephritis. |
| 5 | Anti-GBM disease (Goodpasture syndrome) | The combination of diffuse alveolar hemorrhage (hemoptysis, bilateral pulmonary infiltrates) and rapidly progressive crescentic glomerulonephritis is characteristic; however, the pauci-immune (negative IF) biopsy pattern rather than linear IgG deposits makes this less likely than an ANCA-associated vasculitis. |

### Case 136 — gen_med_consult_37

**Gold terms:** gen med  37, liver biopsy, dark urine, generalized weakness, lymph nodes, granulomatous

**Result:** hit at rank **2**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Hepatocellular carcinoma | Significant weight loss (26 lbs over ~4 weeks), hepatomegaly, jaundice, icteric sclerae, bilateral inguinal lymphadenopathy, and a brother with cirrhosis suggest an underlying hepatic malignancy in a high-risk context. |
| 2 | Lymphoma (Non-Hodgkin's) | Constitutional B symptoms including fever, night sweats, significant weight loss, along with bilateral inguinal lymphadenopathy (up to 2 cm), hepatomegaly, and splenomegaly are classic features of lymphoma. |
| 3 | Viral hepatitis (Hepatitis B or C) with hepatic decompensation | Jaundice, icteric sclerae, RUQ tenderness, hepatomegaly, splenomegaly, dark urine, and a family history of cirrhosis raise concern for chronic viral hepatitis progressing to liver failure. |
| 4 | Cholangiocarcinoma | Obstructive jaundice with dark urine, significant weight loss, RUQ tenderness, and prior cholecystectomy history are consistent with a biliary tract malignancy. |
| 5 | Autoimmune hepatitis | Progressive jaundice, hepatomegaly, splenomegaly, systemic symptoms including fatigue and anorexia, and absence of alcohol use make autoimmune hepatitis a consideration in this 40-year-old male. |

### Case 138 — gen_med_consult_39

**Gold terms:** gen med  39, abdominal pain, nausea, vomiting, fever, altered mental status

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Primary adrenal insufficiency (Addison's disease) | Bilateral adrenal abnormalities on CT (3.5cm right adrenal mass and edematous left adrenal), hyponatremia (Na 127), hyperkalemia (K 4.7), hypotension refractory to 4L IVF, altered mental status, family history of Addison's disease, and a clinical picture consistent with adrenal crisis precipitated by the physiologic stress of dental extraction. |
| 2 | Bilateral adrenal hemorrhage | CT findings of a 3.5cm non-calcified right adrenal mass and edematous left adrenal, in the setting of a newly discovered extensive DVT suggesting a hypercoagulable/antiphospholipid state, are classic for bilateral adrenal hemorrhage leading to acute adrenal crisis. |
| 3 | Antiphospholipid antibody syndrome | Extensive right lower extremity DVT (total obstruction of multiple deep veins), PFO with right-to-left shunt on TEE, bilateral adrenal pathology consistent with hemorrhagic infarction, and a father with SLE (an associated autoimmune condition) all suggest a primary or secondary hypercoagulable state consistent with antiphospholipid antibody syndrome. |
| 4 | Sepsis with multiorgan dysfunction | Patient presents with fever (102.9°F), tachycardia (HR 145), hypotension (BP 99/50), leukocytosis with bandemia (WBC 15.6, 16% bands), altered mental status, oliguria, and bilateral sinusitis on MRI brain, consistent with sepsis from an odontogenic or sinusitis source. |
| 5 | Bacterial meningitis | Acute altered mental status, high fever, leukocytosis with bandemia, and the fact that an LP was performed empirically in the ER with empiric ceftriaxone administered raise concern for bacterial meningitis, though MRI brain showed no contraindications and CSF results are pending. |

### Case 14 — gen_med_h_p_2

**Gold terms:** gen med h p 2, weakness, malaise, dyspnea on exertion, weight loss, atypical pneumonia

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Pneumocystis jirovecii pneumonia (PCP) | Bilateral alveolar and interstitial infiltrates on CXR, severe hypoxemia (pO2 46 on room air), tachypnea, and subacute dyspnea on exertion in a likely HIV-positive patient with oral thrush strongly suggest PCP. |
| 2 | HIV/AIDS with advanced immunosuppression | History of high-risk homosexual activity in Haiti in 1982, oral thrush, marked generalized lymphadenopathy, significant weight loss, and multiple opportunistic features together indicate advanced HIV/AIDS as the underlying condition. |
| 3 | Disseminated Mycobacterium avium complex (MAC) infection | Marked lymphadenopathy, weight loss, anorexia, elevated liver enzymes (AST 131), thrombocytosis, and the severely immunocompromised context are consistent with disseminated MAC. |
| 4 | Kaposi sarcoma | Multiple subcutaneous mobile nodules on the chest wall in an HIV-risk patient with prior biopsy of chest wall cysts, combined with lymphadenopathy and possible pulmonary involvement (infiltrates), raises concern for Kaposi sarcoma. |
| 5 | Bacterial pneumonia (community-acquired, including atypical pathogens) | Bilateral basilar crackles, egophony in mid-lung fields, fever (101.6°F), tachycardia, and leukocytosis with consolidative changes on CXR are compatible with bacterial or atypical pneumonia, possibly co-existing with PCP. |

### Case 143 — gen_med_consult_47

**Gold terms:** gen med  47, inflammatory, degenerative, fever, lumbar spine, sacroiliac joint

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Septic sacroiliitis | Fever of 104°F, severe left sacroiliac joint pain, bacteremia suggested by positive blood cultures workup, and bilateral swollen inguinal nodes all point to infectious arthritis of the sacroiliac joint. |
| 2 | Brucellosis | Patient raises goats and cattle in Mexico (endemic area), has fever, sacroiliac joint pain, and febrile agglutinins were ordered, which is a classic workup for Brucella infection. |
| 3 | Psoas or iliopsoas abscess | High spiking fever, left posterior pelvic and sacroiliac pain, new hyperglycemia consistent with occult diabetes as a risk factor, and bilateral inguinal lymphadenopathy suggest a deep soft tissue infection even though initial MRI was unremarkable. |
| 4 | Epidural or paraspinal abscess | History of prior sacral abscess requiring multiple surgeries and now presenting with severe sacroiliac and low back pain with high fever raises concern for recurrent deep spinal infection, though MRI lumbar spine was reportedly unremarkable. |
| 5 | Osteomyelitis of the sacrum or ilium | Persistent high fever, focal severe pain at the sacroiliac joint, newly discovered hyperglycemia (a known risk factor for hematogenous osteomyelitis), and prior sacral surgical history increase the likelihood of bony infection in this region. |

### Case 147 — gen_med_consult_51

**Gold terms:** gen med  51, abdominal pain, nausea, vomiting, small bowel obstruction, nausea and vomiting

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Adhesive small bowel obstruction | History of ~20 prior small bowel obstruction episodes, multiple prior abdominal surgeries (colon resection, cholecystectomy, appendectomy), CT showing dilated fluid-filled loops of bowel, and hypoactive bowel sounds with abdominal distension are all classic for adhesion-related SBO. |
| 2 | Partial (low-grade) small bowel obstruction | CT demonstrated multiple fluid-filled dilated loops without a clear transition point or complete obstruction, and pain temporarily improved after vomiting, suggesting a partial rather than complete obstruction. |
| 3 | Ileus (postprandial/functional) | Onset of pain shortly after dinner, CT showing no definitive mechanical obstruction, mildly elevated glucose (157), and hypoactive bowel sounds are consistent with a paralytic or functional ileus rather than true mechanical obstruction. |
| 4 | Recurrent colorectal carcinoma with partial obstruction | Patient has a history of partial colon resection for colon carcinoma in 1961; though no recurrence has been documented, new bowel obstruction pattern in an elderly patient warrants consideration of tumor recurrence or a new colorectal neoplasm causing partial luminal obstruction. |
| 5 | Mesenteric ischemia (non-occlusive) | Age 89, post-prandial onset of severe abdominal pain (8/10), mildly elevated WBC (12.1), and hypoactive bowel sounds raise concern for non-occlusive mesenteric ischemia, though the absence of peritoneal signs and elevated lactate data makes this less likely than obstruction. |

### Case 16 — flank_pain_consult

**Gold terms:** flank pain, unable to urinate, urinary tract infection, flank

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute cystitis / urinary tract infection | Urinalysis showing 3+ bacteria along with difficulty urinating strongly supports a bacterial urinary tract infection. |
| 2 | Acute pyelonephritis | Left flank pain combined with 3+ bacteriuria raises concern for upper urinary tract infection, though white count is not elevated and patient feels better. |
| 3 | Focal ileus (localized small bowel ileus) | CT scan explicitly identified a focal ileus in the left upper quadrant, which could account for the left flank discomfort and urinary symptoms from local inflammation. |
| 4 | Ureteral injury / post-traumatic ureteral stricture | History of prior blunt left kidney trauma in a motor vehicle accident could have caused ureteral scarring, contributing to left flank pain and difficulty urinating despite absence of stones on CT. |
| 5 | Nephrolithiasis | Left flank pain and difficulty urinating are classic for ureteral calculus, though CT scan showed no kidney stones, making this less likely but still worth considering if stone passed or is radiolucent. |

### Case 24 — lightheaded_dizziness

**Gold terms:** lightheaded dizziness, passing out, echocardiogram, cardiac catheterizatio, normal sinus rhythm, cardiac enzyme

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Paroxysmal supraventricular tachycardia (PSVT) | Episodic palpitations, racing heart, chest fluttering, and near-syncope that resolved by ED arrival with normal sinus rhythm on EKG are classic for a paroxysmal arrhythmia that terminates spontaneously. |
| 2 | Paroxysmal atrial fibrillation | Intermittent palpitations described as fluttering with near-syncope and self-termination before EKG capture is consistent with paroxysmal atrial fibrillation, especially in a 50-year-old female. |
| 3 | Vasovagal (neurocardiogenic) syncope / presyncope | Lightheadedness, dizziness, and near-syncope without actual loss of consciousness, with normal cardiac enzymes and unremarkable structural workup, supports a vasovagal or neurocardiogenic mechanism. |
| 4 | Anxiety disorder with somatic palpitations | No identifiable arrhythmia on EKG, negative cardiac enzymes, normal prior catheterization and echocardiogram, and prior unexplained chest pain workup raise the possibility of anxiety-mediated sympathetic activation causing palpitations and near-syncope. |
| 5 | Inappropriate sinus tachycardia | Episodes of racing heart with dizziness and palpitations in a 50-year-old female, resolving to normal sinus rhythm (rate 69) on arrival, could represent inappropriate sinus tachycardia, particularly given the absence of structural heart disease on prior workup. |

### Case 27 — dysphagia_hematemesis

**Gold terms:** dysphagia hematemesis, gi prophylaxis, hiv medications, alcohol abuse, weight, prophylaxis

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Esophageal food impaction with esophageal dysmotility (achalasia or secondary motility disorder) | CT chest demonstrating large esophageal distention containing residual food after eating eggplant parmigiana, combined with first-episode dysphagia and globus sensation, strongly suggests underlying esophageal dysmotility with acute food bolus impaction. |
| 2 | Mallory-Weiss tear | Hematemesis occurring in the context of forceful vomiting after eating, with no prior hematemesis history, is classic for a Mallory-Weiss mucosal tear at the gastroesophageal junction. |
| 3 | Esophageal candidiasis | Patient is HIV-positive with CD4 likely suppressed (not taking antiretrovirals for 2-3 months), placing her at high risk for opportunistic esophageal candidiasis, which can cause dysphagia and odynophagia contributing to the current presentation. |
| 4 | Decompensated heart failure with elevated BNP | BNP of 1328 and cardiomegaly on CXR and CT in a patient with known compensated heart failure suggest acute decompensation, which may contribute to esophageal and systemic congestion and the chest pain presentation. |
| 5 | Esophageal stricture (HIV/hepatitis-related or peptic) | Known HIV and hepatitis B/C with history of not taking antiretrovirals raises concern for chronic esophageal injury or stricture formation that predisposed to acute food impaction in an otherwise first-time dysphagia episode. |

### Case 29 — lower_quadrant_pain

**Gold terms:** lower quadrant pain, right lower quadrant pain, white blood cell count, lower quadrant, bilirubin, quadrant

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute appendicitis | Positive Rovsing sign, positive obturator sign, RLQ tenderness with rebound, fever of 38.7, and leukocytosis of 20,000 with 75% polys are classic for appendicitis, even though CT was non-diagnostic with appendix not visualized. |
| 2 | Ovarian torsion | Right lower quadrant pain radiating to the flank in a premenopausal woman with irregular menses (suggesting possible ovarian cyst or enlargement), CT not characterizing adnexa, and fever/tachycardia support this diagnosis. |
| 3 | Ruptured or hemorrhagic ovarian cyst | Premenopausal female with irregular cycles, acute stabbing RLQ pain radiating to the flank, and hematuria on urinalysis (50 blood) are consistent with a ruptured ovarian cyst with peritoneal irritation. |
| 4 | Acute pyelonephritis / ureterolithiasis with superimposed infection | Pain radiating to the right flank, urinalysis showing 1+ leukocytes, WBCs 10-25, and 50 blood with tachycardia and fever raise concern for right-sided urinary tract pathology, though RBC count is low and RLQ signs are prominent. |
| 5 | Meckel's diverticulitis | RLQ pain with peritoneal signs (rebound, Rovsing, obturator), marked leukocytosis, and a CT that failed to identify the appendix could indicate Meckel's diverticulitis mimicking appendicitis in a middle-aged adult. |

### Case 32 — dizziness_recurrent

**Gold terms:** dizziness recurrent, recurrent dizziness, shortness of breath, rotational sensation, earache, headaches

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Benign paroxysmal positional vertigo (BPPV) | Classic rotational vertigo triggered by position changes (arising, rolling over in bed, looking up) lasting minutes and resolving with stillness strongly suggests BPPV, though the Dix-Hallpike (Barany) maneuver could not be completed. |
| 2 | Vertebrobasilar insufficiency / posterior circulation TIA | History of prior stroke with right-sided hemiparesis, right-sided numbness, gait abnormality with right lower extremity circumduction, atrial fibrillation on Coumadin, and positional dizziness raise concern for recurrent posterior circulation ischemia. |
| 3 | Meniere's disease | Unilateral right-sided tinnitus combined with episodic rotational vertigo in a patient with fluctuating vestibular symptoms is consistent with Meniere's disease. |
| 4 | Orthostatic hypotension with presyncope | The patient reports near-syncopal sensations with position changes, and vital signs show an atypical blood pressure response on standing (drop in sitting BP 112/84 to standing 130/90 with pulse decrease from 84 to 66), and she is on multiple antihypertensives including Coreg, furosemide, and Diovan. |
| 5 | Medication-induced dizziness / polypharmacy effect | The patient's extensive medication list includes Percocet, Ultram, Coreg, furosemide, and Diovan — all of which can individually or synergistically cause dizziness and unsteadiness, and the treating clinician had already held Percocet and Ultram for this concern. |

### Case 34 — neuro_consult_leg_weakness

**Gold terms:** neuro  leg weakness, hyperckemia, emg and nerve, nerve conduction studies, leg weakness, leg

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Peroneal (fibular) mononeuropathy | Right ankle dorsiflexion weakness (4/5), ankle eversion weakness, steppage gait, difficulty heel-walking, and a positive Tinel's sign at the right fibular head all strongly localize to the right common peroneal nerve at the fibular head. |
| 2 | Lumbosacral polyradiculopathy (L4-S1) | Right-sided distal lower extremity weakness with absent ankle jerks, diminished vibratory sensation in both toes, chronic back pain, and CT showing degenerative changes are consistent with multilevel lumbosacral nerve root involvement. |
| 3 | Length-dependent peripheral polyneuropathy (likely multifactorial: diabetic/alcoholic) | Bilateral diminished vibratory sensation at the toes, absent ankle jerks, bilateral calf cramping, and chronic tingling/numbness in toes fit a length-dependent polyneuropathy in the context of diabetes, heavy alcohol use (4 drinks/night), and smoking. |
| 4 | Motor neuron disease (e.g., amyotrophic lateral sclerosis or progressive muscular atrophy variant) | Scant fasciculations in both calves, right lower extremity muscle atrophy (hamstrings, calf, quadriceps), asymmetric distal weakness, absent ankle jerks, and elevated CK raise concern for a motor neuron disorder, though upper motor neuron signs are absent. |
| 5 | Statin-related myopathy with hyperCKemia | Persistently elevated CK (500–1000 range) with documented fluctuation correlating with Lipitor use and cessation, in the setting of prior and current lipid-lowering therapy, raises the possibility of a statin-associated myopathy contributing to the clinical picture. |

### Case 36 — h_p_weakness

**Gold terms:** h p weakness, weakness, arm weakness, speech difficulties, headache, visual changes

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute ischemic stroke (cardioembolic) | Sudden-onset right arm weakness (2/5 strength), right facial droop, and expressive aphasia with preserved comprehension in a patient with known moderate-to-severe aortic stenosis and Digoxin use suggest a cardioembolic mechanism. |
| 2 | Acute ischemic stroke (atherosclerotic/thrombotic) | Hypertension, diabetes (on Lantus, Glipizide, Actos), and the focal neurological deficits (right hemiparesis, expressive aphasia) are consistent with large-vessel atherothrombotic ischemic stroke. |
| 3 | Hemorrhagic stroke (intracerebral hemorrhage) | Acute focal deficits including right-sided weakness and expressive aphasia with hypertension (BP 138/59 despite antihypertensives) cannot exclude intracranial hemorrhage until the pending head CT is reviewed. |
| 4 | Todd's paralysis (postictal focal weakness) | The patient is on Depakote ER, suggesting a known seizure disorder, and a postictal state with focal right-sided weakness and transient aphasia could mimic stroke presentation. |
| 5 | Septic embolism secondary to urinary tract infection | The urinalysis shows 608 WBCs and 625 RBCs with a history of chronic UTIs and low-grade fever (99.1°F), raising the possibility of bacteremia with septic cerebral embolism causing the focal neurological deficits. |

### Case 41 — hematuria_er_visit

**Gold terms:** voiding, constipation, hematuria, foley catheter, nausea, vomiting

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Bladder cancer recurrence with hematuria | Known history of bladder cancer combined with painless gross hematuria requiring Foley catheter placement and continuous bladder irrigation strongly suggests tumor-related bleeding. |
| 2 | Benign prostatic hyperplasia with hematuria | Known enlarged prostate with medications Flomax, Proscar, and Cardura indicating significant BPH, which can cause gross hematuria, especially in the context of prior voiding difficulty. |
| 3 | Urinary tract infection with hematuria | Urine culture is pending and UA showed many red cells; prior admission involved voiding difficulty treated with Levaquin, and he is currently still on Levaquin, suggesting an infectious etiology has not been fully excluded. |
| 4 | Anticoagulant or medication-induced hematuria | The patient is on multiple medications including Digoxin and antihypertensives; hemoglobin of 10.8 suggests baseline anemia, and polypharmacy in an elderly patient can predispose to urologic bleeding. |
| 5 | Renal insufficiency-related coagulopathy with hematuria | Elevated BUN of 27 and creatinine of 1.9 indicate chronic kidney disease, which can impair platelet function and contribute to mucosal bleeding including hematuria. |

### Case 42 — left_lower_quadrant_pain_er_visit

**Gold terms:** left lower quadrant pain, bowel movement, constipation, fetal heart, nausea, vomiting

**Result:** hit at rank **2**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute opioid/polysubstance intoxication | Patient appears sedated, falls asleep mid-sentence, has bilateral arm track marks, and recent urine drug screens positive for opiates, benzodiazepines, barbiturates, and marijuana, consistent with active intoxication rather than a primary abdominal pathology. |
| 2 | Constipation in pregnancy | Patient reports no bowel movement in two weeks, has a history of IBS, and palpable stool was found in the rectum on pelvic exam, with LLQ tenderness consistent with fecal impaction/severe constipation. |
| 3 | Urinary tract infection / pyelonephritis | Urinalysis shows many bacteria on a catheterized specimen, the patient has a history of three prior UTIs with possible prior pyelonephritis, lower back pain bilaterally, and she was already on Macrobid questionably. |
| 4 | Drug-seeking behavior with functional pain presentation | Patient is yelling out for pain medication, appears intermittently sedated then agitated ('thrashing'), has multiple prior positive drug screens including opiates, and labs/physical exam do not reveal a clear acute surgical or obstetric etiology for the reported severity of pain. |
| 5 | Preterm labor / uterine irritability | Patient is at 28 weeks gestation presenting with lower abdominal pain and lower back pain, though cervix is currently closed, long, and posterior, making active preterm labor less likely but warranting monitoring. |

### Case 43 — syncope_er_visit

**Gold terms:** ejection fraction, coronary artery bypass grafting, coronary artery disease, v/q scan, bypass grafting, artery bypass

**Result:** **MISS**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Vasovagal syncope | Classic prodrome of nausea, diaphoresis, and abdominal discomfort before loss of consciousness, with rapid recovery upon being laid flat with legs elevated and no post-ictal confusion. |
| 2 | Recurrent pulmonary embolism | Prior history of PE with a similar syncopal presentation, IVC filter in place (suggesting high PE risk), and elevated BNP of 366 suggesting right heart strain, despite negative troponin. |
| 3 | Orthostatic hypotension-related syncope | Documented history of postural hypotension managed by her physician, use of antihypertensives (lisinopril, Toprol, Lasix), and prior episodes of weakness consistent with orthostatic events. |
| 4 | Cardiac arrhythmia-induced syncope | History of paroxysmal atrial fibrillation on amiodarone, resting heart rate of 50–60 bpm, right bundle-branch block on EKG, and known structural heart disease (CAD, mitral regurgitation) all predispose to arrhythmia-mediated syncope. |
| 5 | Cerebrovascular/carotid insufficiency-related syncope | Right carotid bruit on exam, known carotid artery disease on recent ultrasound, and CT findings of chronic microvascular ischemic changes suggest possible transient cerebral hypoperfusion as a contributing mechanism. |

### Case 44 — syncope_er_visit_1

**Gold terms:** syncope  1, residual deficit, headache, ct scan, syncopal episode, stress test

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Vasovagal syncope | Brief loss of consciousness with rapid recovery and no residual deficits in a 75-year-old is consistent with vasovagal etiology, and the situational context (getting up, carrying food) supports a reflex mechanism. |
| 2 | Orthostatic hypotension-induced syncope | New initiation of hydrochlorothiazide today combined with a blood pressure drop from 172/91 to 139/75 suggests volume depletion or medication-induced orthostatic hypotension as a precipitant. |
| 3 | Transient ischemic attack (TIA) | Age 75, new hypertension (150/70 initially, now 172/91), associated headache, and brief loss of consciousness raise concern for a cerebrovascular event despite no residual neurological deficits. |
| 4 | Cardiac arrhythmia-induced syncope | Nondiagnostic Q-waves in the inferior leads on EKG suggest possible prior ischemic injury, which could provide substrate for arrhythmia causing sudden loss of consciousness. |
| 5 | Silent myocardial infarction with syncopal presentation | Inferior lead Q-waves on EKG and new hypertension in a 75-year-old woman (who may present atypically) warrant consideration of an acute or recent inferior MI, especially given the headache and sudden syncope. |

### Case 48 — bilateral_hip_pain

**Gold terms:** consult - history and phy, bilateral hip pain, femoroacetabular, impingement, hip

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Femoroacetabular impingement (FAI) | X-ray shows suggestion of exostosis on the superior femoral neck consistent with FAI, and the patient has anterior groin pain with painful clicking/popping in the right hip of 2 years duration. |
| 2 | Hip labral tear | Painful popping and clicking in the right hip with groin pain in a young active woman with imaging suggesting FAI, as FAI commonly causes labral pathology as a secondary finding. |
| 3 | Greater trochanteric pain syndrome (trochanteric bursitis) | The patient reports lateral hip pain bilaterally, which is a hallmark distribution of greater trochanteric pain syndrome, though significant trochanteric tenderness was absent on exam. |
| 4 | Early hip osteoarthritis | Minimal degenerative changes noted on X-ray along with bilateral groin and lateral hip pain worsening over 2 years in a middle-aged woman support early osteoarthritis as a contributing diagnosis. |
| 5 | Snapping hip syndrome (coxa saltans) | The patient reports painful popping and clicking in the right hip with activity, which is characteristic of snapping hip syndrome, potentially involving the iliopsoas tendon given the anterior groin pain location. |

### Case 49 — consult_jaw_pain

**Gold terms:** consult - history and phy, jaw pain, mandible, numbness and tingling, teeth and tongue, nasal septum

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Oral cavity or oropharyngeal malignancy with perineural invasion (V3/lingual nerve) | 30-year history of heavy chewing tobacco use (half a can/day) combined with persistent left-sided hemifacial and lateral tongue numbness along the V3 distribution strongly raises concern for a malignant neoplasm with perineural spread, even though no overt mass was visualized on exam. |
| 2 | Numb chin syndrome (mental neuropathy) secondary to underlying malignancy or metastatic disease | Unilateral numbness extending from the angle of the jaw to the lip in a 53-year-old with significant tobacco history is a classic presentation of numb chin syndrome, which can herald underlying malignancy or bony infiltration of the mandibular nerve. |
| 3 | Trigeminal neuropathy (idiopathic or inflammatory) | Persistent unilateral sensory deficit confined to the left V3 distribution (jaw, lateral tongue, intrabuccal mucosa) without identifiable structural lesion on exam could represent idiopathic or inflammatory trigeminal neuropathy. |
| 4 | Base of skull lesion or deep space neck mass compressing the inferior alveolar/lingual nerve | The distribution of numbness covering the left jaw, tongue, and buccal mucosa follows the V3 branch, and a lesion in the infratemporal fossa or skull base not visible on nasopharyngoscopy or palpation must be excluded with cross-sectional imaging. |
| 5 | Temporomandibular disorder or atypical facial pain with neuropathic component | Although the patient denies jaw popping or trismus, the jaw and tongue sensory symptoms with a history of headaches and anxiety disorder could be consistent with a neuropathic/atypical facial pain syndrome, though this is a diagnosis of exclusion given the tobacco history. |

### Case 65 — itchy_rash_er_visit

**Gold terms:** urticaria, pruritus, lip swelling, allergic reaction, itchy rash, torso

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute urticaria | Sudden-onset diffuse pruritic erythematous blanching rash on torso, arms, and buttocks with mild tachycardia but no angioedema or systemic compromise is classic for urticaria. |
| 2 | Contact dermatitis (irritant or allergic) | Patient worked removing insulation a couple of days prior, which is a known skin irritant/sensitizer, consistent with a delayed hypersensitivity or irritant reaction now presenting as a widespread rash. |
| 3 | Early anaphylaxis / mild anaphylactic reaction | Widespread urticarial rash with mild tachycardia (HR 105) raises concern for a systemic allergic/anaphylactic process, even though no angioedema or respiratory compromise is present at this time. |
| 4 | Maculopapular drug eruption | Although the patient reports no current medications, unrecognized or recent ingestion of a substance could cause a widespread blotchy macular-papular rash on torso and upper arms as seen on exam. |
| 5 | Viral exanthem | A confluent erythematous blanching rash distributed over the torso and extremities in an otherwise afebrile patient with no identified trigger is consistent with a viral exanthem, though the acuity and pruritis make this less likely. |

### Case 66 — jaw_pain_er_visit

**Gold terms:** jaw pain, dental appointment, ellis type ii fracture, ellis type, dental fracture, toothache

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Dental fracture with pulpitis | Tooth #18 fracture noted on exam (described as a couple of months old) with slight tenderness at that tooth and left lower jaw pain radiating toward the ear, consistent with pulpal inflammation. |
| 2 | Cracked tooth syndrome | Chronic dental fracture at tooth #18 without obvious abscess or caries can cause intermittent or radiating pain to the jaw and ear due to mechanical stress on the pulp. |
| 3 | Temporomandibular joint disorder (TMD) | Left jaw pain radiating toward the left ear without evidence of infection, lymphadenopathy, or abscess is a classic presentation of TMJ dysfunction. |
| 4 | Periapical abscess (early/subclinical) | Fractured tooth #18 with tenderness raises concern for early periapical pathology even in the absence of visible swelling, fluctuance, or fever on exam. |
| 5 | Trigeminal neuralgia (V3 distribution) | Pain originating in the lower left jaw and radiating toward the ear in the distribution of the mandibular branch of CN V could represent trigeminal neuralgia, though the absence of episodic lancinating character makes this less likely. |

### Case 78 — asbestos_exposure_hemoptysis

**Gold terms:** asbestos exposure hemoptysis, mesothelioma, acute bronchitis, pleural effusion, thoracentesis, risk for mesothelioma

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Malignant mesothelioma | History of asbestos exposure combined with left-sided pleural opacification on chest x-ray and hemoptysis in an 80-year-old male strongly raises concern for asbestos-related pleural malignancy. |
| 2 | Congestive heart failure with hemoptysis | Known CHF with EF 40%, bibasilar crackles, left-sided pleural effusion on CXR, and peripheral cyanosis are consistent with decompensated heart failure causing pulmonary venous hypertension and blood-tinged sputum. |
| 3 | Anticoagulant-induced pulmonary hemorrhage | Supratherapeutic INR of 3.7 on Coumadin significantly increases the risk of pulmonary hemorrhage presenting as hemoptysis with blood-mixed sputum. |
| 4 | Primary lung carcinoma (asbestos-related) | Asbestos exposure is a well-established risk factor for bronchogenic carcinoma, and the left-sided pulmonary opacification with hemoptysis warrants evaluation for a primary lung malignancy. |
| 5 | Pulmonary embolism | Atrial fibrillation, peripheral vascular disease, elevated troponin (0.085/0.074), worsening shortness of breath, and hemoptysis are consistent with pulmonary embolism, though anticoagulation with Coumadin (INR 3.7) makes this less likely but not impossible. |

### Case 92 — chest_wall_lump_consult

**Gold terms:** chest wall lump, ct of the chest, chest wall, chest, tenderness, axillae

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Costochondral osteochondroma | The 2-cm hard mass at the costosternal cartilage adjacent to the sternum, confirmed on ultrasound to be bone-related, is characteristic of an osteochondroma arising from the costochondral junction. |
| 2 | Tietze syndrome (costochondritis with swelling) | Localized tender mass at the costosternal cartilage on the left side with pain on deep inspiration is classic for Tietze syndrome, though the ultrasound finding of a bony lesion makes this less straightforward. |
| 3 | Chondrosarcoma of the chest wall | A slow-growing, hard, progressively enlarging mass related to the costal cartilage in a 56-year-old male with a positive family history of cancer warrants exclusion of chondrosarcoma. |
| 4 | Post-traumatic heterotopic ossification / callus formation | History of a car falling on the chest six years prior could explain a bone-related mass at the costochondral junction representing old healed rib/cartilage injury with ossification. |
| 5 | Metastatic lesion to the rib/sternum | A hard, enlarging bony chest wall mass in a heavy smoker (2 PPD) with family history of cancer raises concern for a metastatic deposit, particularly from a primary lung malignancy given his chronic cough and tobacco abuse. |
