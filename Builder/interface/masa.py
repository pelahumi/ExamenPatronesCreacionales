from __future__ import annotations
from abc import ABC, abstractmethod

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