import pickle
from Scaler import Scaler
import os

# file_path = './saved_regressor.pkl'

# if not os.path.exists(file_path):
#     raise FileNotFoundError(f'O arquivo {file_path} não foi encontrado.')
# else:
#     with open(file_path, 'rb') as file:
#         loaded_model, _, scaler_pickle = pickle.load(file)

scaler_instance = Scaler()

def get_saida_dbo(*info):
    print("-"*50)
    # Criar DataFrame a partir dos parâmetros
    original_data = scaler_instance.create_dataframe(info)
    print(original_data.head())
    # Normalizando dataframe
    normalized_data = scaler_instance.normalize(original_data)
    print(normalized_data)
    # Obtendo saída normalizada
    # normalized_dbo = loaded_model.predict(normalized_data)[0]
    normalized_dbo = 4
    print(normalized_dbo)
    # Desnormalizando saída
    desnormalized_dbo = scaler_instance.desnormalize(normalized_dbo)
    print(desnormalized_dbo)
    # Retornando resultado (DBO SAÍDA DESNORMALIZADA)
    print("-"*50)
    return desnormalized_dbo
