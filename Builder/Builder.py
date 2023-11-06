from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
import time
from auxiliar import guardar_pizza_en_csv
import tkinter as tk
from tkinter import ttk
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
            pizzeria.builder.base(BaseTomate())
        elif base == "2":
            print("Ha elegido Base Vegana")
            pizzeria.builder.base(BaseVegana())
        elif base == "3":
            print("Ha elegido Base Especial")
            pizzeria.builder.base(BaseEspecial())
        
        print("3. Ingredientes")
        for i in INGREDIENTES:
            print(i)
        ingredientes = input("Introduzca el número de la opción que desea: ")
        if ingredientes == "1":
            print("Ha elegido Queso")
            pizzeria.builder.ingredientes(IngredienteQueso())
        elif ingredientes == "2":
            print("Ha elegido Jamón")
            pizzeria.builder.ingredientes(IngredienteJamon())
        elif ingredientes == "3":
            print("Ha elegido Pepperoni")
            pizzeria.builder.ingredientes(IngredientePepperoni())
        elif ingredientes == "4":
            print("Ha elegido Champiñones")
            pizzeria.builder.ingredientes(IngredienteChampiñones())
        elif ingredientes == "5":
            print("Ha elegido Piña")
            pizzeria.builder.ingredientes(IngredientePina())
        
        print("4. Cocción")
        for i in COCCION:
            print(i)
        coccion = input("Introduzca el número de la opción que desea: ")
        if coccion == "1":
            print("Ha elegido Horno")
            pizzeria.builder.coccion(CoccionHorno())
        elif coccion == "2":
            print("Ha elegido Leña")
            pizzeria.builder.coccion(CoccionLeña())
        elif coccion == "3":
            print("Ha elegido Piedra")
            pizzeria.builder.coccion(CoccionPiedra())
        
        print("5. Presentación")
        for i in PRESENTACION:
            print(i)
        presentacion = input("Introduzca el número de la opción que desea: ")
        if presentacion == "1":
            print("Ha elegido Caja")
            pizzeria.builder.presentacion(PresentacionCaja())
        elif presentacion == "2":
            print("Ha elegido Bandeja")
            pizzeria.builder.presentacion(PresentacionBandeja())
        elif presentacion == "3":
            print("Ha elegido Troceada")
            pizzeria.builder.presentacion(PresentacionTroceada())
        
        print("6. Maridajes")
        for i in MARIDAJES:
            print(i)
        maridajes = input("Introduzca el número de la opción que desea: ")
        if maridajes == "1":
            print("Ha elegido Vino")
            pizzeria.builder.maridajes(MaridajeVino())
        elif maridajes == "2":
            print("Ha elegido Cerveza")
            pizzeria.builder.maridajes(MaridajeCerveza())
        elif maridajes == "3":
            print("Ha elegido Coctel")
            pizzeria.builder.maridajes(MaridajeCoctel())

        print("7. Extras")
        for i in EXTRAS:
            print(i)
        extras = input("Introduzca el número de la opción que desea: ")
        if extras == "1":
            print("Ha elegido Borde de Queso")
            pizzeria.builder.extras(ExtraBordeQueso())
        elif extras == "2":
            print("Ha elegido Trufa")
            pizzeria.builder.extras(ExtraTrufa())
        elif extras == "3":
            print("Ha elegido Caviar")
            pizzeria.builder.extras(ExtraCaviar())



class PizzaApp:
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



if __name__ == "__main__":
    pizzeria = Pizzeria()
    builder = PizzaBuilder()
    pizzeria.builder = builder

    CARTA = ["Jamón y queso, Pepperoni, Hawaiana, Vegana, Especial"]
    MASAS = ["Masa Fina, Masa Gruesa, Masa Fermentada"]
    BASES = ["Base de Tomate, Base Vegana, Base Especial"]
    INGREDIENTES = ["Queso, Jamón, Pepperoni, Champiñones, Piña"]
    COCCION = ["Horno, Leña, Piedra"]
    PRESENTACION = ["Caja, Bandeja, Troceada"]
    MARIDAJES = ["Vino, Cerveza, Coctel"]
    EXTRAS = ["Borde de Queso, Trufa, Caviar"]

    print("Bienvenido a la Pizzeria Pelayo, ¿Quiere ver nuestra carta o prefiere una pizza personalizada?:")
    print("1. Carta")
    print("2. Personalizada")
    opcion = input("Introduzca el número de la opción que desea: ")

    if opcion == "1":
        print("Carta:")
        for i in CARTA:
            print(i)
        eleccion = str(input("¿Qué pizza desea pedir?: "))


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
        
        
    
    elif opcion == "2":
        pizzeria.personalizada()
        print("Preparando su pizza...")
        time.sleep(2)
        ingredientes = builder.pizza.guardar_ingredientes()
        guardar_pizza_en_csv("Personalizada", ingredientes)
        print("Lista su pizza personalizada.")