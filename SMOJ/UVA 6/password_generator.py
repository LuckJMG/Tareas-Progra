# Input
PHRASE = input()

# Constants
CONSONANTS = "BCDFGHJKLMNPQRSTVWXYZ"

# Variables
password = ""
first_letter = True

# Create password
for char in PHRASE.upper():
    # First letter in minus
    if first_letter and char in CONSONANTS:
        password += char.lower()
        first_letter = False

    # Change vocals to numbers (excluding u)
    elif char == 'A':
        password += '4'
    elif char == 'E':
        password += '3'
    elif char == 'I':
        password += '1'
    elif char == 'O':
        password += '0'
    elif char == ' ':
        password += '_'

    # Add other characters, and if is a letter in upper
    else:
        password += char

# Check if we put a '*' or a '!'
if len(password) % 2 == 0:
    password += '*'
else:
    password += '!'

# Output
print(password)
