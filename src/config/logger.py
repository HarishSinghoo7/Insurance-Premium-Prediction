from datetime import datetime
from src.config.config import ConfigReader
from src.helpers.file_handler import FileHandler
import os

class AppLogger(ConfigReader):
    def __init__(self):
        super(AppLogger, self).__init__()
        self.log_dir = self.config['DEFAULT']['LOG_DIR']
        self.file_handler = FileHandler()

    def log(self, msg: str, **kwargs):
        """
        Description: Record logs in file
        :param msg: message to write in log file
        :param kwargs:
        log_dir: directory where we want to save the log file. Default logs directory
        filename: log file name. Default log_<Y-m-d>.txt
        :return:
        """
        log_dir = self.log_dir
        if 'log_dir' in kwargs.keys():
            log_dir = kwargs['log_dir']
        if not os.path.exists(log_dir):
            self.file_handler.create_dir(log_dir)
        if 'filename' in kwargs.keys():
            filename = kwargs['filename']
        else:
            filename = self.__get_filename()

        msg = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') + '\t\t' + msg + '\r\n'
        open(log_dir + '/' + filename, 'a+').write(msg)

    def __get_filename(self):
        return 'log_' + datetime.utcnow().strftime('%Y-%m-%d') + '.txt'

    def get_working_file_location(self):
        return os.path.realpath
