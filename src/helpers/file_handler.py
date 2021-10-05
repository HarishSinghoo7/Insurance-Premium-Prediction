import os
import pathlib
import pickle
from werkzeug.utils import secure_filename

from src.config.config import ConfigReader


class FileHandler:

    ALLOWED_EXTENSIONS = {'csv'}

    def __init__(self):
        self.conf = ConfigReader()

    def create_dir(self, dir_path):
        dir_path = dir_path.replace("//", "/")
        dir_path = dir_path.replace("\\", "/")
        path = ''
        for dir in dir_path.split('/'):
            path += dir + '/'
            if not os.path.exists(path):
                os.mkdir(path)
        return path

    def get_cwd(self):
        return os.path.abspath(os.getcwd())

    def allowed_file(self, filename):
        return pathlib.Path(filename).suffix in self.ALLOWED_EXTENSIONS

    def save_file(self, file):
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = self.conf.config['DEFAULT']['UPLOAD_FOLDER']
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)
            return file_path
        else:
            raise ValueError(f"InvalidFile: Invalid file type {pathlib.Path(file.filename).suffix}!")

    def save_pickle(self, class_object, object_name):
        object_folder = self.conf.config['DEFAULT']['OBJECT_FOLDER']
        pickle.dump(class_object, open(os.path.join(object_folder, object_name), 'wb'))
        return True

    def load_pickle(self, object_name):
        object_folder = self.conf.config['DEFAULT']['OBJECT_FOLDER']
        return pickle.load(os.path.join(object_folder, object_name))

