# Pedir los tiempos de los nadadores en la primera prueba
tiempos_prueba1 = []
for i in range(1, 4):
    tiempo = int(input(f"Tiempo de nadador {i} en la primera prueba: "))
    tiempos_prueba1.append((i, tiempo))

# Ordenar los tiempos de menor a mayor
tiempos_prueba1.sort(key=lambda x: x[1])

# Identificar los empates en la primera prueba
empates_prueba1 = []
for i in range(len(tiempos_prueba1) - 1):
    if tiempos_prueba1[i][1] == tiempos_prueba1[i + 1][1]:
        empates_prueba1.append(tiempos_prueba1[i][0])
        empates_prueba1.append(tiempos_prueba1[i + 1][0])

# Asignar puntos a los nadadores según su posición en la primera prueba
puntos_prueba1 = [7, 5, 3]
if len(empates_prueba1) > 0:
    max_puntaje = max(puntos_prueba1)
    for nadador in empates_prueba1:
        puntos_prueba1[nadador - 1] = max_puntaje

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

# Identificar los empates en la segunda prueba
empates_prueba2 = []
for i in range(len(tiempos_prueba2) - 1):
    if tiempos_prueba2[i][1] == tiempos_prueba2[i + 1][1]:
        empates_prueba2.append(tiempos_prueba2[i][0])
        empates_prueba2.append(tiempos_prueba2[i + 1][0])

# Asignar puntos a los nadadores según su posición en la segunda prueba
puntos_prueba2 = [7, 5, 3]
if len(empates_prueba2) > 0:
    for nadador in empates_prueba2:
        puntos_prueba2[nadador - 1] = max(puntos_prueba2)

# Mostrar los resultados de la segunda prueba
print("Resultados de la segunda prueba:")
for i in range(3):
    print(f"Nadador {tiempos_prueba2[i][0]}: {tiempos_prueba2[i][1]} segundos, {puntos_prueba2[i]} puntos")

# Calcular los puntos totales de cada nadador
puntos_totales = [0, 0, 0]
for i in range(3):
    puntos_totales[tiempos_prueba1[i][0] - 1] += puntos_prueba1[i]
    puntos_totales[tiempos_prueba2[i][0] - 1] += puntos_prueba2[i]

# Crear una lista de tuplas (nadador, puntos) para ordenar el medallero final
medallero_final = [(i+1, puntos_totales[i]) for i in range(3)]
# Ordenar el medallero final por puntos, de mayor a menor
medallero_final.sort(key=lambda x: x[1], reverse=True)

# Mostrar el medallero final ordenado
print("Medallero final:")
# Manejar empates
puesto = 1
for i, (nadador, puntos) in enumerate(medallero_final):
    if i > 0 and puntos == medallero_final[i-1][1]:
        print(f"Empate en el puesto {puesto} entre los nadadores {medallero_final[i-1][0]} y {nadador}, {puntos} puntos")
    else:
        print(f"Ganador {puesto}: Nadador {nadador}, {puntos} puntos")
    puesto += 1