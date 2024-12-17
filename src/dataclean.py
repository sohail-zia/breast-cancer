import pandas as pd
from dataloading import Loader

PATH = r'artifacts\breast cancer.csv'
loader = Loader()
data = loader.data_loader(PATH)

class Clean:
    def __init__(self):
        pass
    def data_cleaner(self, data=data):
       data.drop('Unnamed: 32', axis = 1, inplace = True)
       data = data.drop_duplicates()
       data = data.dropna()
       data.to_csv(r'./artifacts/clean_data.csv')
       return data