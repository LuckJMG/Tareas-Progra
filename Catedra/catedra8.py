def formatear_palabra(palabra):
    # Variables
    palabra_formateada = ""

    # Eliminar espacios
    for caracter in palabra:
        if caracter != ' ':
            palabra_formateada += caracter

    # Eliminar mayusculas
    palabra_formateada = palabra_formateada.lower()

    return palabra_formateada


def es_palindromo(palabra):
    # Variables locales
    palabra_formateada = formatear_palabra(palabra)
    palabra_invertida = ""
    index = -1

    # Invertir la palabra
    while index >= -len(palabra_formateada):
        palabra_invertida += palabra_formateada[index]
        index -= 1

    # Determinar si la palabra es un palindromo
    if palabra_formateada == palabra_invertida:
        return True

    return False


def coincidencia_caracteres(palabra1, palabra2):
    # Variables
    caracteres_coincididos = ""
    index = 0

    # Comprobar si los caracteres de ambas palabra en el mismo index son iguales
    while index < len(palabra1) and index < len(palabra2):
        if palabra1[index] == palabra2[index]:
            caracteres_coincididos += palabra1[index]
        index += 1

    return caracteres_coincididos


def comprobar_adn(cadena_adn):
    # Variables
    caracteres_validos = "ACGT-"

    # Comprobar valides del ADN
    for base in cadena_adn:
        if base not in caracteres_validos:
            return False

    return True


def puntos_partido(puntos):
    # Variables
    periodo = 1
    periodo_puntos = 0
    total_puntos = 0

    # Formatear puntos
    if puntos[len(puntos) - 1] != ' ':
        puntos_formateados = puntos + ' '
    else:
        puntos_formateados = puntos

    # Calcular puntaje
    for punto in puntos_formateados:
        if punto == 'L':
            periodo_puntos += 1
        elif punto == 'D':
            periodo_puntos += 2
        elif punto == 'T':
            periodo_puntos += 3
        elif punto == ' ':
            print(periodo_puntos, "puntos en el periodo", periodo)
            total_puntos += periodo_puntos
            periodo += 1
            periodo_puntos = 0

    return total_puntos

anotaciones = input("Anotaciones: ")
total_puntos = puntos_partido(anotaciones)
print("Total:", total_puntos, "puntos")
