"""
# Input
radio = int(input("Radio: "))
centro_x = int(input("Coordenada x del centro: "))
centro_y = int(input("Coordenada y del centro: "))
punto_x = int(input("Coordenada x del punto: "))
punto_y = int(input("Coordenada y del punto: "))

# Variables
distancia = ((punto_x - centro_x) ** 2 + (punto_y  - centro_y) ** 2) ** 1/2

# Calculo de posicion
if distancia < radio:
    print("Dentro")
elif distancia > radio:
    print("Fuera")
else:
    print("Justo")
"""

"""
# Input
numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
numero3 = int(input("Numero 3: "))

# Solucion con instrucciones if anidadas
if numero1 > numero2:
    if numero1 > numero3:
        print(numero1, "es el mayor")
    if numero3 > numero1:
        print(numero3, "es el mayor")

if numero2 > numero1:
    if numero2 > numero3:
        print(numero2, "es el mayor")
    if numero3 > numero2:
        print(numero3, "es el mayor")

# Solucion con condiciones complejas
if numero1 > numero2 and numero1 > numero3:
    print(numero1, "es el mayor")
if numero2 > numero1 and numero2 > numero3:
    print(numero2, "es el mayor")
if numero3 > numero1 and numero3 > numero2:
    print(numero3, "es el mayor")
"""

"""
# Input
lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))

# Determinar hipotenusa y determinante
if lado1 > lado2 and lado1 > lado3:
    hipotenusa = lado1
    determinante = lado2 ** 2 + lado3 ** 2
elif lado2 > lado1 and lado2 > lado3:
    hipotenusa = lado2
    determinante = lado1 ** 2 + lado3 ** 2
else:
    hipotenusa = lado3
    determinante = lado1 ** 2 + lado2 ** 2

# Determinar tipo de triangulo
if determinante > hipotenusa ** 2:
    print("El triangulo es acutangulo")
elif determinante < hipotenusa ** 2:
    print("El triangulo es obtusangulo")
else:
    print("El triangulo es rectangulo")
"""

"""
# Input
distancia = int(input("Ingrese distancia: "))
punto_x = abs(int(input("Ingrese x: ")))
punto_y = abs(int(input("Ingrese y: ")))

# Determinar area de los cuadrados
lado1 = distancia
lado2 = 2 * distancia
lado3 = 3 * distancia
lado4 = 4 * distancia

# Determinar en que area cayo el disparo
if punto_x <= lado1 and punto_y <= lado1:
    print("Area 1")
elif punto_x <= lado2 and punto_y <= lado2:
    print("Area 2")
elif punto_x <= lado3 and punto_y <= lado3:
    print("Area 3")
elif punto_x <= lado4 and punto_y <= lado4:
    print("Area 4")
else:
    print("Fuera del area")
"""

# Input
fila_alfil = int(input("Fila alfil: "))
columna_alfil = int(input("Columna alfil: "))
fila_torre = int(input("Fila torre: "))
columna_torre = int(input("Columna torre: "))

# Determinar captura
if fila_torre == fila_alfil or columna_torre == columna_alfil:
    print("Torre captura")
elif abs(fila_alfil - fila_torre) == abs(columna_alfil - columna_torre):
    print("Alfil captura")
else:
    print("Ninguna captura")
