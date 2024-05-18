from fastapi import FastAPI

app = FastAPI()
import pandas as pd
import random

def generate_random_patient_data():
    # Define limits for each attribute based on the provided CSV data
    age_limit = (25, 80)  # Age between 25 and 80 years
    sex_values = [0, 1]  # 0 for female, 1 for male
    cp_values = [0, 1, 2, 3]  # Chest pain type (0-3)
    trestbps_limit = (100, 180)  # Resting blood pressure (mm Hg)
    chol_limit = (150, 350)  # Serum cholesterol (mg/dl)
    fbs_values = [0, 1]  # Fasting blood sugar (0 or 1)
    restecg_values = [0, 1]  # Resting electrocardiographic results (0 or 1)
    thalach_limit = (120, 200)  # Maximum heart rate achieved (bpm)
    exang_values = [0, 1]  # Exercise induced angina (0 or 1)
    oldpeak_limit = (0.0, 4.0)  # ST depression induced by exercise relative to rest
    slope_values = [0, 1, 2]  # Slope of the peak exercise ST segment (0-2)
    ca_values = [0, 1, 2, 3]  # Number of major vessels colored by fluoroscopy
    thal_values = [0, 1, 2, 3]  # Thalassemia type (0-3)
    target_values = [0, 1]  # Target (0 for no heart disease, 1 for heart disease)

    # Generate random values for each attribute
    patient_data = {
        "age": random.randint(age_limit[0], age_limit[1]),
        "sex": random.choice(sex_values),
        "cp": random.choice(cp_values),
        "trestbps": random.randint(trestbps_limit[0], trestbps_limit[1]),
        "chol": random.randint(chol_limit[0], chol_limit[1]),
        "fbs": random.choice(fbs_values),
        "restecg": random.choice(restecg_values),
        "thalach": random.randint(thalach_limit[0], thalach_limit[1]),
        "exang": random.choice(exang_values),
        "oldpeak": round(random.uniform(oldpeak_limit[0], oldpeak_limit[1]), 1),
        "slope": random.choice(slope_values),
        "ca": random.choice(ca_values),
        "thal": random.choice(thal_values),
    }

    return patient_data
@app.get('/')
def home():
    return generate_random_patient_data()
