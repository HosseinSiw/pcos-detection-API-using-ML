import joblib
from fastapi import FastAPI
import numpy as np


import warnings
warnings.filterwarnings("ignore")


app = FastAPI()
model = joblib.load("pipline.pkl")


@app.get('/predict')
def predict(age, bmi, menstrual, testosterone, antral_follicle_count):
    if not age or not bmi or not menstrual or not testosterone or not antral_follicle_count:
        return {"error": "Parameters incomplete."}
    else:
        input_array = np.array([age, bmi, menstrual, testosterone, antral_follicle_count]).reshape(1, -1)
        result = model.predict(input_array)
        return {"prediction": result}        
