class Exc_By_Date:
    def __init__(self) -> None:
        pass
    
    def Get_Datos_Del_2015(df):
        newDf = df[df['date'] == '2015-01-01']
        newDf.sort_values(by = 'market_cap', ascending = False, inplace = True)
        return newDf