import os
import pandas as pd

class DatosCSV:
    
    def __init__(self):
        self.current_dir = os.getcwd()
        self.csv_directory = os.path.join(self.current_dir, 'archive')
        self.dfs = []
        
        
    def extraer_archivos_csv(self):
        for file in os.listdir(self.csv_directory):
            if file.endswith('.csv'):
                df = pd.read_csv(os.path.join(self.csv_directory, file))
                self.dfs.append(df)
        combine_df = pd.concat(self.dfs, ignore_index=True)
        return combine_df
        
    def formateo_datos(self, dfs):
        formatear_data = []
        for df in dfs:
            formatear_data.append({
                'nombre_archivo': df,
                'contenido': df.head().to_string(),
                'informacion': df.info(),
                'descripcion': df.describe()
            })
        return formatear_data


datos_csv = DatosCSV()


datos_combinados = datos_csv.extraer_archivos_csv()

datos_formateados = datos_csv.formateo_datos(datos_csv.dfs)


for dato in datos_formateados:
    print(dato)

