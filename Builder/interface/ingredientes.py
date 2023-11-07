from __future__ import annotations
from abc import ABC, abstractmethod

class Ingredientes(ABC):
    """
    La interfaz Ingredientes declara operaciones para todos los tipos de objetos Ingredientes.
    """

    @abstractmethod
    def tipo_ingredientes(self) -> str:
        pass

class IngredienteQueso(Ingredientes):
    """
    Las clases concretas de Ingredientes implementan la interfaz Ingredientes.
    """

    def tipo_ingredientes(self) -> str:
        return "Queso"

class IngredienteJamon(Ingredientes):
    """
    Las clases concretas de Ingredientes implementan la interfaz Ingredientes.
    """

    def tipo_ingredientes(self) -> str:
        return "Jamón"

class IngredientePepperoni(Ingredientes):
    """
    Las clases concretas de Ingredientes implementan la interfaz Ingredientes.
    """

    def tipo_ingredientes(self) -> str:
        return "Pepperoni"

class IngredienteChampiñones(Ingredientes):
    """
    Las clases concretas de Ingredientes implementan la interfaz Ingredientes.
    """

    def tipo_ingredientes(self) -> str:
        return "Champiñones"

class IngredientePina(Ingredientes):
    """
    Las clases concretas de Ingredientes implementan la interfaz Ingredientes.
    """

    def tipo_ingredientes(self) -> str:
        return "Piña"