import pandas as pd

URL = "https://datos.madrid.es/egobfiles/MANUAL/300178/activaciones_samur_2023.csv"

# Leer CSV desde la URL
data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

print(data.head())  # Mostrar las primeras filas para visualizar los datos
