from random import randint

# Input
votos_a = randint(0, 10000)
votos_b = randint(0, 10000)
votos_c = randint(0, 10000)
votos_d = randint(0, 10000)

# Calcular votos
votos_canciones = [votos_a, votos_b, votos_c, votos_d]
votos_totales = sum(votos_canciones)
max_votos = max(votos_canciones)

# Calcular porcentajes
votos_a = votos_a / votos_totales
votos_b = votos_b / votos_totales
votos_c = votos_c / votos_totales
votos_d = votos_d / votos_totales

# Output
if votos_a > votos_b and votos_a > votos_c and votos_a > votos_d:
    print(f"La cancion A es la ganadora con {max_votos}")
elif votos_b > votos_a and votos_b > votos_c and votos_b > votos_d:
    print(f"La cancion B es la ganadora con {max_votos}")
elif votos_c > votos_a and votos_c > votos_b and votos_c > votos_d:
    print(f"La cancion C es la ganadora con {max_votos}")
else:
    print(f"La cancion D es la ganadora con {max_votos}")

print(f"Porcentaje votos cancion A {votos_a:.2%}")
print(f"Porcentaje votos cancion B {votos_b:.2%}")
print(f"Porcentaje votos cancion C {votos_c:.2%}")
print(f"Porcentaje votos cancion D {votos_d:.2%}")
