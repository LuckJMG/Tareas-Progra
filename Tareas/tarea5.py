# Imports
from random import randint
from turtle import Screen, Turtle

# Funcion (1)
def cantidad_raciones(estacion, temperatura, probabilidad_lluvia):
    # Calcular cantidad de raciones a hacer
    if estacion == "verano":
        if probabilidad_lluvia < 0.5:
            cantidad = 3 * temperatura + 20 * (1 - probabilidad_lluvia)
        else:
            cantidad = 2 * temperatura + 20 * (1 - probabilidad_lluvia)

    elif estacion == "otoño":
        if probabilidad_lluvia < 0.5:
            cantidad = 2 * temperatura + 15 * (1 - probabilidad_lluvia)
        else:
            cantidad = temperatura + 10 * (1 - probabilidad_lluvia)

    elif estacion == "invierno":
        if probabilidad_lluvia < 0.5:
            cantidad = 0.5 * temperatura + 5 * (1 - probabilidad_lluvia)
        else:
            cantidad = 0.5 * temperatura

    elif estacion == "primavera":
        if probabilidad_lluvia < 0.5:
            cantidad = temperatura + 15 * (1 - probabilidad_lluvia)
        else:
            cantidad = temperatura + 10 * (1 - probabilidad_lluvia)

    return round(cantidad)


# Funcion (2)
def regalo_raciones(estacion, raciones):
    # Calcular raciones a regalar
    if estacion == "verano":
        regalo = randint(1, raciones // 10)

    elif estacion == "otoño":
        regalo = randint(1, raciones // 8)

    elif estacion == "invierno":
        regalo = randint(1, raciones // 5)

    elif estacion == "primavera":
        regalo = randint(1, raciones // 7)

    return regalo


# Funcion (3)
def dia_semana(indicador):
    # Convertir indicador en su dia de la semana correspondiente
    if indicador == 1:
        dia = "Lunes"
    elif indicador == 2:
        dia = "Martes"
    elif indicador == 3:
        dia = "Miercoles"
    elif indicador == 4:
        dia = "Jueves"
    elif indicador == 5:
        dia = "Viernes"
    elif indicador == 6:
        dia = "Sabado"
    elif indicador == 7:
        dia = "Domingo"

    return dia


# Funcion (4)
def dibujar_barra(tortuga, x, y, valor):
    # Variables
    ancho = 75
    alto = valor * 3

    # Ir hacia las coordenadas indicadas
    tortuga.penup()
    tortuga.goto(x, y)

    # Dibujar la barra segun lo indicado
    tortuga.pendown()
    tortuga.forward(ancho)
    tortuga.left(90)
    tortuga.forward(alto)
    tortuga.left(90)
    tortuga.forward(ancho)
    tortuga.left(90)
    tortuga.forward(alto)
    tortuga.penup()

    # Escribir el valor de la barra
    tortuga.goto(x + (ancho / 2.5), y + alto)
    tortuga.write(valor)
    tortuga.home()

    # Calcular el area de la barra (en pasos tortuga)
    area = ancho * alto

    return area


# Funcion (5)
def escribir_leyenda(tortuga, x, y, leyenda):
    # Ir hacia las coordenadas indicadas
    tortuga.penup()
    tortuga.goto(x + 20, y - 20)

    # Escribir leyenda
    tortuga.write(leyenda)
    tortuga.home()

    return leyenda


# Programa
# Variables
dia = 1
x_offset = -260
y_offset = -200

# Iniciacion programa
pantalla = Screen()
tortuga = Turtle()
tortuga.screen.title("IWI131: *** El Kiwi del Mote con Huesillos ***")
tortuga.speed(100)
print("*** El Kiwi del Mote con Huesillos ***")

# Input
estacion = input("Estación: ")

while dia <= 7:
    print("Dia", dia)

    # Input del dia
    temperatura = int(input("Pronóstico de temperatura: "))
    probabilidad_lluvia = float(input("Probabilidad de lluvia: "))

    # Calcular raciones a hacer y a regalar
    raciones = cantidad_raciones(estacion, temperatura, probabilidad_lluvia)
    regalo = regalo_raciones(estacion, raciones)

    print("Se producirá", raciones, "raciones; se regalará", regalo, "para promoción")

    # Dibujar barras y leyendas
    dibujar_barra(tortuga, x_offset + (dia - 1) * 75, y_offset, raciones)
    dibujar_barra(tortuga, x_offset + (dia - 1) * 75, y_offset, regalo)
    escribir_leyenda(tortuga, x_offset + (dia - 1) * 75, y_offset, dia_semana(dia))

    dia += 1

# Finalizacion programa
tortuga.goto(1000, 1000)
pantalla.exitonclick()
