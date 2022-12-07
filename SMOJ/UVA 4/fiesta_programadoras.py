# Variables
count = 0

# Main Loop
while count != 5:
    # Input
    name = input()

    # Comprobate access
    if name == "Ada" or name == "Joan" or  name == "Katherine" or name == "Alexandra" or name == "Barbarita":
        count += 1
        print(f"{count} Bienvenida {name} !")
    else:
        print("Acceso denegado X")

# Output
print("Aforo completo")
