from builder import Builder
from auxiliar import validator
from interface.masa import *
from interface.base import *
from interface.ingredientes import *
from interface.coccion import *
from interface.presentacion import *
from interface.maridajes import *
from interface.extras import *


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

        #Definimos los elementos en listas inmutables para mostrarlos por pantalla
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

        while not validator(seleccion_masa):
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

        while not validator(base):
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

        while not validator(ingrediente):
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

        while not validator(coccion):
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

        while not validator(presentacion):
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

        while not validator(maridajes):
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

        while not validator(extras):
            print("El extra que ha elegido no está disponible, por favor, elija otro.")
            extras = input("Introduzca la opción que desea: ")

        if extras == "Borde de Queso":
            self.builder.extras(ExtraBordeQueso())
        elif extras == "Trufa":
            self.builder.extras(ExtraTrufa())
        elif extras == "Caviar":
            self.builder.extras(ExtraCaviar())

        print("Ha elegido {}.".format(extras))