import matplotlib.pyplot as plt

class Grafica_Fluctuaciones:
    def __init__(self) -> None:
        pass
    
    def MostrarGrafica(df,fluctuaciones):

        for moneda, fluctuacion in fluctuaciones.items(): 
            num_registros = len(df[df['coin_name'] == moneda]) - 1
            plt.plot(df[df['coin_name'] == moneda]['date'].tail(num_registros), fluctuacion, label=moneda)



        plt.xlabel('Fecha')
        plt.ylabel('Fluctuaciones')
        plt.title('Fluctuaciobes de las monedas en 2015')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()