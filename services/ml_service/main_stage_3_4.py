# mle_projects/mle-project-sprint3-v001/services/ml_service/main_stage_3_4.py

# ---------- IMPORTS ---------- #
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import pandas as pd
import time
import numpy as np

from prometheus_client import Counter, Histogram, Gauge
from prometheus_fastapi_instrumentator import Instrumentator

from ml_service.model_handler import ModelHandler
from ml_service.query_check import QueryValidator

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

# ---------- METRICS ---------- #
REQUEST_COUNTER = Counter(
    'predictions_total',
    'Total number of prediction requests received'
)

PREDICTION_LATENCY = Histogram(
    'prediction_latency_seconds',
    'Histogram of prediction latency (seconds)'
)

# Histogram of prediction values
PREDICTIONS_HISTOGRAM = Histogram(
    'main_app_predictions',
    'Histogram of predictions'
)

# Gauge for in-progress requests
INPROGRESS_REQUESTS = Gauge(
    'inprogress_requests',
    'Number of requests currently in progress'
)

# ---------- FASTAPI APP ---------- #
app = FastAPI(title='Real Estate Price Prediction API')
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# ---------- MODEL & VALIDATOR ---------- #
model_handler = ModelHandler(model_filename='best_model_hyperparameter_optimization.pkl')
validator = QueryValidator(REQUIRED_MODEL_PARAMS)

# ---------- SCHEMA ---------- #
class PredictionRequest(BaseModel):
    apartment_id: str
    model_params: dict

# ---------- PREDICT ENDPOINT ---------- #
@app.post('/predict')
def predict(request: PredictionRequest):
    INPROGRESS_REQUESTS.inc()
    start_time = time.time()
    REQUEST_COUNTER.inc()

    try:
        params = request.dict()
        if not validator.validate(params):
            raise HTTPException(status_code=400, detail="Invalid request parameters")

        X = pd.DataFrame([params['model_params']])
        y_pred = model_handler.predict(X)[0]

        PREDICTIONS_HISTOGRAM.observe(y_pred)

        latency = time.time() - start_time
        PREDICTION_LATENCY.observe(latency)

        return {'apartment_id': params['apartment_id'], 'price': y_pred, 'latency_sec': round(latency, 4)}
    finally:
        INPROGRESS_REQUESTS.dec()

