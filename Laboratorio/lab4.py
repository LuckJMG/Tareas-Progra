"""
# Input
num1 = int(input("Ingrese num: "))
num2 = int(input("Ingrese num: "))

# Variables
suma = 0

# Calculo de la suma
while num1 + 1 != num2:
    suma += num1 + 1
    num1 += 1

# Output
print(f"La suma es {suma}")
"""

# Input
n = int(input("n: "))

# Variables
i = 1
pi = 1

# Calcular aproximacion de pi
while i < n:
    if i % 2 == 0:
        pi += 1 / (2 * i + 1)
    else:
        pi -= 1 / (2 * i + 1)
    i += 1
pi *= 4

# Output
print(pi)
