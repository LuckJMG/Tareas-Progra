# Variables
defeat = True
plays = 1

# Main loop
while defeat:
    # Input
    number_kiwi = int(input())
    number_oponent = int(input())

    if number_kiwi > number_oponent:
        print(plays)
        print("Victoria")
        defeat = False
    elif number_kiwi == number_oponent:
        print(plays)
        print("Empate")
        defeat = False

    plays += 1
