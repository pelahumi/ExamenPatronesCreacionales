from __future__ import annotations
from abc import ABC, abstractmethod

class Presentacion(ABC):
    """
    La interfaz Presentacion declara operaciones para todos los tipos de objetos Presentacion.
    """

    @abstractmethod
    def tipo_presentacion(self) -> str:
        pass

class PresentacionCaja(Presentacion):
    """
    Las clases concretas de Presentacion implementan la interfaz Presentacion.
    """

    def tipo_presentacion(self) -> str:
        return "Caja"

class PresentacionBandeja(Presentacion):
    """
    Las clases concretas de Presentacion implementan la interfaz Presentacion.
    """

    def tipo_presentacion(self) -> str:
        return "Bandeja"

class PresentacionTroceada(Presentacion):
    """
    Las clases concretas de Presentacion implementan la interfaz Presentacion.
    """

    def tipo_presentacion(self) -> str:
        return "Troceada"