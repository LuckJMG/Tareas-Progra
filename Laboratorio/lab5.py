def cantidad_soluciones(a, b, c):
    discriminante = b ** 2 - 4 * a * c

    if discriminante > 0:
        soluciones = 2
    elif discriminante == 0:
        soluciones = 1
    else:
        soluciones = 0

    return soluciones

from math import pi

def radianes(grados):
    radian = grados * pi / 180
    return radian
