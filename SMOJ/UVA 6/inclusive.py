# Input
WORD = input()

# Constants
VOCALS = "aiou"

# Variables
index = 0
inclusive_word = ""

# Replace last vocal
while index < len(WORD):
    if (index == len(WORD) - 1 or index == len(WORD) - 2) and WORD[index] in VOCALS:
        inclusive_word += 'e'
    else:
        inclusive_word += WORD[index]
    index += 1

# Output
print(inclusive_word)
