from src.models.base_model import BaseModel
from sklearn.linear_model import LinearRegression


class LinearRegressionModel(BaseModel):

    def __init__(self, dataset: tuple):
        super(LinearRegressionModel, self).__init__(dataset)
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.model = LinearRegression()
