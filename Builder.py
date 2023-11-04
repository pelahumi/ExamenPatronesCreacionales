from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

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
