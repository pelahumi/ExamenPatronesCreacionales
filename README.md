# ExamenPatronesCreacionales

Link de mi repositorio de [GitHub](https://github.com/pelahumi/ExamenPatronesCreacionales)

## ÍNDICE
---
1) Abstract Factory
2) Builder
---

## Abstract Factory

## Builder

### Idea general

En este ejercicio se nos pide hacer una pizzería implementando el patrón de diseño builder. El esqueleto principal de nuestra pizzería es el builder.py, en el que implementamos el patrón builder para la creación de diferentes pizzas. Este fichero consta de cuatro clases:

#### 1) Builder

La clase ```Builder``` es la clase abstracta (interface) en la que definimos los métodos para crear los diferentes elementos de la pizza. Como es una clase abstracta (interface), dichos métodos solo serán definidos, y serán modificados en la subclase que la implementa.

#### 2) PizzaBuilder

La clase ```PizzaBuilder``` es la clase que hereda de ```Builder```, aquí es donde vamos a modificar los métodos que definimos en ```Builder``` para que hagan lo que nosotros queramos, en nuestro caso agregan los elementos a la pizza.

#### 3) Pizza

La clase ```Pizza``` es el producto que crea nuestro patrón builder, a partir de la clase ```PizzaBuilder```. Esta clase tiene tres métodos: ```add()``` añader elementos a la pizza, ```list_parts()``` devuelve por pantalla los ingredientes que tiene la pizza. Y además, añadí un método ```guardar_ingredientes()``` para almacenar los ingredientes de cada pizza en una variable, y posteriormente añadirlos al archivo .csv.

#### 4) Pizzería

Por último, tenemos al director de orquesta, la clase ```Pizzeria```. que es la encargada de crear cada tipo de pizza.

Para ver todo esto más claramente, construimos un diagrama UML donde se puede apreciar mejor las relaciones entre las distintas clases:


<p align="center">
  <img src="https://github.com/pelahumi/ExamenPatronesCreacionales/assets/91721764/f965a62e-c7a2-43dd-9e12-d63fdc29d929" alt="BuilderUML">
</p>


### Elementos de la pizza

Para los elementos de la pizza, creamos una clase abstracta para cada elemento (interface): ```Masa```, ```Base```, ```Ìngredientes```, ```Coccion```, ```Presentacion```, ```Maridajes``` y ```Èxtras```, de las cuales obtendremos cada tipo de elemento, como por ejemplo: de ```Masa```obtenemos los tres tipos de masa de nuestra pizzería ```MasaFina```, ```MasaGruesa``` y ```MasaFermentada```. 
A partir de aquí, cada subclase de los elementos devuelve un str con el tipo de elemento, para posteriormente agregarlo a la pizza.

### Almacenamiento de datos

En el fichero auxiliar.py tenemos la función ```guardar_pizza_en_csv()``` que recibe dos argumentos: el nombre de la pizza y sus ingredientes, y los almacena en el archivo pizzasDB.csv.






