# Input
o_number = int(input())

# Variables
number = o_number
length = 0
sum = 0
digit = 0

# Determine the length of the number
while number != 0:
    number //= 10
    length += 1

number = o_number

# Comprobate if is an Armstrong number
for i in range(1, length + 1):
    digit = number % 10
    number = number // 10
    sum += digit ** length

if sum == o_number:
    print("Es de Armstrong")
else:
    print("No es de Armstrong")
