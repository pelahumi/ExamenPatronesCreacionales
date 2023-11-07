from __future__ import annotations
from abc import ABC, abstractmethod


class Maridajes(ABC):
    """
    La interfaz Maridajes declara operaciones para todos los tipos de objetos Maridajes.
    """

    @abstractmethod
    def tipo_maridajes(self) -> str:
        pass

class MaridajeVino(Maridajes):
    """
    Las clases concretas de Maridajes implementan la interfaz Maridajes.
    """

    def tipo_maridajes(self) -> str:
        return "Vino"

class MaridajeCerveza(Maridajes):
    """
    Las clases concretas de Maridajes implementan la interfaz Maridajes.
    """

    def tipo_maridajes(self) -> str:
        return "Cerveza"

class MaridajeCoctel(Maridajes):
    """
    Las clases concretas de Maridajes implementan la interfaz Maridajes.
    """

    def tipo_maridajes(self) -> str:
        return "Coctel"