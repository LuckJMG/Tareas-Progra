# Input
credit = int(input())
years = int(input())
interest = float(input())

# Calculate fee
r = interest / 1200
monthly_fee = round((credit * r) / (1 - ((1 + r) ** (-12 * years))))
total_fee = round(monthly_fee * years * 12)
paid_interest = round(total_fee - credit)
percentage_interest = round(((paid_interest * 100) / credit), 2)

# Output
print(
    f"Crédito por $ {credit} a un plazo de {years} años,",
    f"con una tasa de {interest} %",
)
print(f"Cuota mensual a pagar: $ {monthly_fee}")
print(f"Monto total pagado: $ {total_fee}")
print(f"Intereses pagados: $ {paid_interest}")
print(f"Porcentaje que representan los intereses: {percentage_interest} %")
