from src.config.logger import AppLogger


class BaseModel(AppLogger):

    def __init__(self, dataset: tuple):
        super(BaseModel, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.dataset = dataset
        