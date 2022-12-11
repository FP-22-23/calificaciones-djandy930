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

def test_dicc_series_por_anyo(fichero):
    print("Peliculas por año:", dict(dicc_series_por_anyo(fichero)))

def test_max_series_anyo(fichero):
    print("El año que mas series salieron fue:", max_series_anyo(fichero))

def test_dicc_porcentaje_series_anyo(fichero):
    print("El porcentaje de series por año es:", dicc_porcentaje_series_anyo(fichero))

def test_dicc_anyo_n_mejores_series_imdb(fichero):
    print("El diccionario que almacena las 3 mejores series según IMDB de cada año es:", dicc_anyo_n_mejores_series_imdb(fichero, 3))

def test_dicc_anyo_tupla(fichero):
    print("El diccionario que almacena las tuplas por año es:", dicc_anyo_tupla(fichero))

def test_dibuja_series_anyo(fichero):
    dibuja_series_anyo(fichero, 10)


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
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    test_dicc_series_por_anyo(series)
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    test_max_series_anyo(series)
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    test_dicc_porcentaje_series_anyo(series)
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    test_dicc_anyo_n_mejores_series_imdb(series)
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    test_dicc_anyo_tupla(series)
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    test_dibuja_series_anyo(series)