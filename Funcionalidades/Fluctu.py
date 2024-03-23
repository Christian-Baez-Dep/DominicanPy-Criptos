import pandas as pd
import os

class Fluctuador:
    def __init__(self) -> None:
        pass


    def sacar_fluctuaciones(dfPar):
        nombres_monedas = dfPar['coin_name'].unique()
        fluctuaciones_monedas = {}
        fluctuaciones_monedas_regu = {}
        fluctuacion_mayor = ['moneda', 0]
        fluctuacion_menor = ['moneda', 0]
        for moneda in nombres_monedas:
            df = dfPar[dfPar['coin_name'] == moneda]
            
            fluctuacion_porcentual = (df['price'] - df['price'].shift(1)) / df['price'].shift(1) * 100
            fluctuacion_porcentual = fluctuacion_porcentual.round(2)
            
            fluctuacion_regular = (df['price'] - df['price'].shift(1))
            fluctuacion_regular = fluctuacion_regular.round(6)

            
            fluctuacion_porcentual = fluctuacion_porcentual.dropna()
            fluctuaciones_monedas[moneda] = fluctuacion_porcentual.values
            
            fluctuacion_regular = fluctuacion_regular.dropna()
            fluctuaciones_monedas_regu[moneda] = fluctuacion_regular.values
            
            fluctuacion_total = fluctuacion_porcentual.abs().sum()
            if fluctuacion_mayor[1] == 0:
                fluctuacion_mayor[0] = moneda
                fluctuacion_mayor[1] = fluctuacion_total
                
            if fluctuacion_total > fluctuacion_mayor[1]:
                fluctuacion_mayor[0] = moneda
                fluctuacion_mayor[1] = fluctuacion_total
                
            if fluctuacion_menor[1] == 0:
                fluctuacion_menor[0] = moneda
                fluctuacion_menor[1] = fluctuacion_total
                
            if fluctuacion_total < fluctuacion_menor[1]:
                fluctuacion_menor[0] = moneda
                fluctuacion_menor[1] = fluctuacion_total
            

        return fluctuaciones_monedas,fluctuaciones_monedas_regu,fluctuacion_mayor,fluctuacion_menor
