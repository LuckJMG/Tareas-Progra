from glob import escape
from random import randint


def generar_universo(size):
    if 10 <= size <= 35:
        # Variables
        vocales = "aeiou"
        consonantes = "bcdfghjklmnpqrstvwxyz"
        universo = ""
        cantidad_vocales = round(size * 0.4)
        cantidad_consonantes = size - cantidad_vocales

        # Generar vocales aleatorias del universo
        while cantidad_vocales != 0:
            universo += vocales[randint(0, len(vocales) - 1)]
            cantidad_vocales -= 1

        # Generar consonantes aleatorias del universo
        while cantidad_consonantes != 0:
            universo += consonantes[randint(0, len(consonantes) - 1)]
            cantidad_consonantes -= 1

        return universo

    else:
        return ""


def chequear_palabra(palabra, universo):
    # Variables
    contador_universo = 0
    contador_palabra = 0

    # Chequear si la palabra se puede construir con el universo
    for letra in palabra:
        # Cantidad de letras iguales en el universo
        for caracter in universo:
            if caracter == letra:
                contador_universo += 1

        # Cantidad de letras iguales en la palabra
        for caracter in palabra:
            if caracter == letra:
                contador_palabra += 1

        if letra not in universo or contador_universo < contador_palabra:
            return False

        contador_universo = 0
        contador_palabra = 0

    return True


def puntaje_palabra(palabra):
    # Variables
    vocales = "aeiou"
    vocales_contador = 0
    consonantes_contador = 0

    # Determinar cantidad de vocales y consonantes
    for letra in palabra:
        if letra in vocales:
            vocales_contador += 1
        else:
            consonantes_contador += 1

    # Calcular puntaje
    puntaje = 10 * len(palabra) + 5 * vocales_contador + 3 * consonantes_contador

    return puntaje


# Programa
# Variables
valido = True
en_universo = True
index = 0
puntos = 0
total_puntos = 0
tamano_universo = 0
palabra = ""

# Inicio programa
print("Bienvenido al PysCrable")

# Generar universo
while tamano_universo < 10:
    tamano_universo = int(input("Ingrese el tamaño del universo de letras: "))
universo = generar_universo(tamano_universo)
print("Universo:", universo)

# Formatear palabras
palabras = input("Ingrese sus 3 palabras separadas por un guión: ")
palabras += '-'

# Calcular puntaje final
while index < len(palabras) and valido:
    caracter = palabras[index]

    # Armar palabra actual
    if caracter != '-':
        palabra += caracter

    else:
        # Comprobar que las palabras tienen el largo permitido
        if len(palabra) >= 3:
            # Chequear si la palabra se puede armar con el universo
            en_universo = chequear_palabra(palabra, universo)

            # Si esta en el universo calcular puntaje
            if en_universo:
                puntos = puntaje_palabra(palabra)
                print(palabra, "se puede generar con", universo)
                print("obtienes", puntos, "puntos")
                total_puntos += puntos

            palabra = ""

        # En caso de que no sea de un largo permitido
        else:
            print("Error, las palabras deben tener al menos 3 letras, perdió su intento")
            total_puntos = 0
            valido = False

    index += 1

# Output final
print("Fin del intento, obtuviste un total de", total_puntos, "puntos")
