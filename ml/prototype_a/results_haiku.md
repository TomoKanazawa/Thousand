# DDx Results — model: `haiku`

**Cases scored:** 37

| Metric | Hits | Rate |
|---|---|---|
| hit@1 | 28/37 | 76% |
| hit@3 | 34/37 | 92% |
| hit@5 | 36/37 | 97% |

**Tokens** — input: 47,392 · output: 14,076

## Per-case detail

### Case 01 — abdominal_pain_consult

**Gold terms:** abdominal pain, lower quadrant, abdominal, sigmoid, diverticulitis, tenderness

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Diverticulitis | 7-8 day history of persistent left lower quadrant abdominal pain with focal tenderness and palpable mass/fullness, plus recent obstipation and anorexia in elderly patient despite prior normal CT. |
| 2 | Colorectal malignancy | Persistent 7-8 day abdominal pain with left lower quadrant mass on palpation, anorexia, and obstipation symptoms in 71-year-old with last colonoscopy 5 years prior. |
| 3 | Sigmoid volvulus | Elderly thin female with obstipation, persistent abdominal pain, left lower quadrant fullness on exam, and history of factors predisposing to volvulus including pelvic pathology (grade 4 bladder prolapse). |
| 4 | Inflammatory bowel disease (Crohn's disease or ulcerative colitis) | Persistent 7-8 day abdominal pain with left lower quadrant tenderness and mass, anorexia, and obstipation, though lack of bloody diarrhea makes this less likely. |
| 5 | Ureterolithiasis or pyelonephritis | Left-sided abdominal pain with minimal left flank tenderness and history of bladder prolapse, though normal urinalysis findings and stable vital signs make infection less likely. |

### Case 03 — consult_chest_pain_1

**Gold terms:** chest pain 1, chest pain, emergency room, dull ache, precordial, shortness of breath

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Coronary artery vasospasm (Prinzmetal angina) | Prior catheterization showed suspected RCA spasm, recurrent chest pain with stress relationship, active smoker, and family history of early CAD; current presentation fits intermittent vasospastic pattern. |
| 2 | Atypical angina / Chronic stable angina | Precordial pressure-type chest pain, multiple coronary risk factors (active smoking, hyperlipidemia, family history of CAD), and prior cardiac workup suggesting borderline lesion warrant ongoing evaluation despite negative current enzymes and EKG. |
| 3 | Anxiety disorder with panic attacks | Patient is on Paxil and BuSpar (both anxiety medications), symptoms clearly stress-related with no exertional component, no diaphoresis, and psychosocial examination normal, supporting functional etiology. |
| 4 | Musculoskeletal chest pain | Dull ache quality, stress-related exacerbation, no reproducibility noted, and completely unremarkable cardiac and pulmonary workup are compatible with benign musculoskeletal origin. |
| 5 | Pulmonary embolism | Shortness of breath and chest discomfort are present; however, vital signs are stable, no risk factors documented, lungs clear on exam, and CXR unremarkable make this less likely but should remain in differential pending further workup. |

### Case 04 — consult_syncope

**Gold terms:** hypertension, hyperlipidemia, shortness of breath, coronary artery disease, seizure activity, seizure disorder

**Result:** hit at rank **3**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Hepatic encephalopathy | Elevated ammonia level (69) with syncope and recent mention of tremors in a patient with possible liver dysfunction raises concern for metabolic encephalopathy. |
| 2 | Parkinson's disease with orthostatic hypotension | Recently diagnosed Parkinson's disease with tremor documented on exam, and syncope can result from autonomic dysfunction common in advanced Parkinson's. |
| 3 | Cardiac arrhythmia (paroxysmal) | Syncope without prodromal symptoms, displaced PMI on exam, and propranolol use suggest possible underlying arrhythmia despite normal baseline EKG. |
| 4 | Seizure disorder | Patient reports possible seizure activity prior to syncope, and neurologic exam documents tremors consistent with post-ictal state. |
| 5 | Medication-related syncope (propranolol) | Patient on propranolol 40 mg daily which can cause bradycardia and hypotension leading to syncope, particularly in elderly patient with hypertension. |

### Case 06 — cough_abdominal_pain

**Gold terms:** cough abdominal pain, abdominal pain, cough, pneumonia, body aches, bronchitis

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Community-acquired pneumonia | Elderly patient with history of prior pneumonia, presenting with cough, fever, chills, coarse breath sounds bilaterally at bases, and tachycardia with tachypnea. |
| 2 | Pleurisy (pleuritis) | History of pleurisy, dry cough, fever, and right-sided abdominal pain reproducible with coughing consistent with pleural inflammation. |
| 3 | Acute bronchitis | Presentation with dry cough, generalized body aches, fever, and coarse breath sounds in an elderly patient with significant smoking history. |
| 4 | Musculoskeletal chest wall pain | Right-sided abdominal pain exclusively with coughing, absence of rebound or guarding, and tenderness on palpation suggest mechanical pain from coughing rather than visceral pathology. |
| 5 | Acute coronary syndrome | Elderly female with hypertension and prior smoking history presenting with chest discomfort, dyspnea, nausea, and tachycardia, though lack of typical anginal features makes this lower on differential. |

### Case 08 — er_report_chest_pain_fever

**Gold terms:** er report chest pain fever, chest pain, fever, hypertension, acute myocardial infarction, urinary tract infection

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute cystitis/uncomplicated urinary tract infection | Patient has positive nitrites, positive leukocyte esterase, pyuria (5-10 WBCs/hpf), and bacteria on urinalysis with recent nitrofurantoin treatment for diagnosed UTI |
| 2 | Acute pyelonephritis | Two days of increasing fever with active UTI on urinalysis and elevated temperature (99.4°F), though lack of costovertebral angle tenderness and normal renal function make this less likely |
| 3 | Stable angina or atypical angina pectoris | Substernal chest discomfort with associated nausea, diaphoresis, and dizziness in a 48-year-old with diabetes, hypertension, hyperlipidemia, and strong family history of early CAD in males, despite normal EKG and negative cardiac biomarkers |
| 4 | Musculoskeletal chest pain | Patient developed severe cramping behind left knee during stress testing and has history of arthritis; chest discomfort could be musculoskeletal rather than cardiac given clear chest on exam and negative cardiac workup |
| 5 | Meningitis (bacterial or viral) | Patient presented with fever, neck discomfort, and head discomfort prompting lumbar puncture, though CSF was normal with only 11 RBCs and 0 WBCs ruling out active meningitis |

### Case 106 — feeling_dizzy_er_visit

**Gold terms:** feeling dizzy, hypertension, tachycardia, smoking, dizzy, heart rate

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Hypertensive urgency/emergency | Patient with uncontrolled hypertension (BP 195/83) off medications for months, presenting with tachycardia and dizziness, responding to IV metoprolol |
| 2 | Alcohol withdrawal syndrome (early/impending) | Heavy daily alcohol consumption (5 glasses wine/day), last drink yesterday, patient states 'first time close to withdrawal' with palpitations and tachycardia (HR 121) |
| 3 | Supraventricular tachycardia or other primary arrhythmia | Acute presentation with palpitations and significant tachycardia (HR 121) on EKG showing sinus tachycardia without acute ST changes |
| 4 | Thyroid storm or hyperthyroidism | Tachycardia, palpitations, and weakness presentation; however TSH is normal making thyroid disorder less likely |
| 5 | Sepsis or acute infection | Tachycardia and weakness could indicate infection; however lack of fever, normal white count, and clear respiratory/abdominal exams make acute infection less likely |

### Case 115 — gen_med_consult_10

**Gold terms:** gen med  10, hemoglobin a1c, diarrhea, diabetes mellitus type ii, hypertension, hypercholesterolemia

**Result:** hit at rank **2**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Polyarticular osteoarthritis | 77-year-old with generalized joint pain affecting hands, wrists, and knees with known osteoporosis and history of carpal tunnel releases; physical exam shows doughiness of MCP joints and wrists without significant swelling or erythema. |
| 2 | Rheumatoid arthritis | Polyarticular involvement of hands and wrists with doughiness on exam and inadequate response to NSAIDs (Daypro); age and female gender are consistent with RA presentation. |
| 3 | Medication-induced myalgia or arthralgia | Patient is on multiple medications including statins (gemfibrozil) and recent resumption of Zoloft, both of which can cause musculoskeletal symptoms; symptoms began or worsened concurrent with medication changes. |
| 4 | Polymyalgia rheumatica | Advanced age (77 years old), female gender, and generalized musculoskeletal pain affecting proximal joints; however, lack of systemic symptoms (no fever, normal inflammatory markers expected) makes this less likely. |
| 5 | Secondary hyperparathyroidism with bone disease | History of parathyroidectomy with borderline elevated calcium (10.8), elevated BUN and creatinine (54 and 1.4), known osteoporosis, and chronic diuretic use; can manifest with diffuse musculoskeletal complaints. |

### Case 118 — gen_med_consult_12

**Gold terms:** gen med  12, history of diabetes, dyspnea on exertion, uncertain etiology, weak, syncope

**Result:** hit at rank **2**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Anemia | Elderly patient with longstanding and worsening weakness, dyspnea on exertion, and no other acute cardiopulmonary findings despite preserved O2 saturation suggests possible chronic anemia. |
| 2 | Acute decompensated heart failure | History of heart disease with family history of congestive heart failure, dyspnea on exertion, and elevated blood pressure (146/80) in patient who is non-compliant with medications. |
| 3 | Hypothyroidism | Elderly female with progressive weakness, shakiness, and nonspecific symptoms in setting of poor historian status and multiple comorbidities; thyroid dysfunction commonly overlooked in older adults. |
| 4 | Acute coronary syndrome | Elderly female with cardiac risk factors (age, diabetes, hypertension, hyperlipidemia, family history of CAD), dyspnea on exertion, and nonspecific ST-segment changes on ECG warrant consideration. |
| 5 | Medication non-compliance with acute hypertensive effect | Patient is not taking any medications despite history of hypertension and heart disease, current blood pressure is elevated (146/80), and she is confused and unable to account for her medical regimen. |

### Case 119 — gen_med_consult_14

**Gold terms:** gen med  14, left otalgia, otalgia, serous otitis, atopic dermatitis, serous

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Serous otitis media (otitis media with effusion) | Left tympanic membrane effusion on exam with three-week history of otalgia and hearing difficulty that has improved, consistent with fluid accumulation in middle ear |
| 2 | Chronic rhinosinusitis | History of recurrent sinusitis, current left-sided sinus pressure and jaw pain, and past chronic left-sided headache suggest ongoing sinonasal inflammation |
| 3 | Temporomandibular joint (TMJ) disorder | Left-sided jaw pain with dental evaluation negative for tooth pathology, and no other obvious structural abnormality on exam |
| 4 | Tension-type headache | Patient denies current headache but has history of chronic left-sided headache and ongoing otalgia and sinus pressure which may be contributing factors |
| 5 | Eustachian tube dysfunction | Left tympanic membrane effusion with hearing difficulty three weeks ago, which improved but may represent incomplete resolution of Eustachian tube obstruction |

### Case 120 — gen_med_consult_15

**Gold terms:** gen med  15, tearfulness, mood swings, menopause, postsurgical menopause, mood swings and tearfulness

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Major depressive disorder | Mood swings, tearfulness, difficulty concentrating, insomnia, and dysthymic mood on exam over several months with functional impairment; prior positive response to Wellbutrin supports this diagnosis |
| 2 | Adjustment disorder with depressed mood | Recent sinusitis treatment and recent completion of antibiotics (Minocin) may represent stressor; mood changes developed over recent months with clear timeline |
| 3 | Bipolar II disorder | Rapid mood swings with tearfulness and insomnia in a 50-year-old could represent hypomanic or depressive episodes, though no clear hypomanic features are documented |
| 4 | Medication side effect (post-infection mood disturbance) | Recently completed Minocin and Duraphen II DM; some antibiotics and combination medications can affect mood, though timing and severity suggest primary psychiatric etiology more likely |
| 5 | Thyroid dysfunction (hypothyroidism) | Mood symptoms, difficulty concentrating, and insomnia can be associated with thyroid disease, though no thyromegaly noted on exam and patient denies typical hypothyroid symptoms like hair loss |

### Case 121 — gen_med_consult_16

**Gold terms:** gen med  16, short-term memory loss, anxiety, short term memory loss, memory loss, stress issues

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Age-related cognitive decline (normal aging) | 60-year-old patient with subjective memory concerns but normal mental status on examination, alert and oriented, with no objective cognitive deficits documented on neurologic exam. |
| 2 | Adjustment disorder with anxiety | Patient describes exceeding stress over 5-10 years related to widowhood and high-demand job, taking Zoloft 100 mg daily, with cognitive complaints potentially attributable to anxiety and stress rather than true memory loss. |
| 3 | Medication-related cognitive effects | Patient is on Zoloft (SSRI), Zyrtec (antihistamine), and HCTZ which can all potentially affect cognition, and subjective memory complaints may be side effects rather than primary pathology. |
| 4 | Mild cognitive impairment | Patient reports difficulty absorbing and retaining new technical information at work, though formal cognitive testing is not documented and physical examination is otherwise unremarkable. |
| 5 | Hypothyroidism | Can present with cognitive complaints and memory concerns; patient has hypertension and metabolic risk factors, though TSH and thyroid function are not documented in chart. |

### Case 132 — gen_med_consult_31

**Gold terms:** gen med  31, cerebrovascular accident, recurrent urinary tract infection, diabetes, hypoglycemia, neuropathy

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Urosepsis | Recent recurrent UTI history, Foley catheter in place, altered mental status with decreased consciousness, elevated BUN/creatinine (48/2.8), pyuria (20 WBCs), and currently on Cipro for presumed UTI |
| 2 | Acute stroke or transient ischemic attack | History of right-sided CVA with baseline aphasia now significantly worsened, acute onset confusion and somnolence over 3-4 days, asymmetric motor weakness (right 3-4/5 vs left 5/5) |
| 3 | Hypoglycemia-related encephalopathy | Blood glucose of 40 documented on presentation with poor oral intake, altered mental status and decreased consciousness, though mental status only partially improved with D50 administration |
| 4 | Medication toxicity or adverse effect | Complex polypharmacy including opioids (Percocet 4x daily), muscle relaxants (Flexeril), anticonvulsants (Neurontin), and recent Cipro initiation in setting of possible Septra allergy history |
| 5 | Acute kidney injury | Elevated creatinine 2.8 and BUN 48 with altered mental status, recent poor oral intake, and chronic diabetes with neuropathy suggesting baseline renal compromise |

### Case 133 — gen_med_consult_34

**Gold terms:** gen med  34, chronic abdominal, evaluation, chronic, epigastric, bowel

**Result:** hit at rank **3**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Hepatocellular carcinoma with metastatic disease | Young male with cirrhosis risk factors (H. pylori infection, possible chronic liver disease) presenting with too numerous to count bilobar liver masses up to 8 cm on CT, hepatomegaly with irregular border, and constitutional symptoms including 20-pound weight loss and elevated guaiac, consistent with advanced HCC with extrahepatic spread. |
| 2 | Pancreatic adenocarcinoma with metastatic disease | Extensive mass in pancreatic body and tail with peripancreatic invasion noted on CT, chronic epigastric pain radiating to back, weight loss, anorexia, and nausea/vomiting consistent with pancreatic malignancy with hepatic metastases. |
| 3 | Gastric adenocarcinoma | H. pylori positive patient with chronic epigastric pain unresponsive to triple therapy and PPI, constitutional symptoms including weight loss and loose stools, positive guaiac, and imaging showing extensive abdominal pathology suggestive of gastric malignancy with metastatic spread. |
| 4 | Cirrhosis with hepatic encephalopathy and portal hypertension | Hepatomegaly with irregular border, bilobar liver masses, constitutional symptoms, loose stools, and guaiac positive stools suggest advanced liver disease; however, patient lacks asterixis, elevated ammonia confirmation, or ascites on exam to fully support this diagnosis. |
| 5 | Peptic ulcer disease with chronic sequelae | H. pylori seropositivity with epigastric pain and nausea/vomiting initially fits PUD, but failure to improve after appropriate triple therapy, positive guaiac, hepatomegaly, and extensive CT findings suggest underlying malignancy rather than simple PUD. |

### Case 134 — gen_med_consult_35

**Gold terms:** gen med  35, fluticasone nasal inhaler, confusion and hallucinations, blood pressure, temperature, abdomen

**Result:** hit at rank **4**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Takayasu arteritis | Young Hispanic male with systemic hypertension, elevated pulse, acneiform rash, positive abdominal and femoral bruits, and CNS symptoms (confusion, hallucinations) consistent with large vessel vasculitis affecting cerebral perfusion. |
| 2 | Systemic lupus erythematosus | Young male with fever, weight loss, night sweats, CNS manifestations (confusion, hallucinations, psychosis), and potential vasculitic complications presenting with hypertension and tachycardia. |
| 3 | Acute psychotic episode (primary psychiatric disorder) | Five-day history of confusion, hallucinations, paranoid delusions, insomnia, and elevated/euphoric mood without previous psychiatric history; recent significant psychosocial stressors (new MBA program, high-stress job). |
| 4 | CNS infection (encephalitis or meningitis) | Acute onset confusion, hallucinations, behavioral changes, low-grade fever (100.8°F), tachycardia, and hypertension consistent with infectious CNS involvement, though neck stiffness not documented. |
| 5 | Amphetamine or stimulant toxicity | Acute psychosis, hallucinations, paranoia, insomnia, weight loss, tachycardia (122 bpm standing), hypertension (186/101 reclining), and anxiety despite patient denial of drug use, which may be unreliable. |

### Case 135 — gen_med_consult_36

**Gold terms:** gen med  36, decreased range of motion, coughing up blood, chest, interstitial, infiltrates

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Granulomatosis with polyangiitis (GPA) | Classic triad of upper respiratory involvement (worsening allergic rhinitis), pulmonary findings (hemoptysis, bilateral infiltrates with perihilar predominance and hilar lymphadenopathy on CT), and pauci-immune crescentic glomerulonephritis with eosinophilic infiltration on renal biopsy in an African American woman with polyarthralgias. |
| 2 | Eosinophilic granulomatosis with polyangiitis (EGPA) | Pauci-immune crescentic glomerulonephritis with prominent eosinophilic interstitial infiltrate on renal biopsy, pulmonary infiltrates with hemoptysis, systemic symptoms including migratory polyarthralgias, and constitutional symptoms suggest EGPA variant. |
| 3 | Microscopic polyangiitis | Pauci-immune crescentic glomerulonephritis with negative immunofluorescence, hemoptysis with bilateral pulmonary infiltrates, and systemic polyarthralgias are consistent with microscopic polyangiitis, though absence of typical rash and prominent eosinophils make this less likely. |
| 4 | Anti-glomerular basement membrane disease (anti-GBM) | Pauci-immune crescentic glomerulonephritis with hemoptysis and pulmonary-renal syndrome presentation; however, negative immunofluorescence and prominent eosinophilic infiltration make anti-GBM less likely. |
| 5 | Systemic lupus erythematosus | Polyarthralgias, hemoptysis, glomerulonephritis, and constitutional symptoms in a young African American woman are compatible with SLE, though negative immunofluorescence staining and pauci-immune pattern on renal biopsy make this less likely. |

### Case 136 — gen_med_consult_37

**Gold terms:** gen med  37, liver biopsy, dark urine, generalized weakness, lymph nodes, granulomatous

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Viral hepatitis (A, B, C, or EBV) | Jaundice, dark urine, hepatomegaly, splenomegaly, fever, fatigue, anorexia, and lymphadenopathy are classic for acute viral hepatitis |
| 2 | Autoimmune hepatitis | Subacute presentation with jaundice, hepatomegaly, systemic symptoms, and significant constitutional weight loss over weeks |
| 3 | Hepatic abscess or pyogenic infection | Fever, chills, night sweats, RUQ tenderness, hepatomegaly, and constitutional symptoms suggest possible infectious hepatic process |
| 4 | Hemolytic anemia | Dark urine (hemoglobinuria), jaundice, weakness, fatigue, splenomegaly, and lymphadenopathy are consistent with hemolysis |
| 5 | Cirrhosis with acute decompensation | Jaundice, hepatomegaly, splenomegaly, constitutional symptoms, and family history of brother with cirrhosis warrant consideration of progressive liver disease |

### Case 138 — gen_med_consult_39

**Gold terms:** gen med  39, abdominal pain, nausea, vomiting, fever, altered mental status

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Sepsis with acute adrenal insufficiency | Patient presents with fever, hypotension refractory to initial IVF, altered mental status, and imaging reveals edematous left adrenal with right adrenal mass (3.5cm); family history of uncle with Addison's disease suggests predisposition, and acute sepsis can precipitate adrenal crisis. |
| 2 | Bacterial meningitis | Patient has fever (102.9°C), altered mental status, lethargy, disorientation, tachycardia (HR 145), tachypnea (RR 22), and underwent LP in ER; cephalosporin was empirically administered consistent with meningitis protocol. |
| 3 | Acute pyelonephritis with urosepsis | Initial presentation included fever, abdominal pain, and urinalysis with significant hematuria (53 RBC), proteinuria (100mg), and pyuria; CT abdomen shows perinephric stranding and retroperitoneal edema; patient now septic with hypotension and altered mental status. |
| 4 | Thrombotic thrombocytopenic purpura (TTP) or hemolytic uremic syndrome (HUS) | Patient presents with fever, altered mental status, acute kidney injury (Cr 1.5 from baseline, minimal urine output), thrombocytopenia would complete pentad if present, and neurologic symptoms with hematuria and proteinuria are consistent with microangiopathic hemolytic process. |
| 5 | Acute bacterial sinusitis with intracranial involvement or cavernous sinus thrombosis | MRI brain shows acute and chronic sinusitis affecting multiple sinuses (maxillary, sphenoid, ethmoid, frontal) with air-fluid levels; patient has fever, altered mental status, and right lower extremity DVT which could suggest hypercoagulable state from severe infection. |

### Case 14 — gen_med_h_p_2

**Gold terms:** gen med h p 2, weakness, malaise, dyspnea on exertion, weight loss, atypical pneumonia

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Pneumocystis jirovecii pneumonia (PCP) with AIDS | Young man with history of homosexual activity in Haiti, oral thrush, marked adenopathy, dyspnea on exertion, bilateral basilar crackles with interstitial infiltrates on chest X-ray, and hypoxemia (pO2 46) consistent with PCP in immunocompromised patient |
| 2 | Tuberculosis (pulmonary and disseminated) | Month-long constitutional symptoms including weakness, malaise, weight loss, fever, cachectic appearance, bilateral lung infiltrates, and marked adenopathy in high-risk patient despite recent negative PPD |
| 3 | Lymphoma with pulmonary involvement | Marked generalized adenopathy (epitrochlear, posterior cervical nodes), constitutional symptoms with weight loss, subcutaneous mobile nodules on chest wall, elevated total protein, and bilateral lung infiltrates |
| 4 | Histoplasmosis | Subacute presentation with fever, weight loss, marked adenopathy, oral thrush, hepatic involvement (elevated transaminases, hyperbilirubinemia), and bilateral lung infiltrates in immunocompromised patient |
| 5 | Community-acquired pneumonia with sepsis | Fever, tachycardia, tachypnea, hypotension, elevated respiratory rate with bilateral crackles and infiltrates on imaging, though lack of productive cough makes typical bacterial pneumonia less likely |

### Case 143 — gen_med_consult_47

**Gold terms:** gen med  47, inflammatory, degenerative, fever, lumbar spine, sacroiliac joint

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Sacroiliitis (infectious/inflammatory) | Severe left sacroiliac joint pain with fever (104°F), elevated glucose suggesting systemic inflammation, and history of sacral abscess post-spinal procedure making recurrent infection plausible. |
| 2 | Brucellosis | Fever, swollen inguinal nodes bilaterally, sacroiliac pain, and occupational exposure through active ranch work with goats and cattle in Mexico. |
| 3 | Coccidioidomycosis or Valley Fever | Fever, bilateral inguinal lymphadenopathy, elevated glucose, negative imaging despite systemic illness, and exposure history from ranch work in Mexico. |
| 4 | Tuberculosis (spinal/Pott's disease) | Chronic fever pattern, back/sacroiliac pain, elevated glucose suggesting metabolic stress, and history of spinal procedures creating risk for hematogenous spread. |
| 5 | Acute leukemia or lymphoma | Fever, bilateral inguinal lymphadenopathy, new-onset hyperglycemia, negative imaging despite severe systemic symptoms in elderly patient. |

### Case 147 — gen_med_consult_51

**Gold terms:** gen med  51, abdominal pain, nausea, vomiting, small bowel obstruction, nausea and vomiting

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Small bowel obstruction (partial/incomplete) | 89-year-old with extensive history of recurrent small bowel obstructions (20 prior episodes), presenting with acute lower abdominal pain, nausea/vomiting, dilated bowel loops on CT, and hypoactive bowel sounds despite CT showing no obvious complete obstruction. |
| 2 | Gastroenteritis | Acute onset of abdominal pain followed by nausea and vomiting with temporary pain relief post-emesis, though lacks fever or diarrhea; mild leukocytosis (WBC 12.1) could support mild inflammation. |
| 3 | Acute pancreatitis | Elevated amylase (103) with acute epigastric/abdominal pain and vomiting, though lipase is only mildly elevated (44) and pain is described as lower abdominal rather than typical epigastric location. |
| 4 | Mesenteric ischemia | Elderly patient (89 years) with acute severe abdominal pain (8/10), vomiting, and relatively benign abdominal exam (no peritonitis), though patient denies severe pain on presentation and has no obvious risk factors documented. |
| 5 | Diverticulitis | Elderly patient presenting with lower abdominal pain and mild leukocytosis (WBC 12.1), though CT findings of dilated bowel loops are atypical for uncomplicated diverticulitis and abdominal exam shows only mild tenderness without focal left-sided findings. |

### Case 16 — flank_pain_consult

**Gold terms:** flank pain, unable to urinate, urinary tract infection, flank

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute pyelonephritis | Left flank pain with urinalysis showing 3+ bacteria and history of left kidney trauma are consistent with upper urinary tract infection |
| 2 | Acute cystitis with referred flank pain | Difficulty urinating with 3+ bacteriuria suggests lower urinary tract infection, though flank localization is less typical |
| 3 | Post-traumatic left kidney injury with complications | Vague history of bruised left kidney in motor vehicle accident with current left flank pain and difficulty urinating raises concern for delayed complication |
| 4 | Small bowel obstruction or ileus | CAT scan showed focal ileus in left upper quadrant, though patient is comfortable and exam is benign, making this lower on differential |
| 5 | Ureterolithiasis | Left flank pain and difficulty urinating are classic presentations, though CAT scan specifically ruled out kidney stones |

### Case 24 — lightheaded_dizziness

**Gold terms:** lightheaded dizziness, passing out, echocardiogram, cardiac catheterizatio, normal sinus rhythm, cardiac enzyme

**Result:** hit at rank **2**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Panic disorder or anxiety disorder | Lightheadedness, dizziness, palpitations, and sensation of impending syncope with normal cardiac workup (EKG normal sinus rhythm, cardiac enzymes negative, prior echo and catheterization normal) suggest psychogenic etiology. |
| 2 | Vasovagal syncope (presyncope) | Patient reports lightheadedness, dizziness, and sensation of passing out without actual loss of consciousness, with normal vital signs and normal cardiac examination. |
| 3 | Supraventricular tachycardia (paroxysmal) | Patient describes palpitations and racing heart with chest fluttering during the episode, though EKG at presentation showed normal sinus rhythm suggesting arrhythmia had resolved. |
| 4 | Anemia | Patient presents with lightheadedness, dizziness, and shortness of breath, though H&H reported as stable making this less likely. |
| 5 | Thyroid disorder (hyperthyroidism) | Palpitations, tachycardia sensation, and lightheadedness can occur with thyroid dysfunction, though physical examination noted no thyromegaly. |

### Case 27 — dysphagia_hematemesis

**Gold terms:** dysphagia hematemesis, gi prophylaxis, hiv medications, alcohol abuse, weight, prophylaxis

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Boerhaave syndrome (esophageal rupture) | Acute onset dysphagia and hematemesis after forceful vomiting with severe chest/back pain (8/10), diffuse esophageal dilatation on CT, and elevated troponin suggesting cardiac involvement from mediastinal inflammation. |
| 2 | Mallory-Weiss tear | Hematemesis triggered by forceful vomiting after food intake with esophageal food impaction, though typically presents with self-limited bleeding rather than severe persistent chest pain. |
| 3 | Achalasia with food impaction and secondary esophagitis | Diffuse esophageal dilatation with retained food on CT and dysphagia with hematemesis, though lack of chronic dysphagia history makes this less likely. |
| 4 | Acute coronary syndrome | Severe chest pain (8/10), elevated troponin (0.040), cardiomegaly on imaging, and cardiac risk factors (HTN, heart failure, smoking), though EKG without ischemic changes and symptom onset clearly related to vomiting event makes this less likely. |
| 5 | Esophageal candidiasis with bleeding | Patient has advanced HIV with medication non-compliance (CD4 status unknown) and hematemesis, though lack of typical dysphagia prodrome and acute presentation after food impaction make this less likely as primary diagnosis. |

### Case 29 — lower_quadrant_pain

**Gold terms:** lower quadrant pain, right lower quadrant pain, white blood cell count, lower quadrant, bilirubin, quadrant

**Result:** hit at rank **2**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute pyelonephritis | Right flank pain radiating to side, fever (38.7°C), elevated WBC (20,000), and pyuria (WBC 10-25 in urine) are classic for upper UTI despite minimal dysuria symptoms. |
| 2 | Ovarian pathology (cyst, torsion, or rupture) | Premenopausal female with irregular menses, RLQ pain worse with activity, positive obturator sign, and normal appendicitis workup suggests gynecologic etiology. |
| 3 | Renal infarction or renal artery dissection | Acute-onset severe RLQ/flank pain with radiation, fever, and hematuria (blood 50 in urine) in setting of hypertension on ACE inhibitor. |
| 4 | Acute mesenteric adenitis | Elevated WBC with left shift (75 polys), RLQ tenderness with positive Rovsing sign, and negative imaging for appendicitis may represent viral mesenteric adenitis. |
| 5 | Rectus sheath hematoma | Obese patient on antihypertensive therapy with RLQ pain worse with activity, mild rebound tenderness, and umbilical hernia noted on exam. |

### Case 32 — dizziness_recurrent

**Gold terms:** dizziness recurrent, recurrent dizziness, shortness of breath, rotational sensation, earache, headaches

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Benign paroxysmal positional vertigo (BPPV) | Rotational vertigo triggered by head position changes (turning right/left, looking up, rolling in bed, arising from seated/supine position) lasting minutes with symptom relief when remaining still is classic for BPPV. |
| 2 | Orthostatic hypotension | Patient reports presyncope with positional changes (arising from bed/chair), and vital signs show increase in systolic BP from 112 to 130 mmHg with decrease in pulse from 84 to 66 upon standing, consistent with autonomic dysfunction. |
| 3 | Atrial fibrillation with inadequate rate control | Known history of atrial fibrillation with complaints of palpitations and dizziness; inadequate ventricular rate control could cause recurrent presyncope and dizziness. |
| 4 | Peripheral vestibular dysfunction (possibly age-related or post-stroke) | Tinnitus in right ear, complaint of dizziness on head turning, intact vestibuloocular reflexes on exam, and history of possible prior stroke support peripheral vestibular pathology. |
| 5 | Anxiety disorder with somatization | Patient reports sadness, extreme anxiety, demonstrates pain amplification and exaggerated responses to examination, and has tangential speech, all consistent with significant anxiety contributing to or mimicking vertigo symptoms. |

### Case 34 — neuro_consult_leg_weakness

**Gold terms:** neuro  leg weakness, hyperckemia, emg and nerve, nerve conduction studies, leg weakness, leg

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Chronic inflammatory demyelinating polyneuropathy (CIDP) | Six-month progressive right leg weakness with ankle dorsiflexion/eversion weakness, absent ankle reflexes, diminished vibratory sensation, Tinel's signs, and EMG/NCS studies performed consistent with demyelinating neuropathy workup. |
| 2 | Amyotrophic lateral sclerosis (ALS) | Right leg weakness with scant fasciculations in bilateral calves, muscle atrophy (thinning of right hamstrings/calf/quadriceps), areflexia (absent ankle jerks), and lower motor neuron findings in a patient with EMG/NCS performed. |
| 3 | Common peroneal nerve palsy | Right dorsiflexion weakness (4/5) and eversion weakness (4/5) with Tinel's sign at right fibular head, steppage gait, and inability to walk on toes consistent with localized common peroneal nerve compression. |
| 4 | Distal motor neuropathy secondary to metabolic/toxic etiology | HyperCKemia (baseline 500-600s, elevated with statin use), heavy alcohol consumption (four drinks nightly), statin exposure, and distal lower extremity weakness pattern are all potential contributors to metabolic neuropathy. |
| 5 | L5 radiculopathy from spondylosis | CT scan shows degenerative changes, right-sided weakness affecting dorsiflexion/eversion (L5 distribution), and chronic back pain, though lack of radicular pain and MRI unavailability limit diagnostic confirmation. |

### Case 36 — h_p_weakness

**Gold terms:** h p weakness, weakness, arm weakness, speech difficulties, headache, visual changes

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute ischemic stroke | Acute onset right-sided arm weakness, expressive aphasia with preserved comprehension, and mild right facial droop are classic findings for left hemisphere stroke. |
| 2 | Transient ischemic attack (TIA) | Clinical presentation of acute focal neurologic deficits (right arm weakness, expressive aphasia, facial droop) with potential for resolution fits TIA, though persistence since morning raises stroke concern. |
| 3 | Todd's paralysis (post-ictal paresis) | Patient is on Depakote and Ativan suggesting seizure history; transient focal weakness can occur post-ictal, though no witnessed seizure or loss of consciousness documented. |
| 4 | Acute coronary syndrome with neurologic complications | EKG shows ST-depression and biphasic T-waves diffusely; aortic stenosis and cardiac medications present; acute cardiac event could precipitate stroke or hypoperfusion. |
| 5 | Urosepsis with acute delirium/stroke | Elevated WBC (10,800), pyuria (608 WBCs in UA), history of recurrent UTIs, low-grade fever (99.1°F), and elevated BUN/creatinine suggest infection that could cause acute neurologic changes. |

### Case 41 — hematuria_er_visit

**Gold terms:** voiding, constipation, hematuria, foley catheter, nausea, vomiting

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Bladder cancer with hematuria | Patient has known history of bladder cancer presenting with hematuria and gross blood in urine; this is a recurrent complication in bladder cancer patients. |
| 2 | Acute urinary retention with secondary hematuria | Patient presented recently with difficulty voiding, now with Foley placement and hematuria, suggesting traumatic catheterization or underlying obstructive process from enlarged prostate. |
| 3 | Urinary tract infection with hematuria | Patient was recently treated with Levaquin for presumed UTI with negative cultures; recurrent hematuria with mild elevation in BUN/creatinine could represent inadequately treated infection. |
| 4 | Acute kidney injury | Elevated BUN of 27 and creatinine of 1.9 with hematuria suggests possible glomerulonephritis or other renal pathology, though mild elevation could reflect dehydration. |
| 5 | Benign prostatic hyperplasia with hemorrhagic cystitis | Patient has known enlarged prostate on Flomax and Proscar; chronic outlet obstruction can lead to secondary hemorrhagic cystitis presenting with hematuria. |

### Case 42 — left_lower_quadrant_pain_er_visit

**Gold terms:** left lower quadrant pain, bowel movement, constipation, fetal heart, nausea, vomiting

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Constipation with impaction | No bowel movement in two weeks, stool palpated in rectum on exam, left lower quadrant pain, and normal bowel sounds without guarding/rebound. |
| 2 | Asymptomatic bacteriuria or urinary tract infection | Many bacteria and high ketones on urinalysis with history of recurrent UTIs, though absence of white blood cells, nitrites, and dysuria are atypical. |
| 3 | Acute pyelonephritis | Bilateral lower back tenderness, nausea/vomiting, and bacteriuria on urinalysis in a patient with history of recurrent UTIs, though no costovertebral angle tenderness or fever present. |
| 4 | Substance withdrawal or intoxication | Sedated appearance with intermittent thrashing, track marks on bilateral arms, recent positive urine drug screens for multiple substances including benzodiazepines and opiates. |
| 5 | Acute abdomen secondary to other intra-abdominal pathology | Left lower quadrant pain with nausea and vomiting, though absence of guarding, rebound, fever, and normal CMP make surgical abdomen less likely. |

### Case 43 — syncope_er_visit

**Gold terms:** ejection fraction, coronary artery bypass grafting, coronary artery disease, v/q scan, bypass grafting, artery bypass

**Result:** hit at rank **5**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Vasovagal syncope | Classic presentation with prodromal abdominal discomfort, nausea, and profuse sweating followed by rapid recovery with no post-event confusion upon position change, consistent with vagal syncope. |
| 2 | Orthostatic hypotension | Patient has documented history of postural hypotension managed by her primary care physician, is on multiple antihypertensive medications (lisinopril, Lasix, Toprol), and presents with syncope. |
| 3 | Arrhythmia (bradycardia or heart block) | Patient has history of paroxysmal atrial fibrillation on amiodarone, EKG shows right bundle-branch block, and current heart rate is 50-60 bpm, which could precipitate syncope. |
| 4 | Pulmonary embolism | Patient has significant history of prior PE with similar presentation (syncope with abdominal symptoms), has IVC filter in place, and presents with abdominal discomfort and syncope, though initial V/Q scan was negative. |
| 5 | Acute coronary syndrome | Patient has extensive coronary artery disease history with prior CABG and presented with abdominal discomfort with nausea and diaphoresis, though troponin was negative x2 and no acute EKG changes documented. |

### Case 44 — syncope_er_visit_1

**Gold terms:** syncope  1, residual deficit, headache, ct scan, syncopal episode, stress test

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Orthostatic hypotension | First dose of hydrochlorothiazide given today in context of newly diagnosed hypertension with syncope episode, plus labile blood pressure (172/91 down to 139/75) consistent with medication-induced volume depletion. |
| 2 | Transient ischemic attack (TIA) or stroke | 75-year-old with syncope, headache, and newly elevated blood pressure (172/91) with nondiagnostic Q-waves on EKG suggesting prior ischemic changes; brief loss of consciousness could represent vertebrobasilar insufficiency. |
| 3 | Vasovagal syncope | Syncope occurred in non-threatening circumstance (eating cereal in bedroom) with rapid recovery and no residual deficit, consistent with reflex syncope mechanism. |
| 4 | Arrhythmia (paroxysmal) | Age 75 with syncope episode and nondiagnostic Q-waves on EKG raising concern for prior cardiac ischemia, though current EKG shows only sinus rhythm and no acute findings. |
| 5 | Acute ischemic stroke | Nondiagnostic inferior Q-waves on EKG suggest underlying coronary disease with risk for cardioembolism; headache accompanies syncope in 75-year-old with elevated blood pressure. |

### Case 48 — bilateral_hip_pain

**Gold terms:** consult - history and phy, bilateral hip pain, femoroacetabular, impingement, hip

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Femoroacetabular impingement (FAI) | Imaging shows exostosis on superior femoral neck with clinical presentation of chronic anterior groin and lateral hip pain exacerbated by activity and mechanical symptoms (clicking/popping). |
| 2 | Hip osteoarthritis | 38-year-old with 2+ years of progressive bilateral hip pain, lateral and anterior location, and minimal degenerative changes noted on X-rays. |
| 3 | Labral tear (acetabular) | Chronic groin pain with mechanical symptoms (popping/clicking) and positive findings on groin palpation, which can indicate intra-articular pathology not visible on plain films. |
| 4 | Greater trochanteric pain syndrome | Lateral hip pain with activity and female gender are consistent, though physical exam notably lacked trochanteric tenderness reducing likelihood. |
| 5 | Hip flexor strain or iliopsoas tendinitis | Anterior groin pain with activity and positive groin tenderness on exam could suggest flexor pathology, though mechanical symptoms are less typical. |

### Case 49 — consult_jaw_pain

**Gold terms:** consult - history and phy, jaw pain, mandible, numbness and tingling, teeth and tongue, nasal septum

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Trigeminal neuropathy (idiopathic or post-viral) | Two-month history of left-sided jaw and tongue numbness with decreased sensation to the lateral tongue and jaw region in a V3 distribution, following recent throat infection, with otherwise normal neurologic and structural examination. |
| 2 | Lingual nerve injury or neuropathy | Loss of sensation and taste specifically limited to left lateral tongue with normal oral examination and recent viral illness. |
| 3 | Medication-related neuropathy (post-Avelox) | Recently completed course of Avelox for throat infection with onset of numbness and tingling temporally related to medication use. |
| 4 | Bell's palsy with incomplete presentation | Recent viral infection and unilateral facial sensory changes, though full facial motor function is preserved on examination. |
| 5 | Anxiety disorder with somatization | Known history of anxiety disorder with subjective sensory complaints, though objective decreased sensation on examination somewhat supports an organic etiology. |

### Case 65 — itchy_rash_er_visit

**Gold terms:** urticaria, pruritus, lip swelling, allergic reaction, itchy rash, torso

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute urticaria | Rapid onset of blanching erythematous rash on torso and papular-macular rash on upper arms without systemic symptoms or airway involvement, consistent with non-anaphylactic urticaria. |
| 2 | Contact dermatitis | Recent exposure to insulation material days prior with subsequent development of pruritic rash in exposed areas (torso and arms), though timing is somewhat delayed. |
| 3 | Drug reaction (non-penicillin related) | Acute rash and tachycardia in patient with documented drug allergies, though patient denies recent medication changes and is not currently on medications. |
| 4 | Viral exanthem | Acute onset widespread rash affecting torso and arms in otherwise healthy young adult, though absence of systemic symptoms (fever, malaise) makes this less likely. |
| 5 | Erythema multiforme | Acute polymorphic rash with involvement of torso and extremities, though patient lacks typical target lesions and systemic symptoms typically associated with this diagnosis. |

### Case 66 — jaw_pain_er_visit

**Gold terms:** jaw pain, dental appointment, ellis type ii fracture, ellis type, dental fracture, toothache

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Dental fracture with pulpitis | Dental fracture at tooth #18 noted on examination with slight tenderness and pain radiating to jaw and ear, consistent with exposed pulp or inflammation. |
| 2 | Temporomandibular joint (TMJ) disorder | Left-sided jaw pain radiating toward ear with dental findings that may be incidental; TMJ dysfunction can mimic dental pain without obvious intraoral pathology. |
| 3 | Odontogenic infection (early or localized) | Dental fracture present with jaw pain radiating to ear, though lack of swelling, erythema, fever, and fluctuance make active abscess less likely but early infection possible. |
| 4 | Neuralgia (trigeminal or glossopharyngeal) | Unilateral jaw and ear pain with radiation pattern consistent with cranial nerve irritation, though provocative features and triggers not clearly documented. |
| 5 | Acute coronary syndrome (atypical presentation) | Age 58 with hypertension (BP 168/84) presenting with jaw pain; though pain quality and lack of chest symptoms make this less likely, jaw pain can be atypical cardiac presentation. |

### Case 78 — asbestos_exposure_hemoptysis

**Gold terms:** asbestos exposure hemoptysis, mesothelioma, acute bronchitis, pleural effusion, thoracentesis, risk for mesothelioma

**Result:** **MISS**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Acute decompensated heart failure with pulmonary edema | EF 40%, bibasilar crackles, peripheral cyanosis, worsening shortness of breath, and chest X-ray showing left-sided opacification concerning for pleural effusion |
| 2 | Pulmonary infarction secondary to pulmonary embolism | Hemoptysis with elevated troponin (0.085, 0.074), history of atrial fibrillation on anticoagulation, and acute respiratory symptoms |
| 3 | Pneumonia with sepsis | Hemoptysis, cough, respiratory rate 20, low-grade fever 99.3°F, and bibasilar crackles on lung exam |
| 4 | Acute coronary syndrome with cardiogenic shock | Elevated troponin (0.085, 0.074), extensive CAD history with prior CABG, peripheral cyanosis, and worsening dyspnea |
| 5 | Mechanical valve thrombosis or dysfunction | St. Jude mechanical aortic valve in situ, supratherapeutic INR 3.7, hemoptysis, and acute decompensation in setting of cardiac prosthesis |

### Case 92 — chest_wall_lump_consult

**Gold terms:** chest wall lump, ct of the chest, chest wall, chest, tenderness, axillae

**Result:** hit at rank **1**

| Rank | Diagnosis | Reasoning |
|---|---|---|
| 1 | Osteochondroma (benign bone tumor) | Hard mass fixed to costosternal cartilages in lower left chest wall with ultrasound showing bone-related pathology; most common benign bone tumor in this location |
| 2 | Chondrosarcoma | Progressive enlargement and tenderness over one year of a bone-related mass at costosternal junction; malignant potential of cartilaginous tumors warrants consideration |
| 3 | Tietze syndrome (costochondritis) | Localized tenderness and swelling at costosternal junction with pain on deep inspiration; inflammatory condition of costal cartilages |
| 4 | Chest wall lipoma | Palpable soft tissue mass in chest wall; though ultrasound suggests bone involvement, lipomas are common benign chest wall lesions |
| 5 | Traumatic ossification/heterotopic ossification | History of motor vehicle trauma to chest six years ago with subsequent development of hard mass related to bone |
