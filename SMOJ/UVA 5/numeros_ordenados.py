def ordenado(n):
    # Variables
    tmp = n
    length = 0

    # Calculate length
    while tmp > 0:
        tmp //= 10
        length += 1

    # Check if is not an ordered number
    while length > 0:
        digit1 = n % 10
        n //= 10
        digit2 = n % 10

        if digit2 > digit1:
            return False

        length -= 1

    return True

# Test cases
print(ordenado(579), ordenado(67889), ordenado(9876))
