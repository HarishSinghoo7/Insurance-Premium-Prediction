from src.config.logger import AppLogger
import sqlite3
from src.database.db_exceptions import DBConnectionException


class DBConnection(AppLogger):
    def __init__(self):
        super(DBConnection, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)
        try:
            conf = self.get_config()
            self.connection = sqlite3.connect(database=conf['db_name'])
            self.cursor = self.connection.cursor()
        except Exception as ex:
            self.log(f"{self.cur_file_path}\t\tError: Unable to connect with database!")
            raise DBConnectionException()

    def execute(self, query):
        resp = self.cursor.execute(query)
        if "create" in str.lower(query):
            pass
        elif "insert" in str.lower(query) or "update" in str.lower(query):
            self.connection.commit()
            return resp
        else:
            return self.cursor.fetchall()
