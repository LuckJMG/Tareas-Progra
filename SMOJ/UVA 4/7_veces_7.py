# Variables
seven_count = 0
attempts = 0
count = 0

# Main Loop
while seven_count < 7:
    # Input
    number = int(input())

    # Check number
    if number == 7:
        attempts += 1
        seven_count +=1
    elif 1 <= number <= 10:
        attempts += 1
    else:  # Out of range
        print("INTENTE NUEVAMENTE:")

# Calculate percentage
percentage = round((7 / attempts) * 100, 1)
print(f"{percentage} %")

# Output
while count < attempts:
    print(f"{count + 1} *******")
    count += 1
