import configparser


class ConfigReader:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('src/config/config.ini')

    def get_local_config(self):
        return self.config['LOCAL']

    def get_prod_config(self):
        return self.config['PROD']

    def get_config(self):
        """
        Description: Returning the config parameters
        :return: dictionary of config parameters
        """
        if self.config['DEFAULT']['ENV'] == 'local':
            return dict(self.get_local_config())
        else:
            return dict(self.get_prod_config())