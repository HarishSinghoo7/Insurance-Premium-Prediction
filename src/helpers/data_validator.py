import pathlib
import pandas as pd
from src.config.logger import AppLogger


class DataValidator(AppLogger):
    """
        A class used to validate user inserted data

        ...
        Attributes
        ----------
        __FORM_DATA_VALIDATION_RULE: dict
            Key represents the feature names and value represents the data type or list of data for categorical feature

        __BULK_DATA_VALIDATION_RULE: dict
            Key represents the feature names and value represents the data type


        Methods
        -------
        form_data_validate(data: dict)
            Validate user's form data for single prediction

        bulk_data_validate(file_path: str)
            Validate file data uploaded by user
        """

    __FORM_DATA_VALIDATION_RULE = {
        'age': int,
        'sex': ['male', 'female'],
        'bmi': float,
        'children': int,
        'smoker': ['yes', 'no'],
        'region': ['southeast', 'southwest', 'northeast', 'northwest']
    }

    __BULK_DATA_VALIDATION_RULE = {
                    'age': 'int64',
                    'sex': 'object',
                    'bmi': 'float64',
                    'children': 'int64',
                    'smoker': 'object',
                    'region': 'object'
                }

    __TRAINING_DATA_VALIDATION_RULE = {
        'age': 'int64',
        'sex': 'object',
        'bmi': 'float64',
        'children': 'int64',
        'smoker': 'object',
        'region': 'object',
        'expenses': 'float64'
    }
    
    def __init__(self):
        super(DataValidator, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)

    def form_data_validate(self, data: dict):
        """Validate user's form data for single prediction
        :parameter
        -----------
        data: dict
            contains features name as key and form value as value
        """
        features = self.__FORM_DATA_VALIDATION_RULE
        if data.keys() == features.keys():
            for key, value in data.items():
                if (type(features[key]) == list and value in features[key]) or (type(data[key]) == features[key]):
                    pass
                else:
                    raise ValueError(f"ValidationError: Invalid value, expecting {features[key]} value received {type(data[key])} value")
        else:
            raise ValueError(f"ValidationError: Invalid features, expecting {features.keys()} received {data.keys()}")
        return True

    def bulk_data_validate(self, file_path: str, training_data: bool=False):
        """Validate file data uploaded by user
        :parameter
        -----------
        file_path: str
            Path of the user's uploaded file
        training_data: bool
            Default: False
            If true validate file based on __TRAINING_DATA_VALIDATION_RULE
            If False validate file based on __BULK_DATA_VALIDATION_RULE
        """
        try:
            file_extension = pathlib.Path(file_path).suffix
            if file_extension == '.csv':
                df = pd.read_csv(file_path)
            else:
                raise ValueError(
                    f"ValidationError: Invalid file expecting!")
            if training_data:
                features = self.__TRAINING_DATA_VALIDATION_RULE
            else:
                features = self.__BULK_DATA_VALIDATION_RULE
            if len(df.columns) == len(features.keys()):
                for col in df.columns:
                    if df[col].dtypes != features[col]:
                        raise ValueError(
                            f"ValidationError: Invalid value, expecting {features[col]} value received {df[col].dtypes} value")
            else:
                raise ValueError(
                    f"ValidationError: Invalid features, expecting {len(features.keys())} features received {len(df.columns)} features")
        except Exception as ex:
            raise Exception(ex)
        return True
