import os
import pandas as pd

# Ruta al directorio que contiene los archivos CSV de las criptomonedas
ruta_archivos = "C:/Users/franc/Desktop/Project/archive"

# Lista de los nombres de los archivos CSV de las criptomonedas
criptomonedas_interesantes = ['litecoin.csv', 'ripple.csv', 'bitcoin.csv', 'ethereum.csv']

# Crear un diccionario para almacenar los DataFrames de las criptomonedas
datos_criptomonedas = {}

# Cargar los datos de cada criptomoneda en un DataFrame y almacenarlos en el diccionario
for criptomoneda in criptomonedas_interesantes:
    nombre_criptomoneda = criptomoneda.split('.')[0]  # Obtener el nombre de la criptomoneda
    ruta_completa = os.path.join(ruta_archivos, criptomoneda)
    datos_criptomonedas[nombre_criptomoneda] = pd.read_csv(ruta_completa)

# Convertir la columna de fecha a tipo datetime en cada DataFrame
for df_criptomoneda in datos_criptomonedas.values():
    df_criptomoneda['date'] = pd.to_datetime(df_criptomoneda['date'])

    fecha_inicio = '2015-10-01'
    fecha_fin = '2015-12-31'

# Calcular el valor total del mercado para cada criptomoneda durante los últimos tres meses de 2015
valor_mercado_ultimos_tres_meses = {}
for nombre_criptomoneda, df_criptomoneda in datos_criptomonedas.items():
    df_filtrado = df_criptomoneda[(df_criptomoneda['date'] >= fecha_inicio) & (df_criptomoneda['date'] <= fecha_fin)]
    valor_total_mercado = df_filtrado['market_cap'].sum()
    valor_mercado_ultimos_tres_meses[nombre_criptomoneda] = valor_total_mercado

criptomonedas_mayor_valor = sorted(valor_mercado_ultimos_tres_meses.items(), key=lambda x: x[1], reverse=True)
print("Criptomonedas con mayor valor en el mercado durante los últimos tres meses de 2015:")
for criptomoneda, valor_mercado in criptomonedas_mayor_valor:
    print(f"{criptomoneda}: {valor_mercado}")
