# Pedir los tiempos de los nadadores en la primera prueba
tiempos_prueba1 = []
for i in range(1, 4):
    tiempo = int(input(f"Tiempo de nadador {i} en la primera prueba: "))
    tiempos_prueba1.append((i, tiempo))

# Ordenar los tiempos de menor a mayor
tiempos_prueba1.sort(key=lambda x: x[1])

# Asignar puntos a los nadadores según su posición en la primera prueba
puntos_prueba1 = [7, 5, 3]

# Mostrar los resultados de la primera prueba
print("Resultados de la primera prueba:")
for i in range(3):
    print(f"Nadador {tiempos_prueba1[i][0]}: {tiempos_prueba1[i][1]} segundos, {puntos_prueba1[i]} puntos")

# Pedir los tiempos de los nadadores en la segunda prueba
tiempos_prueba2 = []
for i in range(1, 4):
    tiempo = int(input(f"Tiempo de nadador {i} en la segunda prueba: "))
    tiempos_prueba2.append((i, tiempo))

# Ordenar los tiempos de menor a mayor
tiempos_prueba2.sort(key=lambda x: x[1])

# Asignar puntos a los nadadores según su posición en la segunda prueba
puntos_prueba2 = [7, 5, 3]

# Mostrar los resultados de la segunda prueba
print("Resultados de la segunda prueba:")
for i in range(3):
    print(f"Nadador {tiempos_prueba2[i][0]}: {tiempos_prueba2[i][1]} segundos, {puntos_prueba2[i]} puntos")

# Calcular los puntos totales de cada nadador
puntos_totales = [puntos_prueba1[i] + puntos_prueba2[i] for i in range(3)]

# Mostrar el medallero final
print("Medallero final:")
for i in range(3):
    print(f"Puesto {i+1}: Nadador {tiempos_prueba1[i][0]}, {puntos_totales[i]} puntos")
