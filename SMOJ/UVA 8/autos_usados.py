# Input
cars = {}
iterations = int(input())
while iterations > 0:
    car = input()
    price = int(input())
    if car not in cars:
        cars[car] = [0, 0]
    cars[car][0] += price
    cars[car][1] += 1
    iterations -= 1

# Unpack total prices from car list
cars_list = []
prices = []
for car in cars:
    cars_list.append([car] + cars[car])
    prices.append(cars[car][0])

# Organize car list from greatest to lowest price
count = len(prices)
ordered_cars = []
while count > 0:
    index = prices.index(max(prices))
    ordered_cars.append(cars_list[index])
    del prices[index]
    del cars_list[index]
    count -= 1

# Output
for model, total_price, amount in ordered_cars:
    print("Auto:", model)
    print("Monto Total:", total_price)
    print("Cantidad a vender:", amount)
    print("===")
