from src.config.logger import AppLogger


class ModelEvaluation(AppLogger):

    def __init__(self, model_obj, dataset: tuple):
        super(ModelEvaluation, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.dataset = dataset
        self.model_obj = model_obj

    def evaluate(self):
        # Evaluate model
        pass