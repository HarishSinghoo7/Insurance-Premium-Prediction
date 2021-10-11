import pandas as pd

from src.controller import Controller
from src.helpers.data_validator import DataValidator
from src.helpers.file_handler import FileHandler


class PredictionController(Controller):
    """
    A class used to control Insurance Premium Prediction Requests

    ...
    Attributes
    ----------
    None

    Methods
    -------
    single_data_prediction(data)
        Handle single prediction request came by filling HTML form

    bulk_data_prediction(file)
        Handle bulk prediction request when user upload a file
    """
    def __init__(self):
        super(PredictionController, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)
        
    def single_data_prediction(self, data):
        """Handle single prediction request came by filling HTML form
        :parameter
        -----------
        data: request.form data
            independent variables value for prediction
        """
        self.log(f"{self.cur_file_path}\t\tInfo: single_data_prediction method invoked!")
        resp = {}
        try:
            resp['predictions'] = {
                'age': int(data.get('age')),
                'sex': data.get('sex'),
                'bmi': float(data.get('bmi')),
                'children': int(data.get('children')),
                'smoker': data.get('smoker'),
                'region': data.get('region'),
            }
            self.log(f"{self.cur_file_path}\t\tInfo: Validating Data!")
            self.log(f"{self.cur_file_path}\t\tData: {str(resp['predictions'])}")
            if DataValidator().form_data_validate(resp['predictions']):
                pass
                # resp['predictions']['premium'] = self.__start_prediction
        except Exception as ex:
            self.log(f"{self.cur_file_path}\t\tError: {str(ex)}")
            resp['outputError'] = str(ex)
        finally:
            return resp
    
    def bulk_data_prediction(self, input_file):
        """Handle bulk data prediction (file uploaded by user)
        :parameter
        -----------
        input_file: request.file data
            User uploaded file
        """
        self.log(f"{self.cur_file_path}\t\tInfo: bulk_data_prediction method invoked!")
        resp = {}
        try:
            self.log(f"{self.cur_file_path}\t\tInfo: Uploading user uploaded file!")
            # upload file
            file = input_file.get('file')
            file_path = FileHandler().save_file(file)
            self.log(f"{self.cur_file_path}\t\tInfo: File uploaded at {file_path}")
            self.log(f"{self.cur_file_path}\t\tInfo: Validating Data!")
            if DataValidator().bulk_data_validate(file_path):
                pass
                # resp['predictions']['premium'] = self.__start_prediction
        except Exception as ex:
            self.log(f"{self.cur_file_path}\t\tError: {str(ex)}")
            resp['outputError'] = str(ex)
        finally:
            return resp

    def __start_prediction(self, df: pd.DataFrame()):
        """Handle premium prediction process
        :parameter
        -----------
        df: pandas DataFrame object
        """

        self.log(f"{self.cur_file_path}\t\tInfo: __start_prediction method invoked!")
        # Data Preprocessing

        # Loading best fitted data

        # Predicting premium
        pass