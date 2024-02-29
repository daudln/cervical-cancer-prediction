from fastapi import FastAPI

import joblib
import pandas as pd
from schema.input import InputData

app = FastAPI()


@app.post("/predict/")
async def predict_cancer(data: InputData):
    input_data = pd.DataFrame([data.model_dump()])
    model = joblib.load("cancer_model_best.joblib")
    predictions = model.predict(input_data)

    prediction_result = "Positive" if predictions[0] == 1 else "Negative"

    return {"prediction": prediction_result}