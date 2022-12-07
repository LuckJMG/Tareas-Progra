# Variables
previous_number = 0
count = 1
attempts = 0

# Main Loop
while count + 1 != previous_number:
    # Input
    number = int(input())

    # Comprobate number
    if number == previous_number:
        count += 1
    else:
        count = 0

    attempts += 1
    previous_number = number

# Output
print(attempts)
