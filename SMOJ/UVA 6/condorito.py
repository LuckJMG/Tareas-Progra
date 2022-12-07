# Input
PHRASE = input()

# Constants
WORD_COST = 100
LARGE_FACTOR = 1.5

# Variables
words = 0
length = 0
big_word = 0

# Format phrase
if PHRASE[-1] != ' ':
    formatted_phrase = PHRASE + ' '
else:
    formatted_phrase = PHRASE

# Count words
for letter in formatted_phrase:
    if letter == ' ':
        # Check largest word
        if length > big_word:
            big_word = length

        length = 0
        words += 1
    else:
        length += 1

# Calculate total cost
total_cost = int(words * WORD_COST + (big_word * LARGE_FACTOR))

# Output
print(f"Su mensaje vale: $ {total_cost}")
