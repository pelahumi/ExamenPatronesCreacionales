from __future__ import annotations
from abc import ABC, abstractmethod

class Extras(ABC):
    """
    La interfaz Extras declara operaciones para todos los tipos de objetos Extras.
    """

    @abstractmethod
    def tipo_extras(self) -> str:
        pass

class ExtraBordeQueso(Extras):
    """
    Las clases concretas de Extras implementan la interfaz Extras.
    """

    def tipo_extras(self) -> str:
        return "Borde de Queso"

class ExtraTrufa(Extras):
    """
    Las clases concretas de Extras implementan la interfaz Extras.
    """

    def tipo_extras(self) -> str:
        return "Trufa"

class ExtraCaviar(Extras):
    """
    Las clases concretas de Extras implementan la interfaz Extras.
    """

    def tipo_extras(self) -> str:
        return "Caviar"