# Constantes
MAN_RUN_CALORIES = 30
MAN_BIKE_CALORIES = 25
MAN_WEIGHTS_CALORIES = 37
WOMAN_RUN_CALORIES = 32
WOMAN_BIKE_CALORIES = 22
WOMAN_WEIGHTS_CALORIES = 30

# Input
exercise = input()
genre = input()
minutes = int(input())

# Calcule burned calories
if genre == "Hombre":
    if exercise == "Correr":
        burned_calories = minutes * MAN_RUN_CALORIES
    elif exercise == "Bici":
        burned_calories = minutes * MAN_BIKE_CALORIES
    elif exercise == "Pesas":
        burned_calories = minutes * MAN_WEIGHTS_CALORIES
elif genre == "Mujer":
    if exercise == "Correr":
        burned_calories = minutes * WOMAN_RUN_CALORIES
    elif exercise == "Bici":
        burned_calories = minutes * WOMAN_BIKE_CALORIES
    elif exercise == "Pesas":
        burned_calories = minutes * WOMAN_WEIGHTS_CALORIES

# Output
print(burned_calories)
