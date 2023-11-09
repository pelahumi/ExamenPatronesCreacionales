from builder import PizzaBuilder, Pizzeria
import time
from auxiliar import guardar_pizza_en_csv, validator



def launcher():
    pizzeria = Pizzeria()
    builder = PizzaBuilder()
    pizzeria.builder = builder

    CARTA = ["Jamón y queso", "Pepperoni", "Hawaiana", "Vegana", "Especial"]


    print("Bienvenido a la Pizzeria Pelayo, ¿Quiere ver nuestra carta o prefiere una pizza personalizada?:")
    print("1. Carta")
    print("2. Personalizada")
    opcion = str(input("Introduzca el número de la opción que desea: "))

    if opcion == "1":
        print("Carta:")
        for i in CARTA:
            print(i)

        eleccion = input("¿Qué pizza desea pedir?: ")

        while validator(eleccion, CARTA) is False:
            print("La pizza que ha elegido no está en la carta, por favor, elija otra.")
            eleccion = input("¿Qué pizza desea pedir?: ")

        print("Preparando una pizza de {}...".format(eleccion))

        if eleccion == "Jamón y queso":
            pizzeria.pizza_jamon_queso()
        
        elif eleccion == "Pepperoni":
            pizzeria.pizza_pepperoni()
        
        elif eleccion == "Hawaiana":
            pizzeria.pizza_hawaiana()
        
        elif eleccion == "Vegana":
            pizzeria.pizza_vegana()
        
        elif eleccion == "Especial":
            pizzeria.pizza_especial()
        
        time.sleep(2)
        ingredientes = builder.pizza.guardar_ingredientes()
        guardar_pizza_en_csv(eleccion, ingredientes)
        print("Lista su pizza de {}.".format(eleccion))

    elif opcion == "2":
        pizzeria.personalizada()
        print("Preparando su pizza...")
        time.sleep(2)
        ingredientes = builder.pizza.guardar_ingredientes()
        guardar_pizza_en_csv("Personalizada", ingredientes)
        print("Lista su pizza personalizada.")

   