def decodificar(bits):
    # Variables
    index = 0
    number = 0

    # Convert binary to decimal
    for bit in bits:
        number += int(bit) * 2 ** (len(bits) - 1 - index)
        index += 1

    return number
