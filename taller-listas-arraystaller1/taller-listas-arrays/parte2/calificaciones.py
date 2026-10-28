# Taller de laboratorio: listas y arrays
# Programa para gestionar calificaciones

# Lista inicial de notas de los estudiantes
calificaciones = [3.5, 4.2, 2.8, 4.8, 3.0]

# Mostrar las calificaciones originales
print("CALIFICACIONES ORIGINALES")
print(calificaciones)

# Calcular el promedio original
promedio = sum(calificaciones) / len(calificaciones)
print("Promedio original:", round(promedio, 2))

# Contar estudiantes aprobados y reprobados (nota mínima: 3.0)
aprobados = 0
reprobados = 0
for nota in calificaciones:
    if nota >= 3.0:
        aprobados += 1
    else:
        reprobados += 1

print("Aprobados:", aprobados)
print("Reprobados:", reprobados)

# Regla ilustrativa del ejercicio: ajustar las notas inferiores a 3.0 a 3.0
for i in range(len(calificaciones)):
    if calificaciones[i] < 3.0:
        calificaciones[i] = 3.0

# Calcular nuevamente el promedio
nuevo_promedio = sum(calificaciones) / len(calificaciones)

# Mostrar el resumen final
print("\nCALIFICACIONES ACTUALIZADAS")
print(calificaciones)
print("Nuevo promedio:", round(nuevo_promedio, 2))
print("Total de estudiantes:", len(calificaciones))
