# Taller de laboratorio: listas y arrays

## Parte 1. Comparación de rendimiento

### Objetivo
Comparar el tiempo de ejecución de una lista de Python y un array de NumPy al multiplicar 100.000 números por dos.

### Descripción del experimento
Se crearon una lista de Python y un array de NumPy con 100.000 números. Se multiplicó cada valor por dos y se midió el tiempo de cada operación usando `time.perf_counter()`. Finalmente, se comprobó que ambos resultados fueran iguales.

### Resultados obtenidos
Ejecuta `python comparacion.py` y copia aquí los tiempos exactos que aparezcan en tu terminal:

- Tiempo de ejecución de la lista: **[escribir el tiempo real] segundos**.
- Tiempo de ejecución del array: **[escribir el tiempo real] segundos**.
- ¿Los resultados fueron iguales?: el programa lo verifica al final.

Los tiempos pueden variar según el computador y la ejecución. No se debe afirmar cuál fue más rápido sin revisar los valores obtenidos.

### Análisis comparativo
Una lista de Python procesa la multiplicación mediante una operación por cada elemento. NumPy permite aplicar operaciones vectorizadas sobre arrays numéricos, lo que suele ser eficiente para grandes cantidades de datos. El rendimiento observado debe evaluarse con los tiempos medidos en la prueba.

### Respuestas a las preguntas

#### 1. ¿Qué diferencias se observaron en el tiempo?
La diferencia se identifica comparando los tiempos impresos por el programa. Estos pueden variar dependiendo del computador y de la ejecución.

#### 2. ¿Cómo influye la memoria?
Las listas almacenan referencias a objetos de Python. Los arrays numéricos de NumPy normalmente almacenan elementos de un tipo común en un bloque de memoria, lo que puede favorecer las operaciones numéricas.

#### 3. ¿Cuál estructura elegiría?
Elegiría una lista para colecciones generales de elementos y NumPy para operaciones matemáticas con grandes conjuntos de datos numéricos. La elección depende de la tarea.

## Parte 2. Algoritmo de calificaciones
El programa almacena cinco calificaciones, calcula el promedio original, cuenta estudiantes aprobados y reprobados usando 3.0 como nota mínima, ajusta las notas inferiores a 3.0 a ese valor y calcula el nuevo promedio. El ajuste es una regla ilustrativa para este ejercicio y no implica que deba aplicarse en una situación académica real.

### Conclusión general
Las listas y los arrays tienen características diferentes. La estructura adecuada depende de los datos, las operaciones requeridas y el rendimiento medido. La verificación de resultados ayuda a confirmar que la operación produce valores equivalentes.
