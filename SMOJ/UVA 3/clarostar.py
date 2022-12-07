# Constants
DAY_COST_PLAN = 10
DAY_COST_EXTRA = 15
MAX_DAY_PLAN = 100
NIGHT_COST_PLAN = 7
NIGHT_COST_EXTRA = 13
MAX_NIGHT_PLAN = 80

# Input
day_minutes = int(input())
night_minutes = int(input())

# Calculate total cost
if day_minutes <= MAX_DAY_PLAN:
    print("DIA: no excede")
    total_cost = day_minutes * DAY_COST_PLAN
else:
    print(f"DIA: excede en {day_minutes - MAX_DAY_PLAN} minutos")
    total_cost = DAY_COST_PLAN * MAX_DAY_PLAN
    total_cost += (day_minutes - MAX_DAY_PLAN) * DAY_COST_EXTRA

if night_minutes <= MAX_NIGHT_PLAN:
    print("NOCHE: no excede")
    total_cost += night_minutes * NIGHT_COST_PLAN
else:
    print(f"NOCHE: excede en {night_minutes - MAX_NIGHT_PLAN} minutos")
    total_cost += NIGHT_COST_PLAN * MAX_NIGHT_PLAN
    total_cost += (night_minutes - MAX_NIGHT_PLAN) * NIGHT_COST_EXTRA

# Output
print(f"Cliente paga {total_cost}")
