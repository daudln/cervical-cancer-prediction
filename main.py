from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import joblib
import pandas as pd
from schema.input import InputData


origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:8081",
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict/")
async def predict_cancer(data: InputData):
    input_data = pd.DataFrame([data.model_dump()])
    model = joblib.load("cancer_model_best.joblib")
    predictions = model.predict(input_data)

    prediction_result = "Positive" if predictions[0] == 1 else "Negative"

    return {"prediction": prediction_result}