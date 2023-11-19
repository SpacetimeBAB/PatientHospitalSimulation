import random

DiseaseList = [
    "Influenza", "Common cold", "Tuberculosis", "HIV", "Sprained ankle", "Malaria", "COVID-19", "Cholera",
    "Measles", "Diabetes mellitus", "Hypertension (High blood pressure)", "Cancer", "Alzheimer's disease",
    "Fractured bone", "Asthma", "Chronic obstructive pulmonary disease (COPD)", "Hepatitis B", "Concussion",
    "Dengue fever", "Ebola virus disease", "Leukemia", "Schizophrenia", "Bipolar disorder", "Epilepsy",
    "Rheumatoid arthritis", "Osteoarthritis", "Cystic fibrosis", "Multiple sclerosis", "Sickle cell anemia",
    "Osteoporosis", "Glaucoma", "Cataracts", "Eczema", "Psoriasis", "Irritable bowel syndrome (IBS)", "Crohn's disease",
    "Ulcerative colitis", "Celiac disease", "Gout", "Sprained wrist", "Chlamydia", "Gonorrhea", "Syphilis",
    "Cholecystitis (Gallbladder inflammation)", "Appendicitis", "Pancreatitis",
    "Gastroesophageal reflux disease (GERD)", "Hemorrhoids", "Pneumonia", "Bronchitis", "Encephalitis", "Epiglottitis",
    "Myocardial infarction (Heart attack)", "Congestive heart failure", "Atherosclerosis", "Deep vein thrombosis (DVT)",
    "Pulmonary embolism", "Nephritis (Kidney inflammation)", "Renal failure", "Polycystic kidney disease",
    "Uterine fibroids", "Endometriosis", "Polycystic ovarian syndrome (PCOS)", "Prostate cancer", "Testicular cancer",
    "Ovarian cancer", "Breast cancer", "Colon cancer", "Esophageal cancer", "Leukemia", "Hodgkin's lymphoma",
    "Non-Hodgkin's lymphoma", "Melanoma", "Hypothyroidism", "Hyperthyroidism", "Addison's disease", "Graves' disease",
    "Systemic lupus erythematosus (SLE)", "Fibromyalgia", "Chronic fatigue syndrome (CFS)", "Sarcoidosis",
    "Myasthenia gravis", "Amyotrophic lateral sclerosis (ALS)", "Cerebral palsy", "Down syndrome", "Turner syndrome",
    "Klinefelter syndrome", "Sickle cell disease", "Marfan syndrome", "Sprained knee", "Huntington's disease",
    "Hemophilia", "Thalassemia", "Gaucher's disease", "Fractured rib", "Hemochromatosis", "Cysticercosis", "Leprosy",
    "Yellow fever", "Rabies",
]

HealthStatus = ["Good", "Perfect", "Decent", "Lethal", "Basically dead", "Horrible"]


def getRandomDisease():
    return random.choice(DiseaseList)


def getRandomHealthStatus():
    return random.choice(HealthStatus)
