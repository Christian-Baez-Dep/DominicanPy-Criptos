import matplotlib.pyplot as plt

class Grafica_Precios:
    def __init__(self) -> None:
        pass
    
    def MostrarGrafica(df):
        nombres_unicos = df['coin_name'].unique()

        for moneda in nombres_unicos:
            dfMoneda = df[df['coin_name']==moneda]
            
            plt.plot(dfMoneda['date'], dfMoneda['price'], label=moneda)



        plt.xlabel('Fecha')
        plt.ylabel('Precio')
        plt.title('Precio de Criptomonedas en función de la fecha')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()