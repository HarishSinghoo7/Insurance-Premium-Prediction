from src.models.base_model import BaseModel
from sklearn.ensemble import RandomForestRegressor


class RandomForestRegressorModel(BaseModel):

    hyper_params = {
        'n_estimators': range(1, 20, 2),
        'max_depth': range(5, 15, 2),
        'min_samples_split': range(10, 20, 2),
        'min_samples_leaf': range(5, 10, 1)
    }

    def __init__(self, dataset: tuple):
        super(RandomForestRegressorModel, self).__init__(dataset)
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.model = RandomForestRegressor(**self.get_best_hyper_parameters(RandomForestRegressor(), self.hyper_params))
