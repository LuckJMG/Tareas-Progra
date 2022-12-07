# Constants
code = int(input())

# Variables
tmp = code
odec = 0
length = 0
i = 0

# Calculate length of the code
while tmp > 0:
    tmp //= 10
    length += 1

# Reset temporal variable
tmp = code

# Invert code
while tmp > 0:
    i += 1
    odec += (tmp % 10) * (10 ** (length - i))
    tmp //= 10

# Check code
if code == odec:
    print("Puede ingresar =)")
else:
    print("Alto ahí, deberá registrarse en las 11 porterías dejando su nombre, rut y firma en cada una de ellas, si lo hace bien, le daremos la bienvenida =)")
