import pandas as pd

#Leemos el csv
data = pd.read_csv("AbstractFactory/samur.csv", sep=';', encoding='UTF-8')

#Visualizamos los datos del csv
#print(data.head())

#Visualizamos los tipos de datos
#print(data.dtypes)

#Vemos si hay valores nulos
#print(data.isnull().sum())

#Como el csv tiene 112776 filas -> print(data.shape[0]), y en la columna "Hospital" hay más de 70000 valores nulos, reemplazamos esos valores nulos por "No hospitalizado"
data["Hospital"] = data["Hospital"].fillna("No hospitalizado")

#Siguen quedando valores nulos, pero estos al no ser muy representativos en comparación a los datos totales, los podemos eliminar
data = data.dropna()

#Comprobamos que ya no hay valores nulos
#print(data.isnull().sum())

#Además, podemos eliminar la columna "Año", ya que todos los accidentes fueron en 2023, lo que hace a la columna irrelevante
print(data.head())
data.drop("Año", axis=1, inplace=True)

#En la columna mes la cambiamos por números para manejarla mejor
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

#Creamos un nuevo csv con los datos ya filtrados y limpios
data.to_csv("AbstractFactory/samur_limpio.csv", sep=';', encoding='UTF-8', index=False)








