import tkinter as tk
from builder import *

def pizzaApp():
    # Interfaz gráfica principal
    root = tk.Tk()
    root.title("Pizzeria Pelayo")
    
    pizzeria = Pizzeria()
    builder = PizzaBuilder()
    pizzeria.builder = builder

    # Función para manejar la selección de la carta
    def seleccionar_pizza():
        eleccion = lista_pizzas.get(lista_pizzas.curselection())
        if eleccion:
            label_estado.config(text=f"Preparando una pizza de {eleccion}...")
            root.update()
            time.sleep(2)  # Simular el tiempo de preparación
            # Aquí iría la lógica para preparar la pizza
            # Por ejemplo: pizzeria.pizza_jamon_queso()
            label_estado.config(text=f"Lista su pizza de {eleccion}.")
            ingredientes = builder.pizza.guardar_ingredientes()
            guardar_pizza_en_csv(eleccion, ingredientes)

    # Configuración de la lista de pizzas
    lista_pizzas = tk.Listbox(root)
    lista_pizzas.insert(1, "Jamón y queso")
    lista_pizzas.insert(2, "Pepperoni")
    lista_pizzas.insert(3, "Hawaiana")
    lista_pizzas.insert(4, "Vegana")
    lista_pizzas.insert(5, "Especial")
    lista_pizzas.pack()

    # Botón para seleccionar pizza de la carta
    boton_seleccionar = tk.Button(root, text="Seleccionar Pizza", command=seleccionar_pizza)
    boton_seleccionar.pack()

    # Etiqueta para mostrar el estado de la preparación de la pizza
    label_estado = tk.Label(root, text="")
    label_estado.pack()

    # Inicia la interfaz gráfica
    root.mainloop()

