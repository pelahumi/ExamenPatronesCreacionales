from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

#Creamos las interfaces de cada tipo de producto que serán implementadas por las clases concretas de cada producto.

class Masa(ABC):
    """
    La interfaz Masa declara operaciones para todos los tipos de objetos Masa.
    """

    @abstractmethod
    def tipo_masa(self) -> str:
        pass

class MasaFina(Masa):
    """
    Las clases concretas de Masa implementan la interfaz Masa.
    """

    def tipo_masa(self) -> str:
        return "Masa Fina"

class MasaGruesa(Masa):
    """
    Las clases concretas de Masa implementan la interfaz Masa.
    """

    def tipo_masa(self) -> str:
        return "Masa Gruesa"

class MasaFermentada(Masa):
    """
    Las clases concretas de Masa implementan la interfaz Masa.
    """

    def tipo_masa(self) -> str:
        return "Masa Fermentada"

class Base(ABC):
    """
    La interfaz Base declara operaciones para todos los tipos de objetos Base.
    """

    @abstractmethod
    def tipo_base(self) -> str:
        pass

class Ingredientes(ABC):
    """
    La interfaz Ingredientes declara operaciones para todos los tipos de objetos Ingredientes.
    """

    @abstractmethod
    def tipo_ingredientes(self) -> str:
        pass

class Coccion(ABC):
    """
    La interfaz Coccion declara operaciones para todos los tipos de objetos Coccion.
    """

    @abstractmethod
    def tipo_coccion(self) -> str:
        pass

class Presentacion(ABC):
    """
    La interfaz Presentacion declara operaciones para todos los tipos de objetos Presentacion.
    """

    @abstractmethod
    def tipo_presentacion(self) -> str:
        pass

class Maridajes(ABC):
    """
    La interfaz Maridajes declara operaciones para todos los tipos de objetos Maridajes.
    """

    @abstractmethod
    def tipo_maridajes(self) -> str:
        pass

class Extras(ABC):
    """
    La interfaz Extras declara operaciones para todos los tipos de objetos Extras.
    """

    @abstractmethod
    def tipo_extras(self) -> str:
        pass


class Builder(ABC):

    """
    La interfaz Builder especifica métodos para crear las diferentes partes de los objetos Producto Pizza.
    """

    @property
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def masa(self) -> None:
        pass

    @abstractmethod
    def base(self) -> None:
        pass

    @abstractmethod
    def ingredientes(self) -> None:
        pass

    @abstractmethod
    def coccion(self) -> None:
        pass

    @abstractmethod
    def presentacion(self) -> None:
        pass

    @abstractmethod
    def maridajes(self) -> None:
        pass

    @abstractmethod
    def extras(self) -> None:
        pass


class PizzaBuilder(Builder):
    def __init__(self) -> None:
        """
        Un constructor vacío que se utiliza para crear un objeto Pizza.
        """
        self.reset()

    def reset(self) -> None:
        self._pizza = Pizza()
    
    @property
    def pizza(self) -> Pizza:
        pizza = self._pizza
        self.reset()
        return pizza
    
    def masa(self) -> None:
        self._pizza.add("Masa")
    
    def base(self) -> None:
        self._pizza.add("Base")
    
    def ingredientes(self) -> None:
        self._pizza.add("Ingredientes")
    
    def coccion(self) -> None:
        self._pizza.add("Cocción")
    
    def presentacion(self) -> None:
        self._pizza.add("Presentación")

    def maridajes(self) -> None:
        self._pizza.add("Maridajes")

    def extras(self) -> None:
        self._pizza.add("Extras")

class Pizza():
    """
    Es el producto final que se obtiene de la construcción. 
    Contiene una lista de partes que se construyeron y ensamblaron.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        """
        Añadir un nuevo ingrediente a la pizza.
        """
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Pizza: {', '.join(self.parts)}", end="")

class Pizzeria():

    """
    El director. Construye un objeto usando la interfaz Builder.
    """

    def __init__(self) -> None:
        self._builder = None
    
    @property
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_pizza(self) -> None:
        self.builder.masa()
        self.builder.base()
        self.builder.ingredientes()
        self.builder.coccion()
        self.builder.presentacion()
        self.builder.maridajes()
        self.builder.extras()
