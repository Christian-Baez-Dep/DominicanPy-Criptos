import pandas as pd
import os
import matplotlib.pyplot as plt
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
    
    def analize_volume_n_marketcap(self):
        df_combined = self.get_dataframe()
        df_combined['Relacion Volumen Market Cap '] = df_combined['total_volume'] / df_combined['market_cap']
        df_combined_sorted = df_combined.sort_values(by='Relacion Volumen Market Cap ', ascending=False)

    
    def comportamiento_volumen_capitalizacion(self):
        df_combined = self.get_dataframe()
        average_volume = df_combined.groupby('coin_name')['total_volume'].mean()
        market_cap = df_combined.groupby('coin_name')['market_cap'].mean()
        volume_marketcap_ratio = average_volume / market_cap
        