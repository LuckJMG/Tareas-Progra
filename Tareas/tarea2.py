from math import cos, pi, sin

# Input
print("*** Kiwi ayuda al Coyote ***\nIngrese los siguientes datos:\n")
coordenada_x_correcaminos = float(input("Coordenada x del Correcaminos: "))
velocidad_lanzamiento = float(input("Velocidad inicial de lanzamiento (kms/h): "))
angulo_lanzamiento = float(input("Ángulo de lanzamiento, expresado (grados): "))
coordenada_x_lanzamiento = float(input("Coordenada x del lanzamiento (Coyote): "))
coordenada_y_lanzamiento = float(input("Coordenada y del lanzamiento (Coyote): "))

# Conversion de unidades
velocidad_lanzamiento = velocidad_lanzamiento * 10 / 36 # Conversion de km/h a m/s
angulo_lanzamiento = angulo_lanzamiento * pi / 180 # Conversion de grados a radianes
velocidad_x = velocidad_lanzamiento * cos(angulo_lanzamiento)
velocidad_y = velocidad_lanzamiento * sin(angulo_lanzamiento)

# Tiempo y posicion de impacto
discriminante = (velocidad_y ** 2) - (4 * -4.9 * coordenada_y_lanzamiento)
tiempo_impacto = (velocidad_y + (discriminante ** (1/2))) / 9.8
posicion_impacto = coordenada_x_lanzamiento + velocidad_x * tiempo_impacto

# Calculo posicion en instantes predeterminados
posicion_x_t1 = coordenada_x_lanzamiento + velocidad_x * 0.1
posicion_y_t1 = coordenada_y_lanzamiento + velocidad_y * 0.1 - 0.049
posicion_x_t2 = coordenada_x_lanzamiento + velocidad_x * 0.2
posicion_y_t2 = coordenada_y_lanzamiento + velocidad_y * 0.2 - 0.196
posicion_x_t3 = coordenada_x_lanzamiento + velocidad_x * 0.3
posicion_y_t3 = coordenada_y_lanzamiento + velocidad_y * 0.3 - 0.441
posicion_x_t4 = coordenada_x_lanzamiento + velocidad_x * (tiempo_impacto - 0.3)
posicion_y_t4 = coordenada_y_lanzamiento + velocidad_y * (tiempo_impacto - 0.3) + (-4.9 * ((tiempo_impacto - 0.3) ** 2))
posicion_x_t5 = coordenada_x_lanzamiento + velocidad_x * (tiempo_impacto - 0.2)
posicion_y_t5 = coordenada_y_lanzamiento + velocidad_y * (tiempo_impacto - 0.2) + (-4.9 * ((tiempo_impacto - 0.2) ** 2))
posicion_x_t6 = coordenada_x_lanzamiento + velocidad_x * (tiempo_impacto - 0.1)
posicion_y_t6 = coordenada_y_lanzamiento + velocidad_y * (tiempo_impacto - 0.1) + (-4.9 * ((tiempo_impacto - 0.1) ** 2))

# Calculo distancia de fallo
distancia_fallo = posicion_impacto - coordenada_x_correcaminos

# Output conversiones
print("\nValores ajustados:")
print("Velocidad =", round(velocidad_lanzamiento, 5), "m/s")
print("Ángulo de lanzamiento =", round(angulo_lanzamiento, 5), "radianes")
print("vx =", round(velocidad_x, 5), "m/s")
print("vy =", round(velocidad_y, 5),"m/s")

# Output mediciones
print("\nEvaluación del lanzamiento:")
print("En tiempo 0 el proyectil se encuentra en:", round(coordenada_x_lanzamiento, 5), round(coordenada_y_lanzamiento, 5))
print("En tiempo 0.1 el proyectil se encuentra en:", round(posicion_x_t1, 5), round(posicion_y_t1, 5))
print("En tiempo 0.2 el proyectil se encuentra en:", round(posicion_x_t2, 5), round(posicion_y_t2, 5))
print("En tiempo 0.3 el proyectil se encuentra en:", round(posicion_x_t3, 5), round(posicion_y_t3, 5))
print("En tiempo", round(tiempo_impacto - 0.3, 5), "el proyectil se encuentra en:", round(posicion_x_t4, 5), round(posicion_y_t4, 5))
print("En tiempo", round(tiempo_impacto - 0.2, 5), "el proyectil se encuentra en:", round(posicion_x_t5, 5), round(posicion_y_t5, 5))
print("En tiempo", round(tiempo_impacto - 0.1, 5), "el proyectil se encuentra en:", round(posicion_x_t6, 5), round(posicion_y_t6, 5))
print("Proyectil impacta en coordenada x:", round(posicion_impacto, 5))
print("Se falló al Correcaminos por:", round(distancia_fallo, 5))
