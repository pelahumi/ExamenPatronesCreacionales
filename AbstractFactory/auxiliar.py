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