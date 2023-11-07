from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
import time
from auxiliar import guardar_pizza_en_csv
import tkinter as tk
from tkinter import ttk

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

        MASAS = ["Masa Fina, Masa Gruesa, Masa Fermentada"]
        BASES = ["Base de Tomate, Base Vegana, Base Especial"]
        INGREDIENTES = ["Queso, Jamón, Pepperoni, Champiñones, Piña"]
        COCCION = ["Horno, Leña, Piedra"]
        PRESENTACION = ["Caja, Bandeja, Troceada"]
        MARIDAJES = ["Vino, Cerveza, Coctel"]
        EXTRAS = ["Borde de Queso, Trufa, Caviar"]

        print("Elige los ingredientes de tu pizza:")
        print("1. Masa")
        for i in MASAS:
            print(i)
        seleccion_masa = input("Introduzca el número de la opción que desea: ")
        if seleccion_masa == "1":
            print("Ha elegido Masa Fina")
            self.builder.masa(MasaFina())
        elif seleccion_masa == "2":
            print("Ha elegido Masa Gruesa")
            self.builder.masa(MasaGruesa())
        elif seleccion_masa == "3":
            print("Ha elegido Masa Fermentada")
            self.builder.masa(MasaFermentada())
        
        print("2. Base")
        for i in BASES:
            print(i)
        base = input("Introduzca el número de la opción que desea: ")
        if base == "1":
            print("Ha elegido Base de Tomate")
            self.builder.base(BaseTomate())
        elif base == "2":
            print("Ha elegido Base Vegana")
            self.builder.base(BaseVegana())
        elif base == "3":
            print("Ha elegido Base Especial")
            self.builder.base(BaseEspecial())
        
        print("3. Ingredientes")
        for i in INGREDIENTES:
            print(i)
        ingredientes = input("Introduzca el número de la opción que desea: ")
        if ingredientes == "1":
            print("Ha elegido Queso")
            self.builder.ingredientes(IngredienteQueso())
        elif ingredientes == "2":
            print("Ha elegido Jamón")
            self.builder.ingredientes(IngredienteJamon())
        elif ingredientes == "3":
            print("Ha elegido Pepperoni")
            self.builder.ingredientes(IngredientePepperoni())
        elif ingredientes == "4":
            print("Ha elegido Champiñones")
            self.builder.ingredientes(IngredienteChampiñones())
        elif ingredientes == "5":
            print("Ha elegido Piña")
            self.builder.ingredientes(IngredientePina())
        
        print("4. Cocción")
        for i in COCCION:
            print(i)
        coccion = input("Introduzca el número de la opción que desea: ")
        if coccion == "1":
            print("Ha elegido Horno")
            self.builder.coccion(CoccionHorno())
        elif coccion == "2":
            print("Ha elegido Leña")
            self.builder.coccion(CoccionLeña())
        elif coccion == "3":
            print("Ha elegido Piedra")
            self.builder.coccion(CoccionPiedra())
        
        print("5. Presentación")
        for i in PRESENTACION:
            print(i)
        presentacion = input("Introduzca el número de la opción que desea: ")
        if presentacion == "1":
            print("Ha elegido Caja")
            self.builder.presentacion(PresentacionCaja())
        elif presentacion == "2":
            print("Ha elegido Bandeja")
            self.builder.presentacion(PresentacionBandeja())
        elif presentacion == "3":
            print("Ha elegido Troceada")
            self.builder.presentacion(PresentacionTroceada())
        
        print("6. Maridajes")
        for i in MARIDAJES:
            print(i)
        maridajes = input("Introduzca el número de la opción que desea: ")
        if maridajes == "1":
            print("Ha elegido Vino")
            self.builder.maridajes(MaridajeVino())
        elif maridajes == "2":
            print("Ha elegido Cerveza")
            self.builder.maridajes(MaridajeCerveza())
        elif maridajes == "3":
            print("Ha elegido Coctel")
            self.builder.maridajes(MaridajeCoctel())

        print("7. Extras")
        for i in EXTRAS:
            print(i)
        extras = input("Introduzca el número de la opción que desea: ")
        if extras == "1":
            print("Ha elegido Borde de Queso")
            self.builder.extras(ExtraBordeQueso())
        elif extras == "2":
            print("Ha elegido Trufa")
            self.builder.extras(ExtraTrufa())
        elif extras == "3":
            print("Ha elegido Caviar")
            self.builder.extras(ExtraCaviar())



