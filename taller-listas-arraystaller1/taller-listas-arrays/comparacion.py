import time
import numpy as np

# Creamos 100.000 números para la prueba
cantidad = 100_000
lista = list(range(cantidad))
array = np.arange(cantidad)

# Medimos el tiempo de la lista
inicio = time.perf_counter()
resultado_lista = [numero * 2 for numero in lista]
tiempo_lista = time.perf_counter() - inicio

# Medimos el tiempo del array
inicio = time.perf_counter()
resultado_array = array * 2
tiempo_array = time.perf_counter() - inicio

# Mostramos los resultados
print("COMPARACION DE RENDIMIENTO")
print("Cantidad de datos:", cantidad)
print("Tiempo de la lista:", tiempo_lista, "segundos")
print("Tiempo del array:", tiempo_array, "segundos")
print("¿Los resultados son iguales?", np.array_equal(resultado_lista, resultado_array))
