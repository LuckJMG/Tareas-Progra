from random import randint

# Inicio
print("Bienvenid@s a GimnasIWI!")

# Input
meta_calorias = int(input("Ingrese meta en calorias: "))

# Variables
total_calorias = 0
seguir = True

while seguir:
    # Menu de eleccion
    print("Ingrese ejercicio")
    print("(1) Sentadillas sumo")
    print("(2) Plancha abdominal")
    print("(3) Press frances")
    print("(4) Me canse")
    ejercicio = int(input())

    # Caso sentadillas sumo
    if ejercicio == 1:
        print("SENTADILLAS SUMO")

        # Variables
        repeticiones = int(input("¿Cuantas repeticiones?: "))

        # Calculo calorias
        calorias = repeticiones * randint(3, 7)

        total_calorias += calorias
        print("Calorias quemadas con sentadillas:", calorias)
        print("Calorias hasta el momento:", total_calorias)

    # Caso plancha abdominal
    elif ejercicio == 2:
        print("PLANCHA ABDOMINAL")

        # Variables
        segundos = int(input("Cuantos segundos?: "))
        n = 1
        calorias = 0

        # Calculo calorias
        while n <= segundos:
            i = 1
            factorial = 1

            # Calculo factorial de n
            while i <= n:
                factorial *= i
                i += 1

            calorias += (4 ** n) / factorial
            n += 1

        calorias = round(calorias)
        total_calorias += calorias
        print("Calorias quemadas con plancha:", calorias)
        print("Calorias hasta el momento:", total_calorias)

    # Caso press frances
    elif ejercicio == 3:
        print("PRESS FRANCES")

        # Variables
        repeticiones = int(input("¿Cuantas repeticiones?: "))
        kilos = int(input("¿Cuantos kilos?: "))
        i = 1

        # Calculo calorias
        if repeticiones > kilos:
            calorias = repeticiones
            raiz = repeticiones
            while i < kilos:
                raiz = 1 + (raiz ** (1 / 2))
                calorias += raiz
                i += 1
        else:
            raiz = kilos
            calorias = kilos
            while i < repeticiones:
                raiz = 1 + (raiz ** (1 / 2))
                calorias += raiz
                i += 1

        calorias = round(calorias)
        print("Calorias quemadas con press frances:", calorias)
        total_calorias += calorias
        print("Calorias hasta el momento:", total_calorias)

    # Caso me canse
    elif ejercicio == 4:
        seguir = False
        print("************")
        print("A descansar! Quemaste", total_calorias, "calorias")

    # Caso ingreso opcion invalida
    else:
        print("Ingrese una opcion valida")

    # Comprobar si se alcanzo la meta
    if total_calorias >= meta_calorias:
        seguir = False
        print("************")
        print("Meta cumplida! Quemaste", total_calorias, "de un total de", meta_calorias, "calorias")
