import logging
import pandas as pd
import numpy as np
import dill 
from pydantic import BaseModel

logger = logging.getLogger("uvicorn.error")

class ColumnExtractor(object):
    def __init__(self, cols):
        self.cols = cols

    def transform(self, X):
        return X[:, self.cols]
    
    def fit(self, X, y=None):
        return self


class PredictionRequest(BaseModel):
    battery_power: int
    blue: int
    clock_speed: float
    dual_sim: int
    fc: int
    four_g: int
    int_memory: int
    m_dep: float
    mobile_wt: int
    n_cores: int
    pc: int
    px_height: int
    px_width: int
    ram: int
    sc_h: int
    sc_w: int
    talk_time: int
    three_g: int
    touch_screen: int
    wifi: int
    screen_area: int
    pixel_density: float
    total_memory: int
    is_high_end: int


class FastAPIHandler:
    def __init__(self):
        logger.warning('Loading model...')
        try:
            with open('/models/model.pkl', 'rb') as f:
                self.model = dill.load(f)
            logger.info('Model is loaded')
        except Exception as e:
            logger.error(f'Error loading model: {e}')
            raise
    
    def predict(self, item_features: dict):
        feature_columns = [
            'battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
            'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',
            'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g',
            'touch_screen', 'wifi', 'screen_area', 'pixel_density',
            'total_memory', 'is_high_end'
        ]
        
        item_df = pd.DataFrame([item_features])
        item_df = item_df.reindex(columns=feature_columns, fill_value=0)
        
        preprocessed = self.model.named_steps['preprocessor'].transform(item_df)
        
        X_sfs = preprocessed[:, :3]
        
        logger.info(f"After manual SFS: {X_sfs.shape}")
        
        regressor = self.model.named_steps['model']
        prediction = regressor.predict(X_sfs)
        price = int(round(prediction[0]))
        
        logger.info(f"Final prediction (int): {price}")
        return np.array([price])

