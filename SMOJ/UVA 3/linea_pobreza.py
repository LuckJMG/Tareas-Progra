# Constants
PPOBERTY_LINE1 = 176625
PPOBERTY_LINE2 = 286928
PPOBERTY_LINE3 = 381098
PPOBERTY_LINE4 = 466116

# Input
number_of_members = int(input())
monthly_income = int(input())
is_below_pl = False

# Determine if the home is below the poberty line
if number_of_members == 1:
    if monthly_income <= 0:
        is_below_pl = "error"
    elif monthly_income < PPOBERTY_LINE1:
        is_below_pl = True
elif number_of_members == 2:
    if monthly_income <= 0:
        is_below_pl = "error"
    elif monthly_income < PPOBERTY_LINE2:
        is_below_pl = True
elif number_of_members == 3:
    if monthly_income <= 0:
        is_below_pl = "error"
    elif monthly_income < PPOBERTY_LINE3:
        is_below_pl = True
elif number_of_members == 4:
    if monthly_income <= 0:
        is_below_pl = "error"
    elif monthly_income < PPOBERTY_LINE4:
        is_below_pl = True
else:
    is_below_pl = "error"

# Output
print(is_below_pl)
