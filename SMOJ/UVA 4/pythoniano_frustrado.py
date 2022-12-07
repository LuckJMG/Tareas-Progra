# Input
patience = int(input())

# Variables
no_count = 0
yes_count = 0
power = True

# Main Loop
while power:
    # Input
    punch = input()

    # Check if punched
    if punch == "si":
        yes_count += 1
        patience -= 1
        no_count = 0
    elif punch == "no":
        no_count += 1
        yes_count = 0

    # Check conditions
    if patience == 0 or yes_count == 3:
        print("Aplicando correctivo avalado por las autoridades de esta gran nación. ¡¡ PSSSST PSSSST !!")
        power = False
    elif no_count == 5:
        print("(8) Duérmete pythoncito, duérmete ya, que viene el robotrón y te rociara. (8)")
        power = False
