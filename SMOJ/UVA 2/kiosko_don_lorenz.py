# Constants
PRICE_A = 600
PRICE_B = 300
PRICE_C = 800

# Input
product_a = int(input())
product_b = int(input())
product_c = int(input())
paid = int(input())

# Calculation
total = product_a * PRICE_A + product_b * PRICE_B +  product_c * PRICE_C
change = paid - total

# Output
print(f"TOTAL = {total}")
print(f"PAGADO = {paid}")
print(f"VUELTO = {change}")
