import matplotlib.pyplot as plt
import pandas as pd

class Grafica_Calor:
    def __init__(self) -> None:
        pass
    
    def MostrarGrafica(dfPar):
        nombres_monedas = dfPar['coin_name'].unique()
        df = pd.DataFrame()
        for moneda in nombres_monedas:
            df[moneda] = dfPar[dfPar['coin_name'] == moneda]['price'].reset_index(drop=True)
            
        df_corr = df.corr()

        plt.imshow(df_corr, cmap='hot', interpolation='none')
        plt.colorbar()  # Barra de color para la correlación
        plt.xticks(range(len(df_corr)), df_corr.columns, rotation=90)  # Definir los ticks del eje x con los nombres de las columnas
        plt.yticks(range(len(df_corr)), df_corr.columns)  # Definir los ticks del eje y con los nombres de las columnas
        plt.gcf().set_size_inches(15, 9)

        # Ajustar el espacio entre los xticks
        plt.subplots_adjust(bottom=0.19)
        
                # Separar los xticks
        plt.xticks(range(len(df_corr)), df_corr.columns)
        plt.tick_params(axis='x', which='major', pad=15)  # Ajustar el espaciado entre los xticks


        plt.show()