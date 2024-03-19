import pandas as pd
import os

class AlmacenarResultados:
    def __init__(self):
        self.mejor_auge = []
        self.mejor_estabilidad = []
        self.mejoras_significativas = []

    def procesar_dataframe(self, df):
        precio_inicial = df["close"].iloc[0]
        precio_final = df["close"].iloc[-1]
        cambio = self.calcular_cambio(precio_inicial, precio_final)
        desviacion_estandar = self.calcular_desviacion_estandar(df["close"])

        self.mejor_auge.append({"nombre": df["nombre"].iloc[0], "cambio": cambio})
        self.mejor_estabilidad.append({"nombre": df["nombre"].iloc[0], "desviacion_estandar": desviacion_estandar})

        mejora_significativa = False
        if cambio > 100 or (df["market_cap"].iloc[-1] - df["market_cap"].iloc[0]) > 100000000:
            mejora_significativa = True
            descripcion = "Aumento del precio del " + str(round(cambio, 2)) + "%."
            if cambio > 100:
                descripcion = "Aumento de la capitalización de mercado en $" + str(round((df["market_cap"].iloc[-1] - df["market_cap"].iloc[0]) / 1000000, 2)) + " millones."

        if mejora_significativa:
            self.mejoras_significativas.append({"nombre": df["nombre"].iloc[0], "mejora": descripcion})

        self.mejor_auge.sort(key=lambda x: x["cambio"], reverse=True)
        self.mejor_estabilidad.sort(key=lambda x: x["desviacion_estandar"])

        return self.mejor_auge, self.mejor_estabilidad, self.mejoras_significativas

    def calcular_cambio(self, precio_inicial, precio_final):
        pass

    def calcular_desviacion_estandar(self, precios):
        pass

class ExtraccionCSV:
    
    def __init__(self, csv_directory):
        self.csv_directory = csv_directory
        
    def formateo_archivos_csv(self):
        dfs = []
        for file in os.listdir(self.csv_directory):
            if file.endswith('.csv'):
                df = pd.read_csv(os.path.join(self.csv_directory, file))
                df['nombre'] = os.path.splitext(file)[0]
                dfs.append(df)
        return pd.concat(dfs, ignore_index=True)
    
    def get_dataframe(self):
        combined_df = self.formateo_archivos_csv()
        return combined_df


# Uso de las clases

almacen = AlmacenarResultados()
extraccion = ExtraccionCSV('archive')  # Directorio donde se encuentran los archivos CSV

dataframe = extraccion.get_dataframe()
resultados = almacen.procesar_dataframe(dataframe)
print("Mejor Auge:", resultados[0])
print("Mejor Estabilidad:", resultados[1])
print("Mejoras Significativas:", resultados[2])



