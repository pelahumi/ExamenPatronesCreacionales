from __future__ import annotations
from abc import ABC, abstractmethod

class Coccion(ABC):
    """
    La interfaz Coccion declara operaciones para todos los tipos de objetos Coccion.
    """

    @abstractmethod
    def tipo_coccion(self) -> str:
        pass

class CoccionHorno(Coccion):
    """
    Las clases concretas de Coccion implementan la interfaz Coccion.
    """

    def tipo_coccion(self) -> str:
        return "Horno"

class CoccionLeña(Coccion):
    """
    Las clases concretas de Coccion implementan la interfaz Coccion.
    """

    def tipo_coccion(self) -> str:
        return "Leña"

class CoccionPiedra(Coccion):
    """
    Las clases concretas de Coccion implementan la interfaz Coccion.
    """

    def tipo_coccion(self) -> str:
        return "Piedra"
