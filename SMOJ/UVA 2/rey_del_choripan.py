# Constants
CHORIPAN_PRICE = 150

# Input
savings = int(input())

# Calculations
choripans_bought = savings // CHORIPAN_PRICE
amount_paid = choripans_bought * CHORIPAN_PRICE
change = savings - amount_paid

# Output
print(
    f"Con mi ahorro de {savings} puedo comprar {choripans_bought}",
    f"unidades por {amount_paid} y me sobra {change}",
)
