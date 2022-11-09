# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \22\>/\<23\>)
Autor: \<Andrés Osorno Rodríguez\>   uvus:\<pmq0707\>

Este dataset posee informacion de una lista comprensiva de canales de televisión disponibles en varias plataformas de streaming.

## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<principal.py\>**: Es el modulo principal y contiene el codigo de las funciones a realizar.
  * **\<test.py\>**: Es el modulo test y contiene el código de las funciones test.
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<tv_shows.csv\>**: Este dataset posee informacion de una lista comprensiva de series disponibles en varias plataformas de streaming.
    
## Estructura del *dataset*

El dataset está compuesto por \<10\> columnas, con la siguiente descripción:

* **\<columna 1>**: de tipo \<int\>, representa el ID de las series
* **\<columna 2>**: de tipo \<str\>, representa el título de las series
* **\<columna 3>**: de tipo \<int\>, representa el año de estreno de las series
* **\<columna 4>**: de tipo \<str\>, representa la edad permitida para ver las series seguido de un signo +
* **\<columna 5>**: de tipo \<float>, representa la valoración de IMDB
* **\<columna 6>**: de tipo \<int\>, representa la valoración de Rotten Tomatos
* **\<columna 7>**: de tipo \<bool\>, representa la valoración de Netflix
* **\<columna 8>**: de tipo \<bool\>, representa si la serie está en Hulu
* **\<columna 9>**: de tipo \<bool\>, representa si la serie está en Prime Video
* **\<columna 10>**: de tipo \<date\>, representa la fecha de salida de la serie

## Tipos implementados

Es una namedtuple denominada "Series" que posee como elementos cada una de las columnas

## Funciones implementadas

### \<principal\>

* **<lectura_ficheros(fichero)>**: Una  función  que  lea  el  fichero  y  devuelva  una lista  de  tuplas  con  la información que contiene
* **<esta_en_hulu(lista_series)>**: Te muestra todas las series que están en Hulu
* **<existe_serie_antes_de(lista_series, anyo)>**: Si existe una serie que salió antes que el año que le pasamos, la función te devuelve "True"
* **<maximo_imdb(lista_series)>**: Te devuelve la nota máxima de todas las series de IMDB

### \<test\>

* **<test_lectura(fichero)>**: El test que realiza la lectura del fichero. Te muestra el número de series que hay y te dice las tres primeras y tres últimas series
*
