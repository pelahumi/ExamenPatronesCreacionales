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

    #Productos que están disponibles en la carta de la pizzería

    def pizza_pepperoni(self) -> None:
        self.builder.masa(MasaGruesa())
        self.builder.base(BaseTomate())
        self.builder.ingredientes(IngredientePepperoni())
        self.builder.ingredientes(IngredienteQueso())
        self.builder.coccion(CoccionHorno())
        self.builder.presentacion(PresentacionCaja())
    
    def pizza_jamon_queso(self) -> None:
        self.builder.masa(MasaFina())
        self.builder.base(BaseTomate())
        self.builder.ingredientes(IngredienteJamon())
        self.builder.ingredientes(IngredienteQueso())
        self.builder.coccion(CoccionHorno())
        self.builder.presentacion(PresentacionCaja())
    
    def pizza_hawaiana(self) -> None:
        self.builder.masa(MasaFina())
        self.builder.base(BaseTomate())
        self.builder.ingredientes(IngredienteJamon())
        self.builder.ingredientes(IngredientePina())
        self.builder.coccion(CoccionPiedra())
        self.builder.presentacion(PresentacionBandeja())
    
    def pizza_vegana(self) -> None:
        self.builder.masa(MasaFermentada())
        self.builder.base(BaseVegana())
        self.builder.ingredientes(IngredienteChampiñones())
        self.builder.ingredientes(IngredientePina())
        self.builder.coccion(CoccionLeña())
        self.builder.maridajes(MaridajeCerveza())
        self.builder.presentacion(PresentacionTroceada())
        
    def pizza_especial(self) -> None:
        self.builder.masa(MasaFina())
        self.builder.base(BaseEspecial())
        self.builder.ingredientes(IngredienteJamon())
        self.builder.ingredientes(IngredientePepperoni())
        self.builder.coccion(CoccionLeña())
        self.builder.maridajes(MaridajeCoctel())
        self.builder.presentacion(PresentacionBandeja())
        self.builder.extras(ExtraBordeQueso())
        self.builder.extras(ExtraTrufa())
        self.builder.extras(ExtraCaviar())
    
    #Pizza personalizada

    def personalizada(self) -> None:

        MASAS = ["Masa Fina", "Masa Gruesa", "Masa Fermentada"]
        BASES = ["Base de Tomate", "Base Vegana", "Base Especial"]
        INGREDIENTES = ["Queso", "Jamón", "Pepperoni", "Champiñones", "Piña"]
        COCCION = ["Horno", "Leña", "Piedra"]
        PRESENTACION = ["Caja", "Bandeja", "Troceada"]
        MARIDAJES = ["Vino", "Cerveza", "Coctel"]
        EXTRAS = ["Borde de Queso", "Trufa", "Caviar"]

        print("Elige los ingredientes de tu pizza:")
        print("1. Masa")
        for i in MASAS:
            print(i)
        seleccion_masa = input("Introduzca la opción que desea: ")

        while not validator(seleccion_masa, "Builder/masasDB.csv"):
            print("La masa que ha elegido no está disponible, por favor, elija otra.")
            seleccion_masa = input("Introduzca la opción que desea: ")

        if seleccion_masa == "Masa Fina":
            self.builder.masa(MasaFina())
        elif seleccion_masa == "Masa Gruesa":
            self.builder.masa(MasaGruesa())
        elif seleccion_masa == "Masa Fermentada":
            self.builder.masa(MasaFermentada())
        
        print("Ha elegido {}.".format(seleccion_masa))
        
        print("2. Base")
        for i in BASES:
            print(i)
        base = input("Introduzca la opción que desea: ")

        while not validator(base, BASES):
            print("La base que ha elegido no está disponible, por favor, elija otra.")
            base = input("Introduzca la opción que desea: ") 

        if base == "Base de Tomate":
            self.builder.base(BaseTomate())
        elif base == "Base Vegana":
            self.builder.base(BaseVegana())
        elif base == "Base Especial":
            self.builder.base(BaseEspecial())
        
        print("Ha elegido {}.".format(base))
        
        print("3. Ingredientes")
        for i in INGREDIENTES:
            print(i)
        ingrediente = input("Introduzca la opción que desea: ")

        while not validator(ingredientes, "DB/ingredientesDB.csv"):
            print("El ingrediente que ha elegido no está disponible, por favor, elija otro.")
            ingredientes = input("Introduzca la opción que desea: ")

        if ingrediente == "Queso":
            self.builder.ingredientes(IngredienteQueso())
        elif ingrediente == "Jamón":
            self.builder.ingredientes(IngredienteJamon())
        elif ingrediente == "Pepperoni":
            self.builder.ingredientes(IngredientePepperoni())
        elif ingrediente == "Champiñones":
            self.builder.ingredientes(IngredienteChampiñones())
        elif ingrediente == "Piña":
            self.builder.ingredientes(IngredientePina())

        print("Ha elegido {}.".format(ingrediente))
        
        print("4. Cocción")
        for i in COCCION:
            print(i)
        coccion = input("Introduzca la opción que desea: ")

        while not validator(coccion, COCCION):
            print("La cocción que ha elegido no está disponible, por favor, elija otra.")
            coccion = input("Introduzca la opción que desea: ")

        if coccion == "Horno":
            self.builder.coccion(CoccionHorno())
        elif coccion == "Leña":
            self.builder.coccion(CoccionLeña())
        elif coccion == "Piedra":
            self.builder.coccion(CoccionPiedra())

        print("Ha elegido {}.".format(coccion))
        
        print("5. Presentación")
        for i in PRESENTACION:
            print(i)
        presentacion = input("Introduzca la opción que desea: ")

        while not validator(presentacion, PRESENTACION):
            print("La presentación que ha elegido no está disponible, por favor, elija otra.")
            presentacion = input("Introduzca la opción que desea: ")

        if presentacion == "Caja":
            self.builder.presentacion(PresentacionCaja())
        elif presentacion == "Bandeja":
            self.builder.presentacion(PresentacionBandeja())
        elif presentacion == "Troceada":
            self.builder.presentacion(PresentacionTroceada())

        print("Ha elegido {}.".format(presentacion))
        
        print("6. Maridajes")
        for i in MARIDAJES:
            print(i)
        maridajes = input("Introduzca la opción que desea: ")

        while not validator(maridajes, MARIDAJES):
            print("El maridaje que ha elegido no está disponible, por favor, elija otro.")
            maridajes = input("Introduzca la opción que desea: ")

        if maridajes == "Vino":
            self.builder.maridajes(MaridajeVino())
        elif maridajes == "Cerveza":
            self.builder.maridajes(MaridajeCerveza())
        elif maridajes == "Coctel":
            self.builder.maridajes(MaridajeCoctel())
        
        print("Ha elegido {}.".format(maridajes))

        print("7. Extras")
        for i in EXTRAS:
            print(i)
        extras = input("Introduzca la opción que desea: ")

        while not validator(extras, EXTRAS):
            print("El extra que ha elegido no está disponible, por favor, elija otro.")
            extras = input("Introduzca la opción que desea: ")

        if extras == "Borde de Queso":
            self.builder.extras(ExtraBordeQueso())
        elif extras == "Trufa":
            self.builder.extras(ExtraTrufa())
        elif extras == "Caviar":
            self.builder.extras(ExtraCaviar())

        print("Ha elegido {}.".format(extras))





    