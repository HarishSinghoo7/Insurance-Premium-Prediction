from src.config.logger import AppLogger
from scipy import stats

import pandas as pd
import numpy as np


class OutlierRemoval(AppLogger):

    def __init__(self):
        super(OutlierRemoval, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)

    def log_transformation(self, data: pd.Series()):
        self.log(f"{self.cur_file_path}\t\tInfo: log_transformation method invoked!")
        return np.log(data)

    def reverse_log_transformation(self, data: pd.Series()):
        self.log(f"{self.cur_file_path}\t\tInfo: reverse_log_transformation method invoked!")
        return np.exp(data)

    def sqrt_transformation(self, data: pd.Series()):
        self.log(f"{self.cur_file_path}\t\tInfo: sqrt_transformation method invoked!")
        return np.sqrt(data)

    def reverse_sqrt_transformation(self, data: pd.Series()):
        self.log(f"{self.cur_file_path}\t\tInfo: reverse_sqrt_transformation method invoked!")
        return np.square(data)

    def winsorizing(self, data: pd.Series, limits: tuple = (0.1, 0.1)):
        self.log(f"{self.cur_file_path}\t\tInfo: winsorizing method invoked!")
        return stats.mstats.winsorize(data, limits)
