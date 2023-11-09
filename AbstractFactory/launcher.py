import pandas as pd
from abstractFactory import AbstractFactory
from auxiliar import convertir_a_segundos, comprobador, invertir

def launcher(factory: AbstractFactory):

    data = pd.read_csv("AbstractFactory/DataBase/samur_limpio.csv", sep = ";",  encoding = "UTF-8")

    data["Hora Solicitud"] = data["Hora Solicitud"].apply(convertir_a_segundos)
    data["Hora Intervencion"] = data["Hora Intervencion"].apply(convertir_a_segundos)

    analisis = factory.crear_analisis()
    grafico = factory.crear_grafico()

    col = input("Introduzca el nombre de la columna a analizar: ")

    if comprobador(data, col) == True:
        print("El resultado del análisis es: ", invertir(analisis.calcular(data, col)))
    else: 
        print("El resultado del análisis es: ", analisis.calcular(data, col))

    grafico.dibujar(data, col)

    