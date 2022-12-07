def divisor(n1, n2):
    min_divisor = 2

    while min_divisor < n1 and min_divisor < n2:
        if n1 % min_divisor == 0 and n2 % min_divisor == 0:
            return min_divisor
        min_divisor += 1

    return False

print(divisor(2, 4), divisor(4, 8))
