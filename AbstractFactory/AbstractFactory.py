from __future__ import annotations
from abc import ABC, abstractmethod
from auxiliar import *
import matplotlib.pyplot as plt

#Abstract Factory para las operaciones de estadística
class AbstractFactory(ABC):
    """
    La clase AbstractFactory declara un conjunto de métodos que devuelven
    """

    @abstractmethod
    def crear_analisis(self) -> AbstractAnalisis:
        pass

    @abstractmethod
    def crear_grafico(self) -> AbstractGrafico:
        pass

#Definimos la Factoria concreta para las operaciones de estadística

class HistModeFactory(AbstractFactory):

    """
    La clase ConcreteFactory que implementa los métodos de la clase AbstractFactory
    """

    def crear_analisis(self) -> AbstractAnalisis:
        return Moda()

    def crear_grafico(self) -> AbstractGrafico:
        return Histograma()
    
class HistMeanFactory(AbstractFactory):

    """
    La clase ConcreteFactory que implementa los métodos de la clase AbstractFactory
    """

    def crear_analisis(self) -> AbstractAnalisis:
        return Media()

    def crear_grafico(self) -> AbstractGrafico:
        return Histograma()

class HistMedianFactory(AbstractFactory):

    """
    La clase ConcreteFactory que implementa los métodos de la clase AbstractFactory
    """
    
    def crear_analisis(self) -> AbstractAnalisis:
        return Mediana()
    
    def crear_grafico(self) -> AbstractGrafico:
        return Histograma()

class BarModeFactory(AbstractFactory):

    """
    La clase ConcreteFactory que implementa los métodos de la clase AbstractFactory
    """

    def crear_analisis(self) -> AbstractAnalisis:
        return Moda()

    def crear_grafico(self) -> AbstractGrafico:
        return Barra()

class BarMeanFactory(AbstractFactory):

    """
    La clase ConcreteFactory que implementa los métodos de la clase AbstractFactory
    """

    def crear_analisis(self) -> AbstractAnalisis:
        return Media()

    def crear_grafico(self) -> AbstractGrafico:
        return Barra()

class BarMedianFactory(AbstractFactory):

    """
    La clase ConcreteFactory que implementa los métodos de la clase AbstractFactory
    """
        
    def crear_analisis(self) -> AbstractAnalisis:
        return Mediana()
        
    def crear_grafico(self) -> AbstractGrafico:
        return Barra()


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
    

#Definimos la clase abstracta del producto
class AbstractGrafico(ABC):

    @abstractmethod
    def dibujar(self) -> int:
        pass

#Definimos las clases concretas para cada producto
class Histograma(AbstractGrafico):

    def dibujar(self, data, col):
        plt.hist(data[col], bins=20)
        plt.savefig("AbstractFactory/img/histograma.png")

class Barra(AbstractGrafico):
        
    def dibujar(self, data, col):
        plt.bar(data[col].unique(), data[col].value_counts())
        plt.xticks(data[col].unique(), rotation = 90)
        plt.savefig("AbstractFactory/img/barra.png")













    

        


