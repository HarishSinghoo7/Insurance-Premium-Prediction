from src.config.logger import AppLogger
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

import numpy as np


class ModelEvaluation(AppLogger):

    def __init__(self, model_obj, train_data: tuple, test_data: tuple):
        super(ModelEvaluation, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.trainX, self.trainY = train_data
        self.testX, self.testY = test_data
        self.train_pred = model_obj.predict(self.trainX)
        self.test_pred = model_obj.predict(self.testX)

    def get_evaluation_report(self):
        """Generate regression model evaluation report
        :return
        -------
        dictionary with train and test metrics values
        """
        metrics = {
            'train': {
                'r2_score': self.get_r2_score(train=True),
                'mae': self.get_mae(train=True),
                'mse': self.get_mse(train=True),
                'rmse': self.get_rmse(train=True)
            },
            'test': {
                'r2_score': self.get_r2_score(),
                'mae': self.get_mae(),
                'mse': self.get_mse(),
                'rmse': self.get_rmse()
            }
        }
        self.save_evaluation_report(metrics)
        return metrics

    def get_r2_score(self, train=False):
        """Return model's r2 score"""
        if train:
            return r2_score(self.trainY, self.train_pred)

        return r2_score(self.testY, self.test_pred)

    def get_mae(self, train=False):
        """Return model's mae score"""
        if train:
            return mean_absolute_error(self.trainY, self.train_pred)

        return mean_absolute_error(self.testY, self.test_pred)

    def get_mse(self, train=False):
        """Return model's mse score"""
        if train:
            return mean_squared_error(self.trainY, self.train_pred)

        return mean_squared_error(self.testY, self.test_pred)

    def get_rmse(self, train=False):
        """Return model's rmse score"""
        if train:
            return np.sqrt(mean_squared_error(self.trainY, self.train_pred))

        return np.sqrt(mean_squared_error(self.testY, self.test_pred))

    def save_evaluation_report(self, metrics):
        """Save model's train and test metrics into database"""
        pass
