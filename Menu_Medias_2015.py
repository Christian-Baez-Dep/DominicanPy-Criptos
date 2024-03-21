from Funcionalidades.Filtrador import Filtrator as fl
import matplotlib.pyplot as plt

class Menu_Mean_2015:
    def __init__(self) -> None:
        pass
    
    def MostrarMenu(datos_2015):
        mean_datos = fl.Get_Media(datos_2015)
        
        cmap = plt.get_cmap('viridis')  

        colores = [cmap(i / len(mean_datos['price'].index)) for i in range(len(mean_datos['price'].index))]
        
        fig, axs = plt.subplots(2,figsize=(13, 8))  
        
        axs[0].bar(mean_datos['price'].index,mean_datos['price'].values, color = colores[0])  # Histograma para 'price'
        axs[0].set_title("Histograma de precios")
        axs[0].set_ylim(0, 300)  # Por ejemplo, límites de 0 a 500

        axs[1].bar(mean_datos['market_cap'].index,mean_datos['market_cap'].values, color = colores[1])  # Histograma para 'market_cap'
        axs[1].set_title("Histograma de capitalización de mercado")
        axs[1].set_ylim(0, 1000000000)  # Por ejemplo, límites de 0 a 500

        
        
        plt.ylabel('Medias')
        plt.xlabel('Monedas')
        fig.subplots_adjust(hspace=0.3)  # Espaciado vertical

        plt.show()

        