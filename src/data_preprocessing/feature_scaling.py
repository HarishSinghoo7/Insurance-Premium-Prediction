from src.config.logger import AppLogger
from sklearn.preprocessing import StandardScaler
from src.helpers.file_handler import FileHandler
from sklearn.model_selection import train_test_split

import pandas as pd


class FeatureScaling(AppLogger):

    def __init__(self, dataset: pd.DataFrame(), train: bool = False):
        super(FeatureScaling, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.X = dataset.drop('expenses', axis=1)
        self.Y = dataset.expenses
        self.train = train
        self.file_handler = FileHandler()

    def scale(self):
        """Handle data scaling process and save scaling object inside configured directory
        :return
        -------
        if train = true it will return train-test split result as a tuple
        otherwise numpy array of StandardScaler transformation
        """
        self.log(f"{self.cur_file_path}\t\tInfo: scale method invoked!")
        if self.train:
            # Scale training data
            train_x, test_x, train_y, test_y = train_test_split(self.X, self.Y, test_size=0.20, random_state=101)
            train_x = self.__scale_training_data(train_x, train_y)
            test_x = self.__scale_testing_data(test_x)
            return train_x, test_x, train_y, test_y
        else:
            # Scale testing data
            return self.__scale_testing_data(self.dataset)

    def __scale_training_data(self, features, target):
        """Scaling the training data by using the StandardScaler and saving the object
        :parameter
        ---------
        features: DataFrame of Independent features
        target: pandas series (dependent features)
        """

        self.log(f"{self.cur_file_path}\t\tInfo: __scale_training_data method invoked!")

        sc = StandardScaler()
        sc.fit(features, target)
        # Saving scale object
        self.file_handler.save_pickle(sc, 'scaler.pkl')
        return sc.transform(features)

    def __scale_testing_data(self, features):
        """Scaling the testing data by loading the saved scaler object
        :parameter
        ---------
        features: DataFrame of Independent features
        """
        self.log(f"{self.cur_file_path}\t\tInfo: __scale_testing_data method invoked!")

        sc = self.file_handler.load_pickle('scaler.pkl')
        return sc.transform(features)
