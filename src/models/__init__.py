from src.config.logger import AppLogger


class ModelTraining(AppLogger):

    def __init__(self, train_test_data: tuple):
        super(ModelTraining, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.train_test_data = train_test_data

    def start_training(self):
        # Train Linear Regression Model

        # Train Random Forest Regression Model

        # Train XGBoost Regression Model

        # Train SVM Regression Model

        pass

    def save_best_fitted_model(self):
        # Evaluate Linear Regression Model

        # Evaluate Random Forest Regression Model

        # Evaluate XGBoost Regression Model

        # Evaluate SVM Regression Model

        # save best fitted model

        pass
