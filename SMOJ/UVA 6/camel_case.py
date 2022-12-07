# Variables
phrase = input()
words = 1

# Separate with Upper Case letters
for letter in phrase:
    if '@' < letter < '[':
        words += 1

# Output
print(words)
