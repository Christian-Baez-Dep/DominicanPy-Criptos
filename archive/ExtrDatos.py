# ●Explorar los datos que utilizará en el proyecto para determinar el formato y los datos que necesitará para revisar el comportamiento de crecimiento y/o decrecimiento en determinado tiempo. 
import pandas as pd 
import os

current_dir = os.getcwd()

csv_directory = os.path.join(current_dir, 'archive')

dfs = []
for file in os.listdir(csv_directory):
    if file.endswith('.csv'):
        df = pd.read_csv(os.path.join(csv_directory, file))
        print(f"Contenido de {file}")
        print(df.head().to_string())
        print(f"Informacion de {file}:")
        print(df.info())
        print(f"Describe del archivo {file}")
        print(df.describe())
        print("========================================================")
        print("")
        print("")
        print("")
        print("")
        dfs.append(df)
combined_df = pd.concat(dfs, ignore_index=True)




