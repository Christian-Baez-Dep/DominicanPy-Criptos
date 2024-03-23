import matplotlib.pyplot as plt
import pandas as pd

class Grafica_Dispersion:
    def __init__(self) -> None:
        pass
    def MostrarGraficoDispersion(dfPar):
        nombres_monedas = dfPar['coin_name'].unique()
        df = pd.DataFrame()
        for moneda in nombres_monedas:
            df[moneda] = dfPar[dfPar['coin_name'] == moneda]['price'].reset_index(drop=True)

        # Crear el gráfico de dispersión
        plt.figure(figsize=(10, 6))
        for columna in df.columns:
            plt.scatter(df.index, df[columna], label=columna)

        plt.xlabel('Índice')
        plt.ylabel('Precio')
        plt.title('Gráfico de Dispersión de Precios por Moneda')
        plt.legend()
        plt.grid(True)
        plt.show()
