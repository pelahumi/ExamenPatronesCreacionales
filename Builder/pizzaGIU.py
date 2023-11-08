import tkinter as tk
from tkinter import ttk
from builder import *

import tkinter as tk
from tkinter import ttk


# Asumiendo que las clases Pizzeria, PizzaBuilder y la función guardar_pizza_en_csv están definidas anteriormente.
# Asegúrate de implementar la función guardar_pizza_en_csv.

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
        
        # Opciones de carta o personalizada
        self.opcion_var = tk.StringVar(value="1")
        self.carta_button = ttk.Radiobutton(self.root, text="1. Carta", variable=self.opcion_var, value="1")
        self.carta_button.pack()
        self.person_button = ttk.Radiobutton(self.root, text="2. Personalizada", variable=self.opcion_var, value="2")
        self.person_button.pack()

        # Botón para confirmar elección
        self.confirm_button = ttk.Button(self.root, text="Confirmar", command=self.confirmar_opcion)
        self.confirm_button.pack()

    def confirmar_opcion(self):
        opcion = self.opcion_var.get()
        if opcion == "1":
            self.mostrar_carta()
        elif opcion == "2":
            self.pizzeria.personalizada()  # Asumiendo que esta es una función definida en Pizzeria

    def mostrar_carta(self):
        CARTA = ["Jamón y queso", "Pepperoni", "Hawaiana", "Vegana", "Especial"]
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
        # ... código para preparar la pizza y guardar ingredientes ...


# Asegúrate de que las clases Pizzeria y PizzaBuilder estén definidas aquí o importadas
# A continuación, se inicia la aplicación si este archivo es el script principal.

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaApp(root)
    root.mainloop()
