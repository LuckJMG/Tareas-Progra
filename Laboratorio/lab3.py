"""
numbers = [1, 4, 2, 7, 10, -3, 5, 13, 50]

def number_in_list(number, number_list):
    index = len(number_list) - 1

    while index != 0:
        if number_list[index] == number:
            print(f"{number} esta en la lista {number_list}")
            return True
        index -= 1

    print(f"{number} no esta en la lista {number_list}")
    return False

number_in_list(2, numbers)
"""

vector = [1, 4, 7, 2]
largo = len(vector)
dato = 2

posicion = 0
salida = False

while posicion < largo:
    if vector[posicion] == dato:
        salida = True
    posicion = posicion + 1
print(salida)
