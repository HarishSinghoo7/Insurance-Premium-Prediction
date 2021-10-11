from src.config.logger import AppLogger
from src.models.linear_regression import LinearRegressionModel
from src.models.random_forest_regression import RandomForestRegressorModel
from src.models.svm_regression import SupportVectorRegressorModel
from src.models.xgboost_regression import XGBRegressorModel


class ModelTraining(AppLogger):

    def __init__(self, train_test_data: tuple):
        super(ModelTraining, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.train_test_data = train_test_data
        self.__generate_model_objects()

    def start_training(self):
        """Handle model training process with different-different algorithms"""

        self.log(f"{self.cur_file_path}\t\tInfo: start_training method invoked!")
        # Train Linear Regression Model
        self.lr_model.train()

        # Train Random Forest Regression Model
        self.rfr_model.train()

        # Train SVM Regression Model
        self.svm_model.train()

        # Train XGBoost Regression Model
        self.xgb_model.train()

    def save_best_fitted_model(self):
        # Evaluate Linear Regression Model
        lr_model_eval = self.lr_model.get_model_evaluation()
        # Evaluate Random Forest Regression Model
        rfr_model_eval = self.rfr_model.get_model_evaluation()
        # Evaluate SVM Regression Model
        svm_model_eval = self.svm_model.get_model_evaluation()
        # Evaluate XGBoost Regression Model
        xgb_model_eval = self.xgb_model.get_model_evaluation()

        # save best fitted model

        pass

    def __generate_model_objects(self):
        self.log(f"{self.cur_file_path}\t\tInfo: __generate_model_objects method invoked!")

        # Generating linear model object
        self.lr_model = LinearRegressionModel(self.train_test_data)
        # Generating random forest model object
        self.rfr_model = RandomForestRegressorModel(self.train_test_data)
        # Generating SVM model object
        self.svm_model = SupportVectorRegressorModel(self.train_test_data)
        # Generating XGBoost model object
        self.xgb_model = XGBRegressorModel(self.train_test_data)