import matplotlib.pyplot as plt


class Monedas_Ultimotrismetre:
    def __init__(self) -> None:
        pass
    
    def MostrarMenu(df):
        criptomonedas_interesantes = ['litecoin', 'ripple', 'bitcoin', 'ethereum']
        litecoin = df[df['coin_name'] == criptomonedas_interesantes[0]]
        ripple = df[df['coin_name'] == criptomonedas_interesantes[1]]
        bitcoin = df[df['coin_name'] == criptomonedas_interesantes[2]]
        ethereum = df[df['coin_name'] == criptomonedas_interesantes[3]]
        
        # Graficar el precio de cada criptomoneda en un mismo plot
        plt.figure(figsize=(10, 6))
        plt.plot(litecoin['date'], litecoin['market_cap'], marker='o', linestyle='-', label='Litecoin')
        plt.plot(ripple['date'], ripple['market_cap'], marker='o', linestyle='-', label='Ripple')
        plt.plot(bitcoin['date'], bitcoin['market_cap'], marker='o', linestyle='-', label='Bitcoin')
        plt.plot(ethereum['date'], ethereum['market_cap'], marker='o', linestyle='-', label='Ethereum')
        plt.xlabel('Fecha')
        plt.ylabel('Precio')
        plt.title('Precio de Criptomonedas Interesantes en función de la fecha')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Mostrar la gráfica
        plt.show()
