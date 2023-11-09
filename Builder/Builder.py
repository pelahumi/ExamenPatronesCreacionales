from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from auxiliar import validator

from interface.masa import *
from interface.base import *
from interface.ingredientes import *
from interface.coccion import *
from interface.presentacion import *
from interface.maridajes import *
from interface.extras import *



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
    
    def masa(self, masa: Masa) -> None:
        self._pizza.add(masa.tipo_masa())
    
    def base(self, base: Base) -> None:
        self._pizza.add(base.tipo_base())
    
    def ingredientes(self, ingredientes: Ingredientes) -> None:
        self._pizza.add(ingredientes.tipo_ingredientes())
    
    def coccion(self, coccion: Coccion) -> None:
        self._pizza.add(coccion.tipo_coccion())
    
    def presentacion(self, presentacion: Presentacion) -> None:
        self._pizza.add(presentacion.tipo_presentacion())

    def maridajes(self, maridajes: Maridajes) -> None:
        self._pizza.add(maridajes.tipo_maridajes())

    def extras(self, extras: Extras) -> None:
        self._pizza.add(extras.tipo_extras())



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
        print(f"Ingredientes: {', '.join(self.parts)}", end="")
    
    def guardar_ingredientes(self) -> None:
        for part in self.parts:
            ingredientes = f"{', '.join(self.parts)}"
        return ingredientes







    