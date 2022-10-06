from principal import *
import os

def test_lectura(fichero):
    print("El número de series es:", len(fichero))
    print("Las 3 primeras series son:", fichero[:3])
    print("Las 3 últimas series son:", fichero[-3:])


if __name__=='__main__':
    series = lectura_fichero('data/fichero.csv')
    test_lectura(series)
    print(os.getcwd())
    