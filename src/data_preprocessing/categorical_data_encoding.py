from src.config.logger import AppLogger
from src.helpers.file_handler import FileHandler

import pandas as pd
import category_encoders as ce


class CategoricalDataEncoder(AppLogger):

    encoder_cols = ['sex', 'smoker', 'region']
    
    def __init__(self, dataset: pd.DataFrame(), train = False):
        super(CategoricalDataEncoder, self).__init__()
        self.cur_file_path = self.get_working_file_location()(__file__)
        self.dataset = dataset
        self.train = train

    def one_hot_encoder(self):
        self.log(f"{self.cur_file_path}\t\tInfo: Performing one hot encoder in {self.encoder_cols} features!")
        file_handler = FileHandler()
        if self.train:
            encoder = file_handler.load_pickle('category_encoder.pkl')
        else:
            encoder = ce.OneHotEncoder(cols=self.encoder_cols, return_df=True)
            encoder.fit(self.dataset)
            file_handler.save_pickle(encoder, 'category_encoder.pkl')

        encoded_df = encoder.transform(self.dataset)
        return encoded_df.drop(['sex_1', 'smoker_1', 'region_1'])