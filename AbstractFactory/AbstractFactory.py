import pandas as pd
from auxiliar import convertir_a_segundos

URL = "AbstractFactory/samur.csv"

# Leer CSV desde la URL
data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

#Manipulación de datos
#Eliminamos las columnas que no nos interesan
data.drop("Codigo", axis=1, inplace=True)
data.drop("Hospital", axis=1, inplace=True)

#Cambiamos los tipos de datos a otros más adecuados
mes_a_numero = {
    "ENERO": 1,
    "FEBRERO": 2,
    "MARZO": 3,
    "ABRIL": 4,
    "MAYO": 5,
    "JUNIO": 6,
    "JULIO": 7,
    "AGOSTO": 8,
    "SEPTIEMBRE": 9,
    "OCTUBRE": 10,
    "NOVIEMBRE": 11,
    "DICIEMBRE": 12
}

data["Mes"] = data["Mes"].replace(mes_a_numero)

data["Hora Solicitud"] = data["Hora Solicitud"].apply(convertir_a_segundos)
data["Hora Intervencion"] = data["Hora Intervencion"].apply(convertir_a_segundos)

print(data.head())


