def calculate_median(numbers):
    # Variables
    tmp = list(numbers)
    tmp.sort()

    # Calculate median
    if len(tmp) % 2 != 0:
        median = (len(tmp) - 1) // 2
        median = tmp[median]
    else:
        median = (len(tmp) // 2) - 1
        median = (tmp[median] + tmp[median + 1]) / 2.0

    return median

# Variables
numbers = []
quantity = int(input())

# Input
while quantity > 0:
    numbers.append(int(input()))
    quantity -= 1

# Output
print(round(calculate_median(numbers) * 2))
