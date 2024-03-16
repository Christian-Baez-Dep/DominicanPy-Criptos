import pandas as pd
import os
import matplotlib.pyplot as plt
import ExtraccionCSV
class Analizer:
    extractor = ExtraccionCSV()
    df_analisis=[]
    df_volumen_marketcap=[]
    def analize_volume_n_marketcap(self,lista):
        df_combined = self.get_dataframe()
        df_combined['Relacion Volumen Market Cap '] = df_combined['total_volume'] / df_combined['market_cap']
        df_combined_sorted = df_combined.sort_values(by='Relacion Volumen Market Cap ', ascending=False)
        analisis = pd.DataFrame(df_combined_sorted)
        lista.append(analisis)
    
    def comportamiento_volumen_capitalizacion(self,lista):
        df_combined = self.get_dataframe()
        average_volume = df_combined.groupby('coin_name')['total_volume'].mean()
        market_cap = df_combined.groupby('coin_name')['market_cap'].mean()
        volume_marketcap_ratio = average_volume / market_cap
        comportamiento = pd.DataFrame(volume_marketcap_ratio)
        lista.append(comportamiento)
        
    
    analize_volume_n_marketcap(extractor,df_analisis)
    comportamiento_volumen_capitalizacion(extractor,df_volumen_marketcap)