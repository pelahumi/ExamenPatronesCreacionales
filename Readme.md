# ExamenPatronesCreacionales

Link de mi repositorio de [GitHub](https://github.com/pelahumi/ExamenPatronesCreacionales)

## ÍNDICE
---
1) [Abstract Factory](#1)
2) [Builder](#2)
---

## Abstract Factory<a name="1"></a>

### Idea general

En este ejercicio se pide implementar el patrón de diseño Abstract Factory para realizar cálculos estadísticos (moda, media, mediana) y hacer gráficos de dichos cálculos (histograma, diagrama de barras), partiendo de un fichero csv con datos sobre accidentes registrados por el SAMUR.

En el fichero abstractFactory.py es donde está implementado este patrón, tiene las siguientes clases:

#### 1) Abstract Factory

Es la clase abstracta ```AbstractFactory```, en la que definimos los métodos para calcular y graficar, que serán modificados por las concrete factories.

#### 2) Concrete Factories

Estas clases implementan la clase ```AbstractFactory``` y modifican sus métodos para crear productos específicos. Por ejemplo, la clase ```HistMeanFactory``` lo que hace es crear un producto que calcule la media y haga un histograma.

#### 3) Concrete Products

Estas clases son el resultado de las concrete factories. Siguiendo con el ejemplo anterior, la clase ```HistMeanFactory``` crea un producto de la clase ```Media``` y de ```Histograma```.

#### 4) Abstract Products

Estas clases abstractas actúan como interfaces para crear los concrete products. La clase ```Media``` hereda de su clase abstracta ```AbstractAnalisis``` y la clase ```Histograma``` de ```AbstractGrafico```.

Para obtener una visión más clara del patrón he creado un diagrama UML:


<p align="center">
  <img src="https://github.com/pelahumi/ExamenPatronesCreacionales/assets/91721764/9d136bc3-6856-419b-8647-cbf49584f137" alt="AbstractFactoryUML">
</p>

### Limpieza de datos

Antes de implementar el patrón, debemos de realizar una limpieza y filtrado de los datos proporcionados. Para ello echando un vistazo a los datos, vemos rápidamente que la columna: Año, es totalmente prescindible, ya que todas las llamadas o accidentes registrados por el SAMUR fueron hechas el mismo año: 2023.

Además, tenemos que tener en cuenta los valores nulos. En la columna: Hospital, vemos que más de la mitad de las filas son valores nulos, por lo que tenemos dos opciones: eliminar la columna de nuestro csv o sustituir los valores nulos por otro dato, eliminar las filas no es una opción válida porque estaríamos eliminando más de la mitad de nuestros datos. En mi caso, sustitui estos valores nulos por: No Hospitalizados.

Una vez hecho esto, hemos acabado con la gran mayoría de valores nulos, el resto al no ser un número representativo los podemos elimnar, dropeando las filas que los contienen.

Además, en la columna: Mes, cambié el valor de los datos por su equivalente valor numérico(enero:1, febrero:2...), para facilitar los cálculos.

Una vez que tenemos limpio nuestro csv, crearemos otro que almacene los datos limpios para facilitar su manipulación posterior -> samur_limpio.csv.

### Funciones auxiliares

En el fichero auxiliares.py tenemos la función ```convertir_a_segundos()```, cuya función es transformar las horas, minutos y segundos a segundos, para así facilitar los cálculos estadísticos. También hay una función que invierte esta transformación llamada ```invertir()```, para así dar nuestros resultados en el formato proporcionado.

Por último hay una función llamada ```comprobador()``` que lo que hace es comprobar si la columna sobre la que el usuario quiere hacer el análisis estadístico, es una columna que contiene datos en HH:MM:SS, para así aplicar las funciones anteriores. De lo contrario, no hace nada.


## Builder<a name="2"></a>

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






