# traer_datos.py
# Este archivo sirve para conectarse a Hugging Face y bajar la tablita de datos

from datasets import load_dataset
import pandas as pd

class CargadorHF:
    def __init__(self, dataset_id, split_name='train'):
        # Guardamos el nombre del dataset y la parte que queremos usar
        self.dataset_id = dataset_id
        self.split_name = split_name
    
    def obtener_dataframe(self):
        # Aca bajamos los datos de internet
        datos = load_dataset(self.dataset_id, split=self.split_name)
        
        # Pasamos los datos a una tabla de pandas (DataFrame) para poder usarla
        df = pd.DataFrame(datos)
        return df
