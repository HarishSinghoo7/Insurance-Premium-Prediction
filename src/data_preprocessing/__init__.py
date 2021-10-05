from src.config.logger import AppLogger
from src.data_preprocessing.outlier_removal import OutlierRemoval
from src.data_preprocessing.categorical_data_encoding import CategoricalDataEncoder
from src.data_preprocessing.feature_scaling import FeatureScaling

import pandas as pd


class DataPreprocessing(AppLogger):

    def __init__(self, dataset: pd.DataFrame(), train: bool = False):
        super(DataPreprocessing, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.dataset = dataset
        self.train = train

    def get_preprocessed_data(self):

        self.log(f"{self.cur_file_path}\t\tInfo: Starting data preprocessing!")
        # Data Imputation (No need with current dataset)

        # Removing outliers from numeric data bmi and expenses
        self.log(f"{self.cur_file_path}\t\tInfo: Removing outliers!")
        outlier_removal = OutlierRemoval()
        self.dataset['expenses'] = outlier_removal.log_transformation(self.dataset['expenses'])
        self.dataset['bmi'] = outlier_removal.sqrt_transformation(self.dataset['bmi'])
        self.dataset['bmi'] = outlier_removal.winsorizing(self.dataset['bmi'])

        # Categorical Data Encoding
        self.log(f"{self.cur_file_path}\t\tInfo: Encoding categorical data!")
        self.dataset = CategoricalDataEncoder(self.dataset, train=self.train).one_hot_encoder()

        # Feature Scaling
        self.log(f"{self.cur_file_path}\t\tInfo: Feature scaling!")
        return FeatureScaling(self.dataset, self.train).scale()
