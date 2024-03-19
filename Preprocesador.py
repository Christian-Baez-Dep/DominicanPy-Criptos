import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
class PrepocedarorDatos:
    def __init__(self) -> None:
        pass
    
    def NormalizarFecha(df):    
        df['date'] = df['date'].str.slice(stop=10)

    def RellenarNulos(df):

        df['market_cap_shift'] = df['market_cap'].shift(1)
        df['price_shift'] = df['price'].shift(1)

        df['new_market_cap'] = (df['market_cap_shift'] / df['price_shift']) * df['price']

        df['market_cap'] = df['market_cap'].fillna(df['new_market_cap'])

        df.drop(['market_cap_shift', 'price_shift', 'new_market_cap'], axis=1, inplace=True)
    
    def CambioDeTipo(df):
        df['date'] = df['date'].astype('datetime64[ns]')
        df['coin_name'] = df['coin_name'].astype('category')
        
        


