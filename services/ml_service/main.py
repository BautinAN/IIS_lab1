from fastapi import FastAPI
from api_handler import FastAPIHandler, PredictionRequest
from prometheus_client import Histogram, make_asgi_app, Counter
from contextlib import asynccontextmanager

PREDICTION_CLASS = Histogram(
    'ml_prediction_class_histogram',
    'Распределение классов качества предсказаний смартфонов',
    buckets=[0, 1, 2, 3]
)

metrics_app = make_asgi_app()

REQUESTS_TOTAL = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

app = FastAPI()
app.handler = FastAPIHandler()

@app.middleware("http")
async def prometheus_middleware(request, call_next):
    try:
        response = await call_next(request)
        REQUESTS_TOTAL.labels(
            method=request.method,
            endpoint=request.url.path,
            status=str(response.status_code) 
        ).inc()
        return response
    except Exception:
        REQUESTS_TOTAL.labels(
            method=request.method,
            endpoint=request.url.path,
            status="500"
        ).inc()
        raise 


@app.get('/')
def root_dir():
    return {'Hello': 'World'}

@app.post("/api/prediction")
async def prediction_endpoint(item_id: int, item_features: dict):
    import random
    if random.random() < 0.2:
        1/0  
    
    prediction = app.handler.predict(item_features)
    pred_class = int(prediction[0]) 
    PREDICTION_CLASS.observe(pred_class)
    
    return {
        "price": pred_class,
        "item_id": item_id
    }

app.mount("/metrics", metrics_app)
