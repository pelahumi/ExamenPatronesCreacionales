import pandas as pd

def convertir_a_segundos(hora_minuto):
    if pd.isnull(hora_minuto):
        return None  # Retorna None si el valor es NaN o NaT
    partes = hora_minuto.split(':')
    if len(partes) == 2:  # formato HH:MM
        horas, minutos = partes
        return int(horas) * 3600 + int(minutos) * 60
    elif len(partes) == 3:  # formato HH:MM:SS
        horas, minutos, segundos = partes
        return int(horas) * 3600 + int(minutos) * 60 + int(segundos)
    
def agrupar_y_contar(data, col):
    grouped = data.groupby(col).size()
    return grouped 

def invertir(segundos):
    if segundos is None:
        return None  # Retorna None si el valor es None
    horas = segundos // 3600  # Obtenemos la cantidad de horas
    segundos_restantes = segundos % 3600
    minutos = segundos_restantes // 60  # Obtenemos la cantidad de minutos
    segundos_restantes = segundos_restantes % 60  # Los segundos que restan
    return f"{horas:02}:{minutos:02}:{segundos_restantes:02}"


def comprobador(data, col):
    if col == "Tiempo Llegada" or col == "Hora Solicitud" or col == "Hora Intervencion":
        data[col] = data[col].apply(invertir)
    else: 
        pass