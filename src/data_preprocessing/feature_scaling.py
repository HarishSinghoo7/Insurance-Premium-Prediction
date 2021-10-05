from src.config.logger import AppLogger
from sklearn.preprocessing import StandardScaler
from src.helpers.file_handler import FileHandler
from sklearn.model_selection import train_test_split

import pandas as pd


class FeatureScaling(AppLogger):

    def __init__(self, dataset: pd.DataFrame(), train: bool = False):
        super(FeatureScaling, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.dataset = dataset
        self.train = train
        self.file_handler = FileHandler()

    def scale(self):
        if self.train:
            # Scale training data
            train_x, test_x, train_y, test_y = train_test_split(self.dataset, test_size=0.20, random_state=21)
            train_x = self.__scale_training_data(train_x, train_y)
            test_x = self.__scale_testing_data(test_x)
            return train_x, test_x, train_y, test_y
        else:
            # Scale testing data
            return self.__scale_testing_data(self.dataset)

    def __scale_training_data(self, features, target):
        sc = StandardScaler()
        sc.fit(features, target)
        # Saving scale object
        self.file_handler.save_pickle(sc, 'scaler.pkl')
        return sc.transform(features)

    def __scale_testing_data(self, features):
        sc = self.file_handler.load_pickle('scaler.pkl')
        return sc.transform(features)
