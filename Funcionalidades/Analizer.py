import pandas as pd
import os
import matplotlib.pyplot as plt
from Funcionalidades.ExtrDatos import DatosCSV
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas
class Analizer:
    def __init__(self):
        self.extractor = DatosCSV()
        self.df_analisis=[]
        self.df_volumen_marketcap=[]
        
    
    def analize_volume_n_marketcap(self):
        df_combined = self.extractor.get_dataframe()
        df_combined['Relacion Volumen Market Cap '] = df_combined['total_volume'] / df_combined['market_cap']
        df_combined_sorted = df_combined.sort_values(by='Relacion Volumen Market Cap ', ascending=False)
        analisis = pd.DataFrame(df_combined_sorted)
        return analisis
    
    def comportamiento_volumen_capitalizacion(self,lista):
        df_combined = self.extractor.get_dataframe()
        average_volume = df_combined.groupby('coin_name')['total_volume'].mean()
        market_cap = df_combined.groupby('coin_name')['market_cap'].mean()
        volume_marketcap_ratio = average_volume / market_cap
        comportamiento = pd.DataFrame(volume_marketcap_ratio)
        return comportamiento
