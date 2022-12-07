# Input
distance = float(input())
performance = float(input())
liter_cost = float(input())

# Calculate the cost of the travel
travel_cost = ((1 / performance) * distance) * liter_cost
travel_cost = round(travel_cost, 2)

# Output
print(travel_cost)
