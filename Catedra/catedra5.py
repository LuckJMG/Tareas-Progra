"""
# Variables
cantidad_datos = int(input("Cuantos valores ingresara? "))
i = 1
mayor = float(input("Valor 1: "))
menor = mayor

# Ciclo principal
while i < cantidad_datos:
    valor = float(input(f"Valor {i + 1}: "))

    if valor > mayor:
        mayor = valor
    elif valor < menor:
        menor = valor

    i += 1

# Output
print(f"El rango es: {round((mayor - menor), 2)}")
"""

"""
# Variables
i = 1
euler = 1
anterior = 0
factorial = 1

# Ciclo principal
while euler - anterior > 0.0001:
    factorial *= i
    anterior = euler
    euler += 1 / factorial
    i += 1
    print(euler)
"""
