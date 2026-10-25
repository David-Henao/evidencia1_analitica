# hacer_resumen.py
# Este archivo agarra la tabla de datos y genera el reporte en texto limpio

import pandas as pd

class ResumidorDataset:
    def __init__(self, dataframe):
        # Aca recibimos la tabla que ya nos trajo el otro archivo
        self.df = dataframe
        
    def guardar_resumen_txt(self, nombre_archivo="resumen_dataset.txt"):
        # Abrimos o creamos el block de notas para escribir adentro
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("=== RESUMEN DEL DATASET ===\n\n")
            
            # 1. Medimos el tamaño de la tabla (filas y columnas)
            filas = self.df.shape[0]
            columnas = self.df.shape[1]
            f.write(f"Cantidad de filas: {filas}\n")
            f.write(f"Cantidad de columnas: {columnas}\n\n")
            
            # 2. Listamos los nombres de las columnas y que tipo de dato tienen
            f.write("--- Columnas y Tipos de Datos ---\n")
            for col in self.df.columns:
                tipo = self.df[col].dtype
                f.write(f"Columna: {col} | Tipo: {tipo}\n")
            f.write("\n")
            
            # 3. Contamos si faltan datos en alguna celda (valores nulos)
            f.write("--- Valores Nulos Encontrados ---\n")
            nulos = self.df.isnull().sum()
            for col, cant in nulos.items():
                f.write(f"Columna '{col}': {cant} nulos\n")
