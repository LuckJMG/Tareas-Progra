"""
# Input
multiplo1 = int(input())
multiplo2 = int(input())

# Variables
producto = 0

# Calculo producto
while multiplo2 > 0:
    producto += multiplo1
    multiplo2 -= 1

# Output
print(producto)
"""

"""
# Input
dividendo = int(input())

# Variables
divisor = 1
suma = 0

# Calcular sumatoria
while divisor <= dividendo:
    if dividendo % divisor == 0:
        suma += divisor
    divisor += 1

# Output
print(suma)
"""

"""
# Input
n = int(input("Ingrese n: "))

# Variables
i = 0
j = 1

# Output
while i < n:
    print(j + i)
    j += i
    i += 1
"""

"""
# Input
altura = int(input("Altura: "))
ancho = int(input("Ancho: "))

# Variables
i = 1

# Output
while i <= altura:
    j = 1
    while j <= ancho:
        print("*", end="")
        j += 1
    print("")
    i += 1
"""

"""
# Input
altura = int(input("Altura: "))

# Variables
i = 1

# Output
while i <= altura:
    print("*" * i)
    i += 1
"""
# Input
lado = int(input("Lado: "))

# Variables
i = 1
suma = "*" * lado

# Output
while i <= lado:
    print(" " * (lado - i) + suma)
    suma = suma + "**"
    i += 1

i -= 1

while i > 1:
    print(" " * (lado - i + 1) + "**" * i)
    i -= 1

