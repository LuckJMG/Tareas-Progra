"""
# Variables
cero = False
contador = 0
pares = 0
impares = 0

# Ciclo principal
while not cero:
    # Reseteo de variables
    digito = 0
    numero = 0

    # Convertir byte a base decimal
    while digito < 8:
        bit = int(input())
        numero += bit * (2 ** digito)
        digito += 1

    # Output
    print("El byte es:", numero)

    # Sumar a contadores correspondientes
    contador += 1
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Determinar si es cero para finalizar el programa
    if numero == 0:
        cero = True

# Output
print("Total de bytes ingresados:", contador)
print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)
"""

# Variables
equipaje = True
carga_total = 0
costo_total = 0
cantidad_bultos = 0
bulto_mas_pesado = 0

# Mientras quepa equipaje
while equipaje:
    # Input
    bulto = int(input())

    # Rechazar bultos mayores de 500 kg
    if 0 < bulto <= 500:

        # Comprobar si caben mas bultos
        if carga_total + bulto > 18000:
            equipaje = False

        else:
            cantidad_bultos += 1
            carga_total += bulto

            # Determinar cual es el bulto mas pesado
            if bulto > bulto_mas_pesado:
                bulto_mas_pesado = bulto

            # Calcular costo total
            if 0 < bulto <= 25:
                costo_total += bulto * 1000

            elif 26 <= bulto <= 300:
                costo_total += bulto * 1500

            elif 301 <= bulto <= 500:
                costo_total += bulto * 2000

    else:
        print("Bulto excede peso!")

# Output
print("Numero total de bultos:", cantidad_bultos)
print("Bulto más pesado pesa:", bulto_mas_pesado)
print("Peso promedio de los bultos:", round(carga_total / cantidad_bultos))
print("Ingreso total por concepto de carga:", costo_total)
