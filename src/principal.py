# -*- coding: utf-8 -*-
import math
import csv
from datetime import datetime, date
from collections import namedtuple

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
        

