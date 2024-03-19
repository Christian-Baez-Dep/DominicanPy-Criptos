import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
class Filtrator:
    def __init__(self) -> None:
        pass
    
    def Get_Datos_2015(df):
        newDf = df[(df['date'] >= '2015-01-01') & (df['date'] <= '2015-12-31')]
        return newDf
    def Get_Media(df):
        dictio = {'price': df.groupby('coin_name')['price'].mean().dropna(), 'mark_cap': df.groupby('coin_name')['market_cap'].mean().dropna(), 'total_volume' : df.groupby('coin_name')['total_volume'].mean().dropna()}
        return dictio
    
    def Get_Datos_Del_1_de_2025(df):
        newDf = df[df['date'] == '2015-01-01']
        newDf.sort_values(by = 'market_cap', ascending = False, inplace = True)
        return newDf
    
    def Get_Std_Min(df):
        std_series = df.groupby('coin_name')['market_cap'].std()
        min_coin_name = std_series.sort_values().index[0]
        std_min = std_series[min_coin_name]

        return {"coin_name": min_coin_name, "std_min": std_min}
    
    def Get_Coins_Above_Mean(df):
        serie_mean = df.groupby('coin_name')['price'].mean()
        mean = serie_mean.mean()
        serie_coins_above = serie_mean[serie_mean > mean]
        return serie_coins_above