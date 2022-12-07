def palindromo(numero):
    # Variables
    tmp = numero
    largo = 0
    invertido = 0
    contador = 1

    # Calcular largo del numero
    while tmp > 0:
        tmp //= 10
        largo += 1

    # Invertir el numero
    tmp = numero
    while contador <= largo:
        digito = tmp % 10
        tmp //= 10
        invertido += digito * (10 ** (largo - contador))
        contador += 1

    # Comprobar si es palindromo
    if numero == invertido:
        es_palindromo = True
    else:
        es_palindromo = False

    return es_palindromo

print(palindromo(12231))
