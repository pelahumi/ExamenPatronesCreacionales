from __future__ import annotations
from abc import ABC, abstractmethod

class Base(ABC):
    """
    La interfaz Base declara operaciones para todos los tipos de objetos Base.
    """

    @abstractmethod
    def tipo_base(self) -> str:
        pass

class BaseTomate(Base):
    """
    Las clases concretas de Base implementan la interfaz Base.
    """

    def tipo_base(self) -> str:
        return "Base de Tomate"

class BaseVegana(Base):
    """
    Las clases concretas de Base implementan la interfaz Base.
    """

    def tipo_base(self) -> str:
        return "Base Vegana"

class BaseEspecial(Base):
    """
    Las clases concretas de Base implementan la interfaz Base.
    """

    def tipo_base(self) -> str:
        return "Base Especial"