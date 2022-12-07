"""
# Input
friend1 = int(input())
friend2 = int(input())
friend3 = int(input())

# Calculate quote
quote = (friend1 + friend2 + friend3) / 3

# Output
print("First friend debt:", quote - friend1)
print("Second friend debt:", quote - friend2)
print("Third friend debt:", quote - friend3)


# Input
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# Calculate distance
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

# Output
print("The distance is:", distance)


# Input
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

# Calculate distance
distance1 = abs(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2))
distance2 = abs(((x3 - x1) ** 2 + (y3 - y1) ** 2) ** (1/2))
distance3 = abs(((x3 - x2) ** 2 + (y3 - y2) ** 2) ** (1/2))
perimeter = distance1 + distance2 + distance3

# Output
print("The perimeter is:", perimeter)


# Input
seconds = int(input("Amount of second: "))

# Calculate days, hours and minutes
days = seconds // 86400
hours = (seconds % 86400) // 3600
minutes = ((seconds % 86400) % 3600) // 60

# Output
print(f"{seconds}[s] => {days} days, {hours} hours, {minutes} minutes")


from math import pi

# Input
radio = float(input())
height = float(input())

# Calculate cylinder
base_area = pi * radio**2
side_area = 2 * pi * radio * height
total_area = base_area*2 + side_area
volume = base_area * height

# Output
print(f"The cylinder with {radio} radio and {height} height, has a base area of {base_area}")


# Input
peso = float(input("Ingrese su peso [lb]: "))
altura = float(input("Ingrese su altura [pies]: "))

# Conversion a SI
peso = peso * 0.45359237
altura = (altura // 1) * 0.3048 + (altura % 1) * 0.0254

# Calcular IMC
imc = peso / (altura**2)

# Output
print(f"Tu IMC es de {imc}")
"""

# Input
from math import pi, sin


lado_a = float(input())
lado_b = float(input())
angulo = float(input())

# Conversion angulo a radianes
angulo = angulo * pi / 180

# Calcular area
area = lado_a * lado_b * sin(angulo) / 2

# Output
print(f"El area del triangulo es {area}")
