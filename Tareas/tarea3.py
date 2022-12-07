from random import randint

# Constantes
entrada_viernes = 50000
entrada_sabado = 75000
entrada_domingo = 60000
entrada_todos_dias = 150000
descuento_dos_dias = 0.8  # Descuento de un 20%
extra_vip = 1.4  # Carga de un 40%
precio_estacionamiento = 10000
descuento_banco_pythonea = 0.7  # Descuento de un 30%
descuento_sorteo = 1 - (randint(0, 10) / 100)  # Descuento desde un 0% a un 10%

# Inicio cotizacion
print("Bienvenido a LolaPYlooza")
print("------- Sistema de cotización de entradas -------------\n")

# Dias
cantidad_dias = int(input("Cantidad de dias: "))
if cantidad_dias == 1:
    # Caso 1 dia
    dia1 = input("Día que desea asistir: ")
    if dia1 == "Viernes":
        print("Día 1:", dia1, "Valor $", entrada_viernes)
        pago_total = entrada_viernes
    elif dia1 == "Sábado":
        print("Día 1:", dia1, "Valor $", entrada_sabado)
        pago_total = entrada_sabado
    elif dia1 == "Domingo":
        print("Día 1:", dia1, "Valor $", entrada_domingo)
        pago_total = entrada_domingo
elif cantidad_dias == 2:
    # Caso 2 dias
    # Dia 1
    dia1 = input("Día 1 que desea asistir: ")
    if dia1 == "Viernes":
        entrada_dia1 = entrada_viernes
    elif dia1 == "Sábado":
        entrada_dia1 = entrada_sabado
    elif dia1 == "Domingo":
        entrada_dia1 = entrada_domingo

    # Dia 2
    dia2 = input("Día 2 que desea asistir: ")
    if dia2 == "Viernes":
        entrada_dia2 = entrada_viernes
    elif dia2 == "Sábado":
        entrada_dia2 = entrada_sabado
    elif dia2 == "Domingo":
        entrada_dia2 = entrada_domingo

    print("Día 1:", dia1, "Valor $", entrada_dia1)
    print("Día 2:", dia2, "Valor $", entrada_dia2)
    pago_total = entrada_dia1 + entrada_dia2
    print("Descuento por días:", round(pago_total * (1 - descuento_dos_dias)))
    pago_total = pago_total * descuento_dos_dias
else:
    # Caso todos los dias
    dia1 = "Todos los días"
    print("Total a pagar por todos los días $", entrada_todos_dias)
    pago_total = entrada_todos_dias

# VIP
vip = int(input("Ingrese 1 si desea entrada vip: "))
if vip == 1:
    # Carga VIP
    print("Recargo por entrada VIP $", round(pago_total * (extra_vip - 1)))
    pago_total = pago_total * extra_vip
else:
    # Estacionamiento
    estacionamiento = int(input("Ingrese 1 se desea estacionamiento: "))
    print("Recargo por estacionamiento $", precio_estacionamiento * cantidad_dias)
    pago_total = pago_total + (precio_estacionamiento * cantidad_dias)

# Banco Pythonea
banco_pythonia = int(input("Ingrese 1 si tiene tarjeta Banco Pythonia: "))
if banco_pythonia == 1:
    # Descuento Banco Pythonea
    print("Descuento por cliente Bco Pythonia: $", round(pago_total * (1 - descuento_banco_pythonea)))
    pago_total = pago_total * descuento_banco_pythonea
else:
    # Descuento sorteo
    print("Descuento por sorteo:", round((1 - descuento_sorteo) * 100), "% equivalente a", round(pago_total * (1 - descuento_sorteo)))
    pago_total =  pago_total * descuento_sorteo

# Pago total y final de cotizacion
print("Total a pagar: $", round(pago_total))
