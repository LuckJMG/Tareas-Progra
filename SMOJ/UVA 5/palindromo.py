def es_palindromo():
    pass

def largo_palindromo(number):
    # Variables
    length = 0

    # Check if number is a palindromo
    if es_palindromo(number):
        tmp = number

        # Determine length
        while tmp > 0:
            tmp //= 10
            length += 1

    return length
