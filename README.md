[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8644516&assignment_repo_type=AssignmentRepo)
# L01-Ejercicios-introductorios

Crea dos módulos en un proyecto Python (`calificaciones.py` y `calificaciones_test.py`) e implementa los siguientes ejercicios. Separa la definición de las funciones, incluyéndolas en el módulo `calificaciones.py`, de la invocación para probar esas funciones, incluyéndolas en el módulo `calificaciones_test.py`.

### Ejercicio 1 

Se quiere ayudar a los alumnos de Fundamentos de Programación a calcular la nota de sus cuestionarios de teoría. Como estos alumnos estudian Python, se quieren implementar funciones que permitan hacer este cálculo. Para resolver un problema, antes hay que entenderlo, así que, antes de implementar los apartados siguientes, vamos a explicar el problema a resolver.

Un cuestionario de teoría está compuesto por 10 preguntas. Cada pregunta tiene asociadas 5 posibles respuestas, que se enumeran desde la a) hasta la e). Las preguntas son de respuesta múltiple. Lo que implica que puede haber una respuesta correcta, dos, tres, cuatro o, incluso cinco. Una vez que el alumno lee una pregunta, tiene que trasladar sus respuestas a una cuadrícula que aparece en la primera página del cuestionario, similar a la que puedes ver en la imagen que se muestra a continuación. Esta imagen se corresponde con las respuestas que la alumna Ada Byron marcó en el primer cuestionario de la asignatura. Fíjate que Ada marcó como respuestas correctas a la pregunta 1 las opciones a), b) y e). Además, una vez que Ada terminó su cuestionario, contó el número de casillas que había marcado con una X, y puso ese número en la casilla situada a la derecha de la celda Número total de casillas marcadas. Como puedes comprobar, Ada creía que en el cuestionario había 26 respuestas correctas.

![image](https://user-images.githubusercontent.com/72299672/135712707-e0898f87-d3fd-40b6-bb10-450d93e59139.png)

Cuando la profesora de Ada va a corregir su cuestionario, usa una plantilla similar a la que se adjunta en la siguiente imagen, en la que están marcadas las respuestas que son correctas en el cuestionario. Como puedes comprobar, en el cuestionario hay 27 respuestas correctas. 

![image](https://user-images.githubusercontent.com/72299672/135712630-2c7ed015-7877-460b-8529-6bab3a1ad376.png)

Para corregir el cuestionario de Ada, la profesora marca en rojo los errores, y cuenta para cada pregunta el número de aciertos y el número de errores, tal como se ve en la siguiente captura. Si te fijas de nuevo en la pregunta 1, podrás comprobar que Ada tiene dos aciertos (marcó sendas equis en las respuestas a) y b), que efectivamente eran respuestas correctas); tiene un error (ya que puso una X en la repuesta e), que es una respuesta incorrecta; y, finalmente, tiene una respuesta no encontrada, ya que la respuesta d) era correcta, y Ada no la marcó con una X.

![image](https://user-images.githubusercontent.com/72299672/135713363-34494ae6-eebf-41c4-9583-769d78ac8e24.png)

El resumen del resultado de Ada en el primer cuestionario es el siguiente:

* Aciertos: 23
* Errores: 3
* No encontrados: 4

Es decir, puso 23 X en los sitios correctos, marcó 3 X que no debería haber marcado, y no puso 4 X que debería haber marcado.

#### Apartado a

Escribe una función en Python que permita calcular la nota que un alumno tiene en un cuestionario. La nota se
calcula con la fórmula que se muestra más abajo, donde aciertos representa el número de aciertos del alumno, errores representa el número de errores del alumno, y totalRespuestas el número total de respuestas correctas del cuestionario. Ten en cuenta que un alumno no debe tener puntuaciones
negativas. Ayuda: Usa la función predefinida max de Python.

![image](https://user-images.githubusercontent.com/72299672/135712229-fc96131e-6b31-459d-afcd-a7a9b1d176c7.png)

Como ejemplo, puedes ver en la siguiente imagen cómo se calcularía la nota de Ada en el cuestionario 1. Un cuestionario con 27 respuestas correctas, en el que Ada tuvo 23 aciertos y 3 errores.

![image](https://user-images.githubusercontent.com/72299672/135713722-14d75bc3-6109-4f0e-b659-94ceeef357c5.png)


#### Apartado b

Escribe una función en python que solicite por consola el número de errores, el número de aciertos y el número total de respuestas correctas, y devuelva tres enteros correspondientes a los tres datos leídos por la consola.

#### Apartado c

En el modulo `calificaciones_test.py` invoca a las dos funciones anteriores para ayudar a Ada a calcular la nota de su cuestionario.


### Ejercicio 2

Se quiere ayudar a los alumnos de Fundamentos de Programación a calcular la nota por evaluación continua que han obtenido en la asignatura, de acuerdo a las siguientes fórmulas, donde Ci es la nota del cuestionario i, Pi es la nota del examen práctico i y PRYi es la nota del proyecto i (todas números reales de 0 a 10).

![image](https://user-images.githubusercontent.com/72299672/191313732-6d5b1146-c3bd-4685-a4e0-4bb92f7940fe.png)

Para estructurar bien el código divide el problema en las siguientes funciones:

#### Apartado a

Escribe una función `calcula_nota_cuatrimestre` que tenga como entrada tres parámetros: cuestionarios, una tupla con tres números reales correspondientes a las notas de los tres cuestionarios del cuatrimestre; parcial, una nota correspondiente al examen práctico; y proyecto, una nota correspondiente al proyecto. Esta función debe devolver la nota del estudiante en el cuatrimestre. Esta nota se calcula de la siguiente forma: si la nota del proyecto es inferior a 5, entoces la nota del cuatrimestre es un 3; si la nota del proyecto es superior o igual a 5, entonces la nota del cuatrimestre se calcula con la fórmula indicada anteriormente.

#### Apartado b

Escribe una función `calcula_nota_evaluacion_continua` que tenga como entrada tres parámetros: cuestionarios, una tupla con seis números reales correspondientes a las notas de los seis cuestionarios del cuatrimestre; parciales, una tupla con dos valores reales, correspondientes a los dos exámenes prácticos del cuatrimestre; y proyectos, una tupla con dos valores reales correspondiente a las notas de los dos proyectos de curso. Esta función debe devolver la nota del estudiante por evaluación continua. Esta nota se calcula de la siguiente forma:  si la nota del primer cuatrimestre es inferior a 4 o la nota del segundo cuatrimestre es inferior a 4, entonces la nota de la evaluación continua es 4. Si la nota de ambos cuatrimestres es superior a 4, entonces la nota se calcula como la media de las notas de los dos cuatrimestres, tal y como se muestra en la fórmula anterior.

#### Apartado c

Escribe tres funciones, en python para solicitar por consola las notas de los cuestionarios, las notas de los parciales y las notas de los proyectos.

#### Apartado d

En el modulo `calificaciones_test.py` invoca a las funciones anteriores para ayudar a Ada a calcular su nota por evaluación continua.
