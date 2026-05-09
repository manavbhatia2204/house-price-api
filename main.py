from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

Instrumentator().instrument(app).expose(app)

model = joblib.load("model.pkl")


class HouseInput(BaseModel):
    GrLivArea: float
    OverallQual: float
    GarageCars: float


@app.get("/")
def home():
    return {"message": "House Price Prediction API is running"}


@app.post("/predict")
def predict(data: HouseInput):
    input_data = pd.DataFrame([data.dict()])
    
    input_data = input_data.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )
    
    prediction = model.predict(input_data)[0]
    
    return {
        "predicted_price": float(prediction)
    }