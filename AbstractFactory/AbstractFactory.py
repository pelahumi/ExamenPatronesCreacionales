from __future__ import annotations
from abc import ABC, abstractmethod
from auxiliar import *

#Abstract Factory para las operaciones de estadística
class AbstractFactory(ABC):
    """
    La clase AbstractFactory declara un conjunto de métodos que devuelven
    """

    @abstractmethod
    def crear_moda(self) -> AbstractAnalisis:
        pass

    @abstractmethod
    def crear_media(self) -> AbstractAnalisis:
        pass

    @abstractmethod
    def crear_mediana(self) -> AbstractAnalisis:
        pass

#Definimos la Factoria concreta para las operaciones de estadística

class AnalisisFactory(AbstractFactory):

    def crear_moda(self):
        return Moda()
    
    def crear_media(self):
        return Media()

    def crear_mediana(self):
        return Mediana()


#Definimos la clase abstracta del producto
class AbstractAnalisis(ABC):

    @abstractmethod
    def calcular(self) -> int:
        pass

#Definimos las clases concretas para cada producto
class Moda(AbstractAnalisis):

    def calcular(self, data, col):
        return data[col].mode()[0]

class Media(AbstractAnalisis):
    
    def calcular(self, data, col):
        return data[col].mean()

class Mediana(AbstractAnalisis):
        
    def calcular(self, data, col):
        return data[col].median()
























def launcher(factory: AbstractFactory):
    moda = factory.crear_moda()
    media = factory.crear_media()
    mediana = factory.crear_mediana()

    col = str(input("Introduce la columna sobre la que quieres realizar el análisis: "))

    calculo_moda = moda.calcular(data,col) 
    calculo_mediana = mediana.calcular(data,col)
    calculo_media = media.calcular(data,col)
    

    if comprobador(data,col) == True:
        calculo_moda = invertir(calculo_moda)
        calculo_mediana = invertir(calculo_mediana)
        calculo_media = invertir(calculo_media)

    else:
        pass

    print("La moda de la columna", col, "es:", calculo_moda)
    print("\n")
    print("La media de la columna", col, "es:", calculo_media)
    print("\n")
    print("La mediana de la columna", col, "es:", calculo_mediana)


if __name__ == "__main__":
    launcher(AnalisisFactory())












    

        


