# Constants
LOWER_ABECEDARY = "abcdefghijklmnopqrstuvwxyz"
UPPER_ABECEDARY = LOWER_ABECEDARY.upper()

# Variables
phrase = input()
displacement = int(input())
encrypted_phrase = ""
index = 0
tmp = 0

while displacement >= len(LOWER_ABECEDARY):
    displacement -= len(LOWER_ABECEDARY)

# Encrypt phrase
for letter in phrase:
    tmp = displacement

    if letter in LOWER_ABECEDARY:
        index = LOWER_ABECEDARY.index(letter)

        # Check if displacement is out of bonds
        if index + displacement >= len(LOWER_ABECEDARY):
            tmp =  displacement + index - len(LOWER_ABECEDARY)
            index = 0

        # Encrypt
        encrypted_phrase += LOWER_ABECEDARY[index + tmp]

    elif letter in UPPER_ABECEDARY:
        index = UPPER_ABECEDARY.index(letter)

        # Check if displacement is out of bonds
        if index + displacement >= len(UPPER_ABECEDARY):
            tmp =  displacement + index - len(UPPER_ABECEDARY)
            index = 0

        # Encrypt
        encrypted_phrase += UPPER_ABECEDARY[index + tmp]

    else:
        encrypted_phrase += letter

# Output
print(encrypted_phrase)
