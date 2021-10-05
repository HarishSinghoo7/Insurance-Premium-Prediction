from src.database import DBConnection


class Migration(DBConnection):
    table = str
    schema = dict

    def __init__(self):
        super(Migration, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)

    def create(self):
        self.log(f"{self.cur_file_path}\t\tInfo: creating {self.table} table!")
        schema = [f"{key} {value}" for key, value in self.schema.items()]
        query = f"CREATE TABLE IF NOT EXISTS {self.table} ({', '.join(schema)})"
        self.execute(query)
