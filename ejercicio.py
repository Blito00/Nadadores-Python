# Pedir los tiempos de los nadadores en la primera prueba
tiempos_prueba1 = []
for i in range(1, 7):
    tiempo = int(input(f"Tiempo de nadador {i} en la primera prueba: "))
    tiempos_prueba1.append(tiempo)

# Ordenar los tiempos de menor a mayor
tiempos_prueba1.sort()

# Asignar puntos a los nadadores según su posición en la primera prueba
puntos_prueba1 = [7, 5, 3]

# Mostrar los resultados de la primera prueba
print("Resultados de la primera prueba:")
for i in range(3):
    print(f"Nadador {i+1}: {tiempos_prueba1[i]} minutos, {puntos_prueba1[i]} puntos")

# Pedir los tiempos de los nadadores en la segunda prueba
tiempos_prueba2 = []
for i in range(1, 7):
    tiempo = int(input(f"Tiempo de nadador {i} en la segunda prueba: "))
    tiempos_prueba2.append(tiempo)

# Ordenar los tiempos de menor a mayor
tiempos_prueba2.sort()

# Asignar puntos a los nadadores según su posición en la segunda prueba
puntos_prueba2 = [7, 5, 3]

# Mostrar los resultados de la segunda prueba
print("Resultados de la segunda prueba:")
for i in range(3):
    print(f"Nadador {i+1}: {tiempos_prueba2[i]} minutos, {puntos_prueba2[i]} puntos")

# Calcular los puntos totales de cada nadador
puntos_totales = [puntos_prueba1[i] + puntos_prueba2[i] for i in range(3)]

# Mostrar el medallero final
print("Medallero final:")
for i in range(3):
    print(f"Ganador {i+1}: Nadador {i+1}, {puntos_totales[i]} puntos")