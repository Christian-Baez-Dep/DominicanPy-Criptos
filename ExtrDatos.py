import os
import pandas as pd

class DatosCSV:
    
    def __init__(self):
        self.current_dir = os.getcwd()
        self.csv_directory = os.path.join(self.current_dir, 'archive')
        self.dfs = []
        
        
    def extra_archivos_csv(self):
        for file in os.listdir(self.csv_directory):
            if file.endswith('.csv'):
                df = pd.read_csv(os.path.join(self.csv_directory, file))
                self.dfs.append(df)
        return self.dfs
        
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

    def get_dataframe(self):
        self.extra_archivos_csv()
        combine_df = pd.concat(self.dfs, ignore_index=True)
        return combine_df