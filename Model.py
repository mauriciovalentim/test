import numpy as np
from pathlib import Path
import pickle
import pandas as pd


def getMaxValues():
    max_values = pd.read_pickle('max_values.pkl')
    max_dqo = max_values['DQO_SAIDA']
    max_values = max_values.drop('DQO_SAIDA')
    return max_values.to_dict(), max_dqo


def formatData(info, maxValues):
    res = [{key: info[key] / maxValues[key] for key in maxValues}]
    return res


maxValues, maxDQOSaida = getMaxValues()
import os

file_path = 'saved_regressor.pkl'

if not os.path.exists(file_path):
    raise FileNotFoundError(f'O arquivo {file_path} não foi encontrado.')
else:
    loaded_model, data, scaler = pickle.load(open(file_path, 'rb'))

choosen_cols = [
    # 'HORA',
    'TEMPERATURA_ENTRADA',
    'PH_ENTRADA',
    'SSD_ENTRADA',
    'SST_ENTRADA',
    'ST_ENTRADA',
    'DQO_ENTRADA',
    # 'DQO_EFICIENCIA',
    'DBO_ENTRADA',
    # 'DBO_EFICIENCIA',
    'OG_ENTRADA',
]


def getSaidaDBO(temperatura, ph, ssd, sst, st, dqo, dbo, og):
    # Criar DataFrame a partir dos parâmetros
    info = {
        'TEMPERATURA_ENTRADA': temperatura,
        'PH_ENTRADA': ph,
        'SSD_ENTRADA': ssd,
        'SST_ENTRADA': sst,
        'ST_ENTRADA': st,
        'DQO_ENTRADA': dqo,
        'DBO_ENTRADA': dbo,
        'OG_ENTRADA': og
    }

    data = pd.DataFrame([info])

    # Selecionar colunas de interesse
    choosen_cols = [
        'TEMPERATURA_ENTRADA',
        'PH_ENTRADA',
        'SSD_ENTRADA',
        'SST_ENTRADA',
        'ST_ENTRADA',
        'DQO_ENTRADA',
        'DBO_ENTRADA',
        'OG_ENTRADA'
    ]
    scaledData = data[choosen_cols].copy()
    scaledData[choosen_cols] = scaler.transform(data[choosen_cols])

    # Fazer previsão usando o modelo existente
    saidaDBO_normalizado = loaded_model.predict(scaledData)

    des = pd.DataFrame(saidaDBO_normalizado)

    print(scaler.inverse_transform([des] ))

    return 1




# teste = getSaidaDBO(19, 4, 0.15, 0.15, 0.35, 1542.45, 325, 0.15) 

# TEMPERATURA_ENTRADA: 18.90 / 38.4
# PH_ENTRADA: 3.26 / 26.2
# SSD_ENTRADA: 0.10 / 4513.0
# SST_ENTRADA: 0.10 / 339030.0
# ST_ENTRADA: 0.30 / 289636.0
# DQO_ENTRADA: 1542.38 / 451003.8
# DQO_SAIDA: 1.00 / 15.0
# DBO_ENTRADA: 320.00 / 159998.4
# OG_ENTRADA: 0.10 / 150875.0
