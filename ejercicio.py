def main():
    # Pedir tiempos de los nadadores para la primera prueba
    print("Prueba 1")
    tiempos_1 = pedir_tiempos()

    # Ordenar los tiempos de menor a mayor
    tiempos_ordenados_1 = sorted(tiempos_1.values())

    # Asignar puntos a los nadadores de acuerdo a su posición en la primera prueba
    asignar_puntos(tiempos_1, tiempos_ordenados_1)

    # Pedir tiempos de los nadadores para la segunda prueba
    print("\nPrueba 2")
    tiempos_2 = pedir_tiempos()

    # Ordenar los tiempos de menor a mayor
    tiempos_ordenados_2 = sorted(tiempos_2.values())

    # Asignar puntos a los nadadores de acuerdo a su posición en la segunda prueba
    asignar_puntos(tiempos_2, tiempos_ordenados_2)

    # Calcular el total de puntos para cada nadador
    puntos_totales = calcular_puntos_totales(tiempos_1, tiempos_2)

    # Mostrar el medallero final
    mostrar_medallero(puntos_totales)


def pedir_tiempos():
    # Inicializa un diccionario vacío para almacenar los tiempos de los nadadores
    tiempos = {}
    # Pide al usuario el número de nadadores
    num_nadadores = int(input("Ingrese el número de nadadores: "))
    # Itera sobre cada nadador y pide su tiempo
    for i in range(1, num_nadadores + 1):
        tiempo = int(input(f"Ingrese el tiempo del nadador {i}: "))
        # Almacena el tiempo en el diccionario con la clave "Nadador X"
        tiempos[f"Nadador {i}"] = tiempo
    # Retorna el diccionario con los tiempos
    return tiempos


def asignar_puntos(tiempos, tiempos_ordenados):
    # Itera sobre cada nadador y su tiempo en el diccionario
    for nadador, tiempo in tiempos.items():
        # Encuentra la posición del tiempo en la lista ordenada
        posicion = tiempos_ordenados.index(tiempo) + 1
        # Asigna puntos según la posición
        if posicion == 1:
            tiempos[nadador] = 7
        elif posicion == 2:
            tiempos[nadador] = 5
        elif posicion == 3:
            tiempos[nadador] = 3
        else:
            tiempos[nadador] = 0


def calcular_puntos_totales(tiempos_1, tiempos_2):
    # Inicializa un diccionario vacío para almacenar los puntos totales
    puntos_totales = {}
    # Itera sobre cada nadador en los tiempos de la primera prueba
    for nadador in tiempos_1.keys():
        # Calcula el total de puntos sumando los puntos de ambas pruebas
        puntos_totales[nadador] = tiempos_1[nadador] + tiempos_2[nadador]
    # Retorna el diccionario con los puntos totales
    return puntos_totales


def mostrar_medallero(puntos_totales):
    # Ordena el diccionario de puntos totales en orden descendente
    medallero = sorted(puntos_totales.items(), key=lambda x: x[1], reverse=True)
    # Imprime el medallero final
    print("\nMedallero final:")
    for i, (nadador, puntos) in enumerate(medallero):
        print(f"Ganador {i + 1}: {nadador}, {puntos} puntos")


if __name__ == "__main__":
    main()