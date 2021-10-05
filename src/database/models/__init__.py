from src.database import DBConnection

class DBModel(DBConnection):
    table = ''
    select = '*'

    def __init__(self):
        super(DBModel, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)

    def create(self, data: dict):
        try:
            self.log(f"{self.cur_file_path}\t\t{self.table} entered create method")

            query = "INSERT INTO " + self.table +\
                    " ( " + ', '.join(data.keys()) + ") VALUES ('" + "', '".join(map(str, data.values())) + "')"

            self.log(f"{self.cur_file_path}\t\t{self.table} executing query: {query}")

            return self.execute(query)
        except Exception as ex:
            self.log(f"{self.cur_file_path}\t\t{self.table} InsertException: {ex}")

    def update(self, data:dict, cond: dict):
        try:
            self.log(f"{self.cur_file_path}\t\t{self.table} entered update method")

            query = "UPDATE " + self.table + " SET " + self.__dict_to_str(data) + " WHERE " + self.__dict_to_str(cond)

            self.log(f"{self.cur_file_path}\t\t{self.table} executing query: {query}")

            return self.execute(query)
        except Exception as ex:
            self.log(f"{self.cur_file_path}\t\t{self.table} UpdateException: {ex}")

    def delete(self, cond: dict):
        try:
            self.log(f"{self.cur_file_path}\t\t{self.table} entered delete method")

            query = "DELETE FROM " + self.table + " WHERE " + self.__dict_to_str(cond)

            self.log(f"{self.cur_file_path}\t\t{self.table} executing query: {query}")
            return self.execute(query)
        except Exception as ex:
            self.log(f"{self.cur_file_path}\t\t{self.table} DeleteException: {ex}")

    def find(self, id):
        try:
            self.log(f"{self.cur_file_path}\t\t{self.table} entered find method")

            query = "SELECT " + self.select + " FROM " + self.table + " WHERE id =" + id

            self.log(f"{self.cur_file_path}\t\t{self.table} executing query: {query}")

            return self.execute(query)
        except Exception as ex:
            self.log(f"{self.cur_file_path}\t\t{self.table} FindByIdException: {ex}")

    def fetch(self, cond: dict=None):
        try:
            self.log(f"{self.cur_file_path}\t\t{self.table} entered fetch method")
            if cond:
                query = "SELECT " + self.select + " FROM " + self.table + " WHERE " + self.__dict_to_cond(cond)
            else:
                query = "SELECT " + self.select + " FROM " + self.table

            self.log(f"{self.cur_file_path}\t\t{self.table} executing query: {query}")

            return self.execute(query)
        except Exception as ex:
            self.log(f"{self.cur_file_path}\t\t{self.table} FetchException: {ex}")

    def __dict_to_str(self, data):
        query = ""
        for field, value in data.items():
            query += f"{field} = '{value}', "
        return query.rstrip(',')

    def __dict_to_cond(self, data):
        query = ""
        for field, value in data.items():
            query += f"{field} = '{value}' and "
        return query.rstrip(' and ')