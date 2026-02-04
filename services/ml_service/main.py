from fastapi import FastAPI
from api_handler import FastAPIHandler, PredictionRequest

app = FastAPI()
app.handler = FastAPIHandler()


@app.get('/')
def root_dir():
    return {'Hello': 'World'}


@app.post('/api/prediction')
def make_prediction(item_id: int, features: PredictionRequest):
    item_features = features.dict()
    prediction = app.handler.predict(item_features)[0]
    
    return {
        'price': int(prediction),
        'item_id': item_id
    }
