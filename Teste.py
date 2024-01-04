import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# DataFrame original
data = {'Feature1': [4, 5, 6, 7, 8, 9]}
df = pd.DataFrame(data)

# Inicializar o MinMaxScaler
scaler = MinMaxScaler()

# Ajustar o scaler aos dados e transformar as colunas especificadas
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Exibir DataFrame original e normalizado
print("DataFrame Original:")
print(df)

print("\nDataFrame Normalizado:")
print(df_scaled)

# Agora, tentar transformar o valor 3
valor_transformado = scaler.transform([[3.9]])
print("\nValor Transformado (3):", valor_transformado)
