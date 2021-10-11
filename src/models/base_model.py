from src.config.logger import AppLogger
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from src.models.model_evaluation import ModelEvaluation


class BaseModel(AppLogger):

    def __init__(self, dataset: tuple):
        super(BaseModel, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.trainX, self.testX, self.trainY, self.testY = dataset
        self.best_params = {}

    def train(self):
        """Training the ML model"""
        self.log(f"{self.cur_file_path}\t\tInfo: train method invoked!")
        self.log(f"{self.cur_file_path}\t\tInfo: training {self.model.__class__.__name__} model!")

        self.model.fit(self.trainX, self.trainY)

    def get_best_hyper_parameters(self, estimator, parameters: dict,
                                  search_method='GridSearchCV', cv=5,
                                  scoring='r2', n_jobs=-1, verbose=0):
        """Performing hyper parameter tuning
        :parameter
        ----------
        estimator: object
                Model object
        parameters: dictionary
                hyper parameters in key values
        search_method: string
                default GridSearchCV you can set RandomizedSearchCV as well
        cv: int
            Number of CV
        scoring: string
            evaluation method used in cross validation like r2, precision, recall, f1 etc.. Default r2
        n_jobs: int
            number of jobs running into cpu. Default -1 all cpu cores
        verbose: int
            Default 0 didn't print anything. > 0 print the progress
        """
        self.log(f"{self.cur_file_path}\t\tInfo: train method invoked!")

        if search_method == 'RandomizedSearchCV':
            search_cv = RandomizedSearchCV(
                estimator=estimator,
                param_distributions=parameters,
                cv=cv,
                scoring=scoring,
                n_jobs=n_jobs,
                verbose=verbose)
        else:
            search_cv = GridSearchCV(
                estimator=estimator,
                param_grid=parameters,
                cv=cv,
                scoring=scoring,
                n_jobs=n_jobs,
                verbose=verbose)

        search_cv.fit(self.trainX, self.trainY)
        return search_cv.best_params_

    def get_model_evaluation(self):
        """Handle model evaluation process and save model evaluation details in database"""

        self.log(f"{self.cur_file_path}\t\tInfo: model_evaluation method invoked for {self.model.__class__.__name__}!")

        evaluation = ModelEvaluation(self.model, (self.trainX, self.trainY), (self.testX, self.testY))
        return evaluation.get_evaluation_report()
