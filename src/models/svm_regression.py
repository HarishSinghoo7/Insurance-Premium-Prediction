from src.models.base_model import BaseModel
from sklearn.svm import SVR

import numpy as np


class SupportVectorRegressorModel(BaseModel):

    hyper_params = {
        'degree': range(1, 6),
        'epsilon': np.linspace(0.01, 1, 10)
    }

    def __init__(self, dataset: tuple):
        super(SupportVectorRegressorModel, self).__init__(dataset)
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.model = SVR(**self.get_best_hyper_parameters(SVR(), self.hyper_params))
