import joblib
from fastapi import FastAPI, Query
import numpy as np
from typing import Optional


import warnings
warnings.filterwarnings("ignore")


app = FastAPI()
model = joblib.load("pipline.pkl")


@app.get('/predict')
def predict(age: Optional[float] = Query(..., description="Age of the person"),
    bmi: Optional[float] = Query(..., description="BMI of the person"),
    menstrual: Optional[float] = Query(..., description="Menstrual data (e.g., 0 or 1)"),
    testosterone: Optional[float] = Query(..., description="Testosterone level"),
    antral_follicle_count: Optional[float] = Query(..., description="Antral follicle count")
    ):
    if not all([age, bmi, menstrual, testosterone, antral_follicle_count]):
        return {"error": "Parameters incomplete."}
    else:
        input_array = np.array([age, bmi, menstrual, testosterone, antral_follicle_count]).reshape(1, -1)
        ml_result = model.predict(input_array)
        ml_result = ml_result.tolist()[0]
        if ml_result == 0:
            result = 'No PCOS Diagnosis detected'
        elif ml_result == 1:
            result = 'PCOS Diagnosis detected'
        
        return {"prediction": result}        
