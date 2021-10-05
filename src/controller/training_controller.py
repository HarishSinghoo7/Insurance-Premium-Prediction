from src.controller import Controller
from src.helpers.data_validator import DataValidator
from src.data_preprocessing import DataPreprocessing
from src.models import ModelTraining

import pandas as pd
import glob
import os


class TrainingController(Controller):
    # dir_path = os.path

    def __init__(self):
        super(TrainingController, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.data_dir = self.config['DEFAULT']['TRAINING_DATA_FOLDER']

    def start_training(self):
        try:
            self.log(f"{self.cur_file_path}\t\tInfo: Training Process Started!")
            # Filter training data dir
            self.__filter_training_data_files()

            # Merge all valid files data
            training_data = self.__merge_training_data()

            if training_data:
                # Data Preprocessing
                train_test_data = DataPreprocessing(training_data, True).get_preprocessed_data()

                # Model Training
                training = ModelTraining(train_test_data)
                training.start_training()

                # Saving Best fitted model
                training.save_best_fitted_model()

                return "Training complete!"
            else:
                raise Exception("Error: No valid dataset found for training!")
        except Exception as ex:
            self.log(f"{self.cur_file_path}\t\tError: {str(ex)}")
            return str(ex)

    def __filter_training_data_files(self):
        """Filter training data files by moving invalid files into archive_data directory """

        self.log(f"{self.cur_file_path}\t\tInfo: Validating training data!")
        # Read all files from data_dir
        training_files = glob.glob(os.path.join(self.data_dir, '*'))

        # Validate file_names and file_data
        for file_path in training_files:
            try:
                self.log(f"{self.cur_file_path}\t\tInfo: Validating {file_path}")
                DataValidator().bulk_data_validate(file_path, True)
            except Exception as ex:
                self.log(f"{self.cur_file_path}\t\tError: {str(ex)}")

                archive_dir = self.config['DEFAULT']['ARCHIVE_DATA']
                filename = os.path.basename(file_path)
                # Move file into archive_data directory
                self.log(f"{self.cur_file_path}\t\tInfo: moving file {filename} into {archive_dir}")
                os.replace(file_path, os.path.join(archive_dir, filename))

    def __merge_training_data(self):
        """Merge all training dataset files data and remove the duplicate data"""

        self.log(f"{self.cur_file_path}\t\tInfo: Merging all training data and removing duplicate rows!")
        training_files = glob.glob(os.path.join(self.data_dir, '*'))

        for i, file_path in enumerate(training_files):
            df = pd.read_csv(file_path)
            if i == 0:
                training_data = df
            else:
                training_data = training_data.append(df, ignore_index=True)
        return training_data.drop_duplicates()

