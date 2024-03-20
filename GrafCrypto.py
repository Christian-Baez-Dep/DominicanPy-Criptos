import pandas as pd
import matplotlib.pyplot as plt
import os
from ExtrDatos import DatosCSV as dc
from Filtrador import Filtrator as flc
from Preprocesador import PrepocedarorDatos as ppd


class GraficadorCrypto:
    
    def init(self) -> None:
        pass
    
    def Graficar_2015(df):
        criptomonedas = ['litecoin', 'ripple', 'bitcoin', 'ethereum']

        fig, axs = plt.subplots(len(criptomonedas), figsize=(10, 8), sharex=True)

        index = 0
        ppd.NormalizarFecha(df)
        ppd.RellenarNulos(df)
        ppd.CambioDeTipo(df)
        df_2015 = flc.Get_Datos_2015(df)

        for moneda  in (criptomonedas):
        
        
        
            df_moneda = df_2015[df_2015['coin_name']== moneda]
            print(df_moneda.to_string())
            
            axs[index].plot(df_moneda['date'], df_moneda['price'])
            axs[index].set_title(moneda)  
            axs[index].set_ylabel('Precio')
            axs[-1].set_xlabel('Fecha')
            index+=1
            
        plt.tight_layout()
        plt.show()
