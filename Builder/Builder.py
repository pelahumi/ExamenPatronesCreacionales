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

    def pizza_pepperoni(self) -> None:
        self.builder.masa(MasaGruesa())
        self.builder.base(BaseTomate())
        self.builder.ingredientes(IngredientePepperoni())
        self.builder.ingredientes(IngredienteQueso())
        self.builder.coccion(CoccionHorno())
        self.builder.presentacion(PresentacionCaja())


if __name__ == "__main__":
    pizzeria = Pizzeria()
    builder = PizzaBuilder()
    pizzeria.builder = builder

    print("Pizza Pepperoni:")
    pizzeria.pizza_pepperoni()
    builder.pizza.list_parts()
