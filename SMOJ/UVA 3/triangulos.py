# Input
lado1 = float(input())
lado2 = float(input())
lado3 = float(input())

# Output
if lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1 or lado1 + lado2 <= lado3:
    print("No es triangulo")
elif lado1 == lado2 == lado3:
    print("Triangulo equilatero")
elif (lado1 == lado3 or lado2 == lado3 or lado1 == lado2) and lado1**2 + lado3**2 == lado2**2:
    print("Triangulo isosceles rectangulo")
elif lado1 == lado3 or lado2 == lado3 or lado1 == lado2:
    print("Triangulo isosceles")
elif lado1 != lado3 != lado2 and lado1**2 + lado3**2 == lado2**2:
    print("Triangulo escaleno rectangulo")
else:
    print("Triangulo escaleno")
