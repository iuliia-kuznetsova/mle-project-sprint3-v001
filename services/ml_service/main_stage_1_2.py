# /services/ml_service/main_stage_1_2.py

# ---------- IMPORTS ---------- #
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

from .model_handler import ModelHandler
from .query_check import QueryValidator

# ---------- CONFIG ---------- #
REQUIRED_MODEL_PARAMS = [
    'f1', 'f2', 'f5', 'f6', 'f7', 'f8', 'f9', 'f15', 'f17', 'f19', 
    'f20', 'f21', 'f23', 'f24', 'f25', 'f26', 'f27', 'f28', 'f29',
    'f31', 'f32', 'f33', 'f34', 'f35', 'f36', 'f39', 
    'f41', 'f43', 'f44', 'f45', 'f47', 'f48', 'f49',
    'f50', 'f51', 'f52', 'f53', 'f54', 'f55', 'f56', 'f57', 'f58', 'f59',
    'f60', 'f61', 'f62', 'f63', 'f64', 
    'building_type', 'build_decade'
]

# ---------- API INITIALIZATION ---------- #
# FastAPI app
app = FastAPI(title='Real Estate Price Prediction API')

# Model and validator initialization
model_handler = ModelHandler(model_filename='best_model_hyperparameter_optimization.pkl')
validator = QueryValidator(REQUIRED_MODEL_PARAMS)

# Request body schema
class PredictionRequest(BaseModel):
    apartment_id: str
    model_params: dict

# ---------- API ENDPOINT ---------- #
@app.get('/')
def read_root():
    return {
        'message': 'Welcome to the Real Estate Price Prediction API! Use the /predict endpoint to get predictions'
    }

@app.post('/predict')
def predict(request: PredictionRequest):
    params = request.dict()

    if not validator.validate(params):
        raise HTTPException(status_code=400, detail='Invalid request parameters')

    # Data 
    X = pd.DataFrame([params['model_params']])

    # Prediction
    y_pred = model_handler.predict(X)[0]

    # Result
    return {
        'apartment_id': params['apartment_id'],
        'price': y_pred
    }