# Constants
CHECK_WORD = "pythonia"
PHRASE = input().lower()

# Variables
index_check = 0
index_phrase = 0

# Check if all letters are in the phrase
while index_check < len(CHECK_WORD) and index_phrase < len(PHRASE):
    if CHECK_WORD[index_check] == PHRASE[index_phrase]:
        index_check += 1

    index_phrase += 1

# Output
if index_check == len(CHECK_WORD):
    print("SI")
else:
    print("NO")
