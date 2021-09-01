import numpy as np
import pandas as pd
from utils import get_root_dir, create_dir

class DataInterface:
    def __init__(self, model, features):
        self.features = features
        self.model = model
        self.data_dir = f'{get_root_dir()}/data/'
        self.model_dir = self.data_dir + self.model
        create_dir(self.model_dir)
        self.__reset_tmp()
    
    def __reset_tmp(self):
        self.tmp = pd.DataFrame(columns=self.features)

    def load(self):
        pass

    def save_gen(self, data):
        row = pd.Series(data, index=self.features)
        self.tmp = self.tmp.append(row, ignore_index=True)

    def save(self):
        self.tmp.to_csv(self.model_dir+'/data.csv')
        self.__reset_tmp()
    
    def print_gen(self, step):
        data = self.tmp.tail(1)
        info = str('{num:.1f}% '.format(num=step)).zfill(6)
        for feature in self.features:
            value = data[feature].item()
            if feature in ['weightsize', 'msteps']:
                number = str('{num:.4f} '.format(num=value))
            else:
                number = int(value)
            info += f'| {feature}: {number}'
        print(info)