"""class PizzaApp:
    def __init__(self, root):
        self.pizzeria = Pizzeria()
        self.builder = PizzaBuilder()
        self.pizzeria.builder = self.builder

        self.root = root
        self.root.title("Pizzería Pelayo")

        # Crear widgets
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Bienvenido a la Pizzería Pelayo, ¿Quiere ver nuestra carta o prefiere una pizza personalizada?").pack()
        self.cart_button = ttk.Button(self.root, text="1. Carta", command=self.mostrar_carta)
        self.cart_button.pack()
        self.person_button = ttk.Button(self.root, text="2. Personalizada", command=self.pizza_personalizada)
        self.person_button.pack()

    def mostrar_carta(self):
        carta_window = tk.Toplevel(self.root)
        carta_window.title("Carta de Pizzas")
        
        ttk.Label(carta_window, text="Seleccione una pizza de la carta:").pack()
        self.pizza_var = tk.StringVar()
        pizza_menu = ttk.Combobox(carta_window, textvariable=self.pizza_var, values=CARTA)
        pizza_menu.pack()
        
        order_button = ttk.Button(carta_window, text="Ordenar", command=self.preparar_pizza)
        order_button.pack()

    def preparar_pizza(self):
        eleccion = self.pizza_var.get()

        if eleccion == "Jamón y queso":
            print("Preparando una pizza de Jamón y queso...")
            pizzeria.pizza_jamon_queso()
            time.sleep(2)
            ingredientes = builder.pizza.guardar_ingredientes()
            guardar_pizza_en_csv("Jamón y queso", ingredientes)
            print("Lista su pizza de Jamón y queso.")
            
        
        elif eleccion == "Pepperoni":
            print("Preparando una pizza Pepperoni...")
            pizzeria.pizza_pepperoni()
            time.sleep(2)
            ingredientes = builder.pizza.guardar_ingredientes()
            guardar_pizza_en_csv("Pepperoni", ingredientes)
            print("Lista su pizza de Pepperoni.")
            
        
        elif eleccion == "Hawaiana":
            print("Preparando una pizza Hawaiana...")
            pizzeria.pizza_hawaiana()
            time.sleep(2)
            ingredientes = builder.pizza.guardar_ingredientes()
            guardar_pizza_en_csv("Hawaiana", ingredientes)
            print("Lista su pizza de Hawaiana.")

        elif eleccion == "Vegana":
            print("Preparando una pizza Vegana...")
            pizzeria.pizza_vegana()
            time.sleep(2)
            ingredientes = builder.pizza.guardar_ingredientes()
            guardar_pizza_en_csv("Hawaiana", ingredientes)
            print("Lista su pizza de Hawaiana.")
        
        elif eleccion == "Especial":
            print("Preparando una pizza Especial...")
            pizzeria.pizza_especial()
            time.sleep(2)
            ingredientes = builder.pizza.guardar_ingredientes()
            guardar_pizza_en_csv("Especial", ingredientes)
            print("Lista su pizza Especial.")
        
        else:
            print("No tenemos esa pizza en la carta, lo sentimos.")

        # ... y así sucesivamente para cada tipo de pizza ...

    def pizza_personalizada(self):
        personalizada_window = tk.Toplevel(self.root)
        personalizada_window.title("Pizza Personalizada")

        # Aquí implementarías la lógica para permitir al usuario seleccionar los componentes de su pizza.
        # Puedes usar Entry, Combobox o cualquier otro widget para recoger la entrada del usuario.

        # Por ejemplo, crear menús desplegables para cada tipo de ingrediente:
        ttk.Label(personalizada_window, text="Seleccione la masa:").pack()
        masa_menu = ttk.Combobox(personalizada_window, values=MASAS)
        masa_menu.pack()

        # ... y así sucesivamente para cada componente ...

        # Finalmente, un botón para confirmar la selección del usuario y preparar la pizza.
        confirm_button = ttk.Button(personalizada_window, text="Confirmar", command=self.confirmar_personalizada)
        confirm_button.pack()

    def confirmar_personalizada(self):
        # Aquí implementarías la lógica para construir la pizza personalizada según las selecciones del usuario.
        pass
"""


    