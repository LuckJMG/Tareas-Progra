# Input
binary_number = int(input())

# Convertion to base 10
digit1 = binary_number % 10
digit2 = (binary_number // 10) % 10
digit3 = binary_number // 100
number = digit1 + digit2 * 2 + digit3 * 4

# Output
print(number)
