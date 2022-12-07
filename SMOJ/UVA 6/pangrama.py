# Constants
ABECEDARY = "abcdefghijklmnopqrstuvwxyz"
PHRASE = input().lower()

# Variables
pangrama = True
index = 0

# Check if all letters are in the phrase
while pangrama and index < len(ABECEDARY):
    if ABECEDARY[index] not in PHRASE:
        pangrama = False
    else:
        index += 1

# Output
if pangrama:
    print("PANGRAMA")
else:
    print("NO PANGRAMA")
