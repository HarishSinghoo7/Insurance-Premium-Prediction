from src.config.logger import AppLogger
from scipy import stats

import pandas as pd
import numpy as np


class OutlierRemoval(AppLogger):

    def __init__(self):
        super(OutlierRemoval, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)

    def log_transformation(self, data: pd.Series()):
        return np.log(data)

    def reverse_log_transformation(self, data: pd.Series()):
        return np.exp(data)

    def sqrt_transformation(self, data: pd.Series()):
        return np.sqrt(data)

    def reverse_sqrt_transformation(self, data: pd.Series()):
        return np.square(data)

    def winsorizing(self, data: pd.Series, limits: tuple = (0.1, 0.1)):
        return stats.mstats.winsorize(data, limits)
