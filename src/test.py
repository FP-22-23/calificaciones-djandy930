from principal import *
import os

def test_lectura(fichero):
    print("El número de series es:", len(fichero))
    print("Las 3 primeras series son:", fichero[:3])
    print("Las 3 últimas series son:", fichero[-3:])

def test_esta_en_hulu(fichero):
    print("Esta es la lista de las series que están disponibles en Hulu:", esta_en_hulu(fichero))

def test_existe_serie_antes_de(fichero):
    print("¿Existe una serie anterior al año 1992?", existe_serie_antes_de(fichero, 1992))
    print("¿Existe una serie anterior al año 1300?", existe_serie_antes_de(fichero, 1300))

def test_series_mas_valoracion_imdb(fichero):
    print("Estas son las series con máxima valoración:", series_mas_valoracion_imdb(fichero))

def test_valoracion_series_ordenadas(fichero):
    print("Listado de 5 series con más valoración rotten tomatoes que están en netflix:", valoracion_series_ordenadas(fichero, 5))


if __name__=='__main__':
    series = lectura_fichero('data/fichero.csv')
    test_lectura(series)
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("Segundo ejercicio")
    test_esta_en_hulu(series)
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    test_existe_serie_antes_de(series)
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    test_series_mas_valoracion_imdb(series)
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    test_valoracion_series_ordenadas(series)
    