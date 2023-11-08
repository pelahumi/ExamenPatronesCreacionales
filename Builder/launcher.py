from builder import PizzaBuilder, Pizzeria
import time
from auxiliar import guardar_pizza_en_csv
import tkinter as tk


"""def launcher():
    pizzeria = Pizzeria()
    builder = PizzaBuilder()
    pizzeria.builder = builder

    CARTA = ["Jamón y queso, Pepperoni, Hawaiana, Vegana, Especial"]

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
        print("Lista su pizza personalizada.")"""


def launcher():
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

launcher()
