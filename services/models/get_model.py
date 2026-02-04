import mlflow
import dill

class ColumnExtractor(object):
    def __init__(self, cols):
        self.cols = cols

    def transform(self, X):
        return X[:, self.cols]
    
    def fit(self, X, y=None):
        return self

TRACKING_SERVER_HOST = "127.0.0.1"
TRACKING_SERVER_PORT = 5000

registry_uri = f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}"
tracking_uri = f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}"

mlflow.set_tracking_uri(tracking_uri)
mlflow.set_registry_uri(registry_uri)

RUN_ID = 'dee2b68b897f4c529aaca23369b1a1da'
loaded_model = mlflow.sklearn.load_model(f'runs:/{RUN_ID}/models')

with open('model.pkl', 'wb') as f:
    dill.dump(loaded_model, f)

print(f"Модель сохранена в model.pkl")
