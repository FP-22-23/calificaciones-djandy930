# -*- coding: utf-8 -*-
import math
import csv
from datetime import datetime, date
from collections import namedtuple, Counter
from matplotlib import pyplot as plt

Series = namedtuple("Series", "id, title, year, age, imdb, rotten_tomatoes, netflix, hulu, prime_video, fecha_salida")

def parsear_bool(num):
    result = False
    if num=="1":
        result= True
    return result

def parsear_float(cadena):
    result = 0.0
    if cadena == "":
        result = 0.0
    else:
        result = float(cadena)
    return result


def lectura_fichero(fichero):
    result = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for id, title, year, age, imdb, rotten_tomatoes, netflix, hulu, prime_video, fecha_salida in lector:
            result.append((Series(int(id), title, int(year), age, 
                parsear_float(imdb), int(rotten_tomatoes), parsear_bool(netflix), 
                parsear_bool(hulu), parsear_bool(prime_video), datetime.strptime(fecha_salida, '%d-%m-%y').date())))
    return result

def esta_en_hulu(lista_series):
    result=[]
    for tupla in lista_series:
        if tupla.hulu == True:
            result.append(tupla.title)
    return result
    #return [tupla.title for tupla in lista_series if tupla.hulu==True]

def existe_serie_antes_de(lista_series, anyo):
    result=False
    for tupla in lista_series:
        if tupla.year < anyo:
            result = True
    return result
    

def maximo_imdb(lista_series):
    result = []
    for tupla in lista_series:
        result.append(tupla.imdb)
    return max(result)


def series_mas_valoracion_imdb(lista_series):
    result = []
    for tupla in lista_series:
        if tupla.imdb == maximo_imdb(lista_series):
            result.append(tupla)
    return result
    #return [tupla for tupla in lista_series if tupla.imdb == maximo_imdb(lista_series)]

def valoracion_series_ordenadas(lista_series, n):
    return sorted([tupla for tupla in lista_series if tupla.netflix], reverse=True, key= lambda n:n[5])[:n]

def dicc_series_por_anyo(lista_series):
    anyos = [tupla.year for tupla in lista_series]
    contador = Counter(anyos)
    return contador

def max_series_anyo(lista_series):
    anyo_mas_series = dicc_series_por_anyo(lista_series).most_common(1)[0][0]
    return anyo_mas_series

def porcentaje_series_anyo(lista_series, anyo):
    total_peliculas = len(lista_series)
    num_peliculas_anyo = len([tupla.title for tupla in lista_series if tupla.year==anyo])
    return num_peliculas_anyo/total_peliculas * 100

def dicc_porcentaje_series_anyo(lista_series):
    diccionario = dict()
    anyos = list(set([tupla.year for tupla in lista_series]))
    for anyo in anyos:
        diccionario[anyo] = porcentaje_series_anyo(lista_series, anyo)
    return diccionario

def anyo_n_mejores_series_imdb(lista_series, n, anyo):
    lista_ordenada = sorted([tupla for tupla in lista_series if tupla.year == anyo], key = lambda n: n[4], reverse=True)
    lista_nombres = [tupla.title for tupla in lista_ordenada][:n]
    return lista_nombres

def dicc_anyo_n_mejores_series_imdb(lista_series, n):
    diccionario = dict()
    anyos = list(set([tupla.year for tupla in lista_series]))
    for anyo in anyos:
        diccionario[anyo] = anyo_n_mejores_series_imdb(lista_series, n, anyo)
    return diccionario

def dicc_anyo_tupla(lista_series):
    diccionario = dict()
    anyos = list(set([tupla.year for tupla in lista_series]))
    for anyo in anyos:
        diccionario[anyo] = [tupla for tupla in lista_series if tupla.year ==anyo]
    return diccionario

def dibuja_series_anyo(lista_series, limite =5):
    '''
    Esta función va a obtener un diagrama de barras en el que en el eje x
    estarán los años y se represantará cuantas peliculas han salido en cada año
    '''
    series_anyo = dicc_series_por_anyo(lista_series)
    anyos = sorted(series_anyo, key = series_anyo.get, reverse=True)[:limite]
    peliculas = sorted((series_anyo.values()), reverse = True)[:limite]
    plt.bar(anyos, peliculas)
    plt.xticks(rotation=80)
    plt.title("Frecuencia de las peliculas por año:")
    plt.show()