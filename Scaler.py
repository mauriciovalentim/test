# import os
# from pathlib import Path
# import pickle

# file_path = './saved_regressor.pkl'

# if not os.path.exists(file_path):
#     raise FileNotFoundError(f'O arquivo {file_path} não foi encontrado.')
# else:
#     loaded_model, data, scaler = pickle.load(open(file_path, 'rb'))

# print(data)

import pandas as pd

class Scaler:
    def __init__(self):
        self.max_values, self.max_dqo = self._get_max_values()

    def create_dataframe(self, data):
        info = {
            'TEMPERATURA_ENTRADA': data[0],
            'PH_ENTRADA': data[1],
            'SSD_ENTRADA': data[2],
            'SST_ENTRADA': data[3],
            'ST_ENTRADA': data[4],
            'DQO_ENTRADA': data[5],
            'DBO_ENTRADA': data[6],
            'OG_ENTRADA': data[7]}
        dataframe = pd.DataFrame([info])
        return dataframe

    def normalize(self, data):
        return data.div(self.max_values)

    def desnormalize(self, dqo):
        return dqo*self.max_dqo

    def _get_max_values(self):
        max_values = pd.read_pickle('max_values.pkl')
        max_dqo = max_values['DQO_SAIDA']
        max_values = max_values.drop('DQO_SAIDA')
        return max_values, max_dqo
    

# a = Scaler()
# info = {
#         'TEMPERATURA_ENTRADA': a.max_values['TEMPERATURA_ENTRADA'],
#         'PH_ENTRADA': a.max_values['PH_ENTRADA'],
#         'SSD_ENTRADA': a.max_values['SSD_ENTRADA'],
#         'SST_ENTRADA': a.max_values['SST_ENTRADA'],
#         'ST_ENTRADA': a.max_values['ST_ENTRADA'],
#         'DQO_ENTRADA': a.max_values['DQO_ENTRADA'],
#         'DBO_ENTRADA': a.max_values['DBO_ENTRADA'],
#         'OG_ENTRADA': a.max_values['OG_ENTRADA']
#     }

# data = pd.DataFrame([info])
# print(a.normalize(data))