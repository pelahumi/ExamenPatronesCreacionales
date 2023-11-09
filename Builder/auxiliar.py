import csv

def guardar_pizza_en_csv(nombre_pizza, ingredientes):
    # Nombre del archivo CSV en el que se guardarán las pizzas
    archivo_csv = 'Builder/pizzasDB.csv'

    # Abre el archivo en modo de escritura
    with open(archivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        
        # Escribe los detalles de la pizza en el archivo
        writer.writerow([nombre_pizza, ingredientes])

def validator(lista, seleccion):
    if seleccion in lista:
        return True
    else:
        return False
    
