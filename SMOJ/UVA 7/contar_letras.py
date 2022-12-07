def contar_letras(text):
    # Constants
    AVAILABLE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    # Variables
    text_letters = []
    letter_count = []

    # Determine letters of the text without repetition
    for letter in text:
        if letter not in text_letters and letter in AVAILABLE_LETTERS:
            text_letters.append(letter)

    text_letters.sort()

    # Count each letter of the text
    for letter in text_letters:
        count = 0

        for char in text:
            if letter == char:
                count += 1

        letter_count.append([letter, count])

    return letter_count
