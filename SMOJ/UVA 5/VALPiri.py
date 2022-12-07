def a_texto_19(numero):
    # Convert numbers between 0 and 19 to text
    if 0 <= numero < 20:
        if numero == 0:
            numero = "cero"
        elif numero == 1:
            numero = "uno"
        elif numero == 2:
            numero = "dos"
        elif numero == 3:
            numero = "tres"
        elif numero == 4:
            numero = "cuatro"
        elif numero == 5:
            numero = "cinco"
        elif numero == 6:
            numero = "seis"
        elif numero == 7:
            numero = "siete"
        elif numero == 8:
            numero = "ocho"
        elif numero == 9:
            numero = "nueve"
        elif numero == 10:
            numero = "diez"
        elif numero == 11:
            numero = "once"
        elif numero == 12:
            numero = "doce"
        elif numero == 13:
            numero = "trece"
        elif numero == 14:
            numero = "catorce"
        elif numero == 15:
            numero = "quince"
        elif numero == 16:
            numero = "dieciseis"
        elif numero == 17:
            numero = "diecisiete"
        elif numero == 18:
            numero = "dieciocho"
        else:
            numero = "diecinueve"

        return numero

    else:
        return None

def a_texto_99(numero):
    # Comprobate if is in the admited cases
    if 0 <= numero < 100:
        # Comprobate if the case is in the a_texto_19 function
        if 0 <= numero < 20:
            return a_texto_19(numero)

        # Separate number in its digits
        units = numero % 10
        tens = numero // 10

        # Convert units into text
        units = a_texto_19(units)

        # Convert tens into text
        if tens == 2:
            tens = "veinte"
        elif tens == 3:
            tens = "treinta"
        elif tens == 4:
            tens = "cuarenta"
        elif tens == 5:
            tens = "cincuenta"
        elif tens == 6:
            tens = "sesenta"
        elif tens == 7:
            tens = "setenta"
        elif tens == 8:
            tens = "ochenta"
        elif tens == 9:
            tens = "noventa"

        # If number is between 21 and 29
        if tens == "veinte" and units != "cero":
            return f"veinti{units}"

        # If number does not have units
        elif units == "cero":
            return tens

        else:
            return f"{tens} y {units}"

    # Wrong inputs
    else:
        if numero < 0:
            return "Lo siento, hoy solo tengo vibras positivas"
        elif 100 <= numero < 1000:
            return "Solo proceso hasta 99"
        else:
            return "Es broma?"

# Test cases
print(a_texto_99(-12), a_texto_99(69), a_texto_99(22), a_texto_99(13))
