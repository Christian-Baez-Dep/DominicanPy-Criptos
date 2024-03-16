import pandas as pd
import os

class ExtraccionCSV:
    
    def __init__(self):
        self.current_dir = os.getcwd()
        self.csv_directory = os.path.join(self.current_dir, 'archive')
        self.dfs = []
        
        
    def formateo_archivos_csv(self):
        for file in os.listdir(self.csv_directory):
            if file.endswith('.csv'):
                df = pd.read_csv(os.path.join(self.csv_directory, file))
                print(f"Contenido e información de {file}:")
                print(df.head().to_string())
                print(df.info())
                print(df.describe())
                print("========================================================")
                self.dfs.append(df)
    
    def get_dataframe(self):
        self.formateo_archivos_csv()
        combine_df = pd.concat(self.dfs, ignore_index=True)
        return combine_df
    

extraccion = ExtraccionCSV()

combine_df = extraccion.get_dataframe()

print(combine_df.head())
