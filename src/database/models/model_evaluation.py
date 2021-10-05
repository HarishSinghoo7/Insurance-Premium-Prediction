from src.database.models import DBModel


class ModelEvaluation(DBModel):

    def __init__(self):
        super(ModelEvaluation, self).__init__()
        self.table = 'model_evaluation'
