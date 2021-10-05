from src.controller import Controller
from src.database.migrations.create_training_data_table import CreateTrainingDataTable
# from src.database.migrations.create_model_evaluation_table import


class DBMigrationController(Controller):

    def __init__(self):
        super(DBMigrationController, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)

    def migrate(self):
        try:
            self.log(f"{self.cur_file_path}\t\tInfo: Migrating database!")
            CreateTrainingDataTable().create()
        except Exception as ex:
            self.log(f"{self.cur_file_path}\t\tError: {str(ex)}")
            raise Exception(ex)