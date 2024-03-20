import os
import pandas as pd
from Preprocesador import PrepocedarorDatos as ppd
from ExtrDatos import DatosCSV 

class Market:
    

    def init(self) -> None:
        pass
    
    def datos_interesantes():
        criptomonedas_interesantes = ['litecoin', 'ripple', 'bitcoin', 'ethereum']
        Exc = DatosCSV()

        datos_criptomonedas = Exc.extraer_archivos_csv()
        ppd.NormalizarFecha(datos_criptomonedas)
        ppd.CambioDeTipo(datos_criptomonedas)
        ppd.RellenarNulos(datos_criptomonedas)

        fecha_inicio = '2015-10-01'
        fecha_fin = '2015-12-31'

        df_filtrado = datos_criptomonedas[(datos_criptomonedas['date'] >= fecha_inicio) & (datos_criptomonedas['date'] <= fecha_fin)]
        df_filtrado = df_filtrado[df_filtrado['coin_name'].isin(criptomonedas_interesantes)]

        return df_filtrado
