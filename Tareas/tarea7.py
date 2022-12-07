def clasificar(tiempos, n):
    # Variables
    cupos = n
    participantes = []
    mejores_tiempos = []
    clasificados = []
    rezagados = []

    # Eliminar repetidos
    for vuelta in tiempos:
        participante = vuelta[0]
        tiempo = vuelta[1]

        if participante not in participantes:
            participantes.append(participante)
            mejores_tiempos.append(tiempo)
        else:
            posicion = participantes.index(participante)

            # Dejar solo el mejor tiempo en caso de repeticion
            if tiempo < mejores_tiempos[posicion]:
                del mejores_tiempos[posicion]
                mejores_tiempos.insert(posicion, tiempo)

    contador = len(participantes)

    # Seleccionar clasificados
    while contador > 0:
        posicion = mejores_tiempos.index(min(mejores_tiempos))

        if cupos > 0:
            clasificados.append([mejores_tiempos[posicion], participantes[posicion]])
            cupos -= 1
        else:
            rezagados.append([mejores_tiempos[posicion], participantes[posicion]])

        del participantes[posicion]
        del mejores_tiempos[posicion]
        contador -= 1

    return [clasificados, rezagados]

print("Bienvenidos al Gran Premio de Pythonia (Pythonia Moto Grand Prix 2022)\n")

# Sesion de practica
p = eval(input("Ingrese tiempos de la sesión de práctica: "))
participantes_p = clasificar(p, 10)
print("\nClasifican directamente a Q2:\n")
for clasificado in participantes_p[0]:
    print(clasificado[1], "con tiempo:", clasificado[0])

# Sesion Q1
q1 = eval(input("\nIngrese tiempos de la sesión Q1: "))
participantes_q1 = clasificar(q1, 2)
print("\nClasifican a Q2\n")
print(participantes_q1[0])
print("\nOrden de partida del puesto 13 en adelante:\n")
print(participantes_q1[1])

# Sesion Q2
q2 = eval(input("\nIngrese tiempos de la sesión Q2: "))
participantes_q2 = clasificar(q2, 12)

# Orden final
print("\nOrden de partida para el Gran Premio de Pythonia 2022:\n")
orden_final = participantes_q2[0] + participantes_q1[1]
for posicion in range(len(orden_final)):
    print(str(posicion + 1) + ".", orden_final[posicion][1])
