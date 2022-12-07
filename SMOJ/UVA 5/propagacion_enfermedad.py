from math import factorial

def estima_contagios(t):
    # Variables
    count = 0
    infected = 0

    # Calculate amount of infected people
    while count <= 100:
        infected += t ** count / factorial(count)
        count += 1

    infected = round(infected)
    return infected

print(estima_contagios(0), estima_contagios(10))
