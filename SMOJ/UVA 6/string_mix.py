# Input
PHRASE1 = input()
PHRASE2 = input()

# Determine largest and shortest phrase
if len(PHRASE1) >= len(PHRASE2):
    large_phrase = PHRASE1.lower()
    short_phrase = PHRASE2.upper()
else:
    large_phrase = PHRASE2.lower()
    short_phrase = PHRASE1.upper()

# Variables
step = len(large_phrase) // len(short_phrase)
phrase_mix = ""
index = 0
count = 0

# Mix phrases
for char in large_phrase:
    phrase_mix += char
    count += 1

    if count == step:
        count = 0
        phrase_mix += short_phrase[index]
        index += 1

# Output
print(phrase_mix)
