from Funcionalidades.Filtrador import Filtrator as fl
import matplotlib.pyplot as plt

class Menu_Mean():
    def __init__(self) -> None:
        pass
    
    def MostrarMenu(df):
        mean_datos = fl.Get_Media(df)
        cmap = plt.get_cmap('viridis')  

        colores = [cmap(i / len(mean_datos['price'].index)) for i in range(len(mean_datos['price'].index))]
        
        fig, axs = plt.subplots(2,figsize=(15, 9))  
        bar_width = 0.75  # Ancho de las barras

        axs[0].bar(mean_datos['price'].index,mean_datos['price'].values, color = colores[0], width = bar_width)  # Histograma para 'price'
        axs[0].set_title("Diagrama de precios")
        axs[0].set_xticks(mean_datos['price'].index)  # Establecer los ticks del eje x
        axs[0].set_xticklabels(mean_datos['price'].index, rotation=45, ha='right', fontsize=7)  # Rotación de los ticks del eje x
        axs[0].set_ylim(0, 1000)  # Por ejemplo, límites de 0 a 500
        axs[0].set_xlim(left=-0.9)  # Ajuste de límites en el eje x

        axs[1].bar(mean_datos['market_cap'].index,mean_datos['market_cap'].values, color = colores[1], width = bar_width)  # Histograma para 'market_cap'
        axs[1].set_title("Diagrama de capitalización de mercado")
        axs[1].set_xticks(mean_datos['market_cap'].index)  # Establecer los ticks del eje x
        axs[1].set_xticklabels(mean_datos['market_cap'].index, rotation=45, ha='right', fontsize= 7 ) # Rotación de los ticks del eje x
        axs[1].set_ylim(0, 27500000000)  # Por ejemplo, límites de 0 a 500
        axs[1].set_xlim(left=-0.9)  # Ajuste de límites en el eje x

        
        plt.ylabel('Medias')
        plt.xlabel('Monedas')
        fig.subplots_adjust(hspace=0.7)  # Espaciado vertical

        plt.show()
