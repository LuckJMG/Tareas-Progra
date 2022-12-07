# Constants
SIGNAL = input()

# Variables
altered_letters = 0
index = 0

# Check signal
while index < len(SIGNAL):
    # Check S of the signal
    if index % 3 == 0 or index % 3 == 2:
        if SIGNAL[index] != 'S':
            altered_letters += 1

    # Check O of the signal
    elif index % 3 == 1:
        if SIGNAL[index] != 'O':
            altered_letters += 1

    index += 1

# Output
print(altered_letters)
