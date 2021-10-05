class DBConnectionException(Exception):
    def __init__(self, msg: str="Error: Unable to connect with database"):
        self.msg = msg
        super(DBConnectionException, self).__init__(msg)

    def __str__(self):
        return self.msg