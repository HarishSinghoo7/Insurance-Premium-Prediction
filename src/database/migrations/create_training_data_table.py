from src.database.migrations import Migration


class CreateTrainingDataTable(Migration):

    def __init__(self):
        super(CreateTrainingDataTable, self).__init__()
        self.table = 'training_data'
        self.schema = {
            'ID': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'age': 'INT',
            'sex': 'CHAR(10)',
            'bmi': 'REAL',
            'children': 'INT',
            'smoker': 'CHAR(5)',
            'region': 'CHAR(50)',
            'expenses': 'REAL'
        }
        self.create()

