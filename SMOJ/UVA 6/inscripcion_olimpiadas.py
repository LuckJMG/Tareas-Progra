# Variables
participant_number = 0
participant_list = ""
repeat = True

# Make participant list
while repeat:
    # Input
    participant = input()

    # Check if the name repeats
    if participant in participant_list:
        repeat = False

    # In other case add name to the list
    else:
        participant_number += 1
        participant_list += participant + '|'

participant = ""

# Output
for char in participant_list:
    if char != '|':
        participant += char
    else:
        print(participant)
        participant = ""

print(participant_number)
