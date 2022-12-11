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
* **<series_mas_valoracion_imdb(lista_series)>**: Te devuelve la serie o series que tienen la nota más alta
* **<valoracion_series_ordenadas(lista_series, n)>**: Te devuelve las n series más valoradas ordenadas por rotten_tomatoes y que están en Netflix
* **<dicc_series_por_anyo(lista_series)>**: Nos devuelve un diccionario en el que la clave es el año y el valor es el número de series que han salido ese año
* **<max_series_anyo(lista_series)>**: Te devuelve el año en el que más series han sacado
* **<porcentaje_series_anyo(lista_series, anyo)>**: Te devuelve el porcentaje de series que salieron el año dado sobre el total de series
* **<dicc_porcentaje_series_anyo(lista_series)>**: Te devuelve un diccionario en el que la clave es el año y el valor es el porcentaje de series que salieron ese año sobre el total de series
* **<anyo_n_mejores_series_imdb(lista_series, n, anyo)>**: Te devuelve una lista con las n mejores series en un año siguiendo el criterio de IMDB
* **<dicc_anyo_n_mejores_series_imdb(lista_series, n)>**: Te devuelve un diccionario en el que la clave es el año y el valor es una lista con las n mejores series de ese año
* **<dicc_anyo_tupla(lista_series)>**: Te devuelve un diccionario en el que la clave es el año y el valor es una lista de tuplas de las series que salieron en ese año
* **<dibuja_series_anyo(lista_series, limite =5)>**: Te devuelve un diagrama de barras en el que el eje x son los años y el eje y el número de películas que han salido en cada año. Hay un parámetro límite para mostrar los "limite" años en los que más series salieron

### \<test\>

* **<test_lectura(fichero)>**: El test que realiza la lectura del fichero. Te muestra el número de series que hay y te dice las tres primeras y tres últimas series
* **<test_esta_en_hulu(fichero)>**: El test que te muestra la lista de las series que están en Hulu
* **<test_existe_serie_antes_de(fichero)>**: El test que te muestra con True o False si había una serie anterior a un año que le pasamos
* **<test_series_mas_valoracion_imdb(fichero)>**: El test que te muestra las series mejor valoradas de IMDB
* **<test_valoracion_series_ordenadas(fichero)>**: El test que te devuelve las n series más valoradas que están ordenadas por rotten_tomatos y que están en Netflix
* **<test_dicc_series_por_anyo(series)>**: En este test se ejecutará la función dicc_series_por_anyo(series)
* **<test_max_series_anyo(series)>**: En este test se ejecutará la función max_series_anyo(series)
* **<test_dicc_porcentaje_series_anyo(series)>**: En este test se ejecutará la función dicc_porcentaje_series_anyo(series)
* **<test_dicc_anyo_n_mejores_series_imdb(series)>**: En este test se ejecutará la función dicc_anyo_n_mejores_series_imdb(series, 3)
* **<test_dicc_anyo_tupla(series)>**: En este test se ejecutará la función dicc_anyo_tupla(series)
* **<test_dibuja_series_anyo(series)>**: En este test se ejecutará la función dibuja_series_anyo(series, limite = 5)
