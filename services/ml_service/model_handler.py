# mle_projects/mle-project-sprint3-v001/services/ml_service/model_handler.py

import os
import joblib
import numpy as np
import pandas as pd

class ModelHandler:
    '''
        Handles loading a CatBoost model and making predictions.
    '''

    def __init__(self, model_filename: str):
        # Directory of the current script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # The model is in ../../models relative to this script
        self.model_path = os.path.join(base_dir, '..', 'models', model_filename)
        self.model_path = os.path.normpath(self.model_path)
        self.model = None
        self.load_model()

    def load_model(self):
        try:
            with open(self.model_path, 'rb') as fd:
                self.model = joblib.load(fd)
                print(f'Model loaded successfully from {self.model_path}')
        except Exception as e:
            print(f'Failed to load model: {e}')
            self.model = None

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        if self.model is None:
            raise RuntimeError('Model has not been loaded')
        y_pred_log = self.model.predict(X)
        y_pred = np.expm1(y_pred_log)
        return y_pred


## ---------- IMPORTS ---------- #
#import os
#import joblib
#import numpy as np
#import pandas as pd
#from catboost import CatBoostRegressor
#
## ---------- CONFIG ---------- #
#PROJECT_3_PATH = '/home/mle-user/mle_projects/mle-project-sprint3-v001'
#
## ---------- MODEL LOADING AND PREDICTION ---------- #
#class ModelHandler:
#    '''
#        Handles loading a CatBoost model and making predictions.
#    '''
#
#    def __init__(self, model_filename: str):
#        self.model_path = os.path.join(PROJECT_3_PATH, 'services', 'models', model_filename)
#        mle_projects/mle-project-sprint3-v001/services/models/best_model_hyperparameter_optimization.pkl
#        self.model = None
#        self.load_model()
#
#    def load_model(self):
#        try:
#            with open(self.model_path, 'rb') as fd:
#                self.model = joblib.load(fd)
#                print("Model loaded successfully")
#        except Exception as e:
#            print(f"Failed to load model: {e}")
#            self.model = None
#
#    def predict(self, X: pd.DataFrame) -> np.ndarray:
#        if self.model is None:
#            raise RuntimeError("Model is not loaded!")
#        y_pred_log = self.model.predict(X)
#        y_pred = np.expm1(y_pred_log)
#        return y_pred
#    
## ---------- MAIN EXECUTION ---------- #
#if __name__ == '__main__':
#
#    # Test model loading
#    handler = ModelHandler(model_filename='best_model_hyperparameter_optimization.pkl')
#    
#    # Test prediction
#    import pandas as pd
#    test_data = pd.DataFrame([{
#        'f1': 3.0,
#        'f2': 0.0,
#        'f5': 2.0,
#        'f6': 3.0,
#        'f7': 3.0,
#        'f8': 3.0,
#        'f9': 3.0,
#        'f15': 4.0,
#        'f17': 4.0,
#        'f19': 4.0,
#        'f20': 3.0,
#        'f21': 1.0,
#        'f23': 2.0,
#        'f24': 4.0,
#        'f25': 4.0,
#        'f26': 3.0,
#        'f27': 3.0,
#        'f28': 3.0,
#        'f29': 0.0,
#        'f31': 2.0,
#        'f32': 3.0,
#        'f33': 4.0,
#        'f34': 3.0,
#        'f35': 3.0,
#        'f36': 3.0,
#        'f39': 4.0,
#        'f41': 4.0,
#        'f43': 4.0,
#        'f44': 2.0,
#        'f45': 4.0,
#        'f47': 3.0,
#        'f48': 2.0,
#        'f49': 3.0,
#        'f50': 2.0,
#        'f51': 4.0,
#        'f52': 3.0,
#        'f53': 4.0,
#        'f54': 3.0,
#        'f55': 3.0,
#        'f56': 3.0,
#        'f57': 4.0,
#        'f58': 3.0,
#        'f59': 3.0,
#        'f60': 3.0,
#        'f61': 3.0,
#        'f62': 3.0,
#        'f63': 3.0,
#        'f64': 3.0,
#        'building_type': 2,
#        'build_decade': 2010
#    }])
#    
#    pred = handler.predict(test_data)
#    print(f'Price prediction: {pred}')