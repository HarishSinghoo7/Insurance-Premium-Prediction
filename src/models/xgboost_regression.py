from src.models.base_model import BaseModel
from xgboost import XGBRegressor

import numpy as np


class XGBRegressorModel(BaseModel):

    hyper_params = {
        'n_estimators': range(10, 50, 10),
        'max_depth': range(10, 20, 2),
        'gamma': np.linspace(0, 2, 5)
    }

    def __init__(self, dataset: tuple):
        super(XGBRegressorModel, self).__init__(dataset)
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.model = XGBRegressor(**self.get_best_hyper_parameters(XGBRegressor(), self.hyper_params))
