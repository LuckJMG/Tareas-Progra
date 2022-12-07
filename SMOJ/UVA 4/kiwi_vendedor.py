# Constants Input
gasoline = float(input())
performance = float(input())

# Variables
current_x = 0
current_y = 0
visited_cities = 0

while gasoline > 0:
    # Variables Input
    city_x = int(input())
    city_y = int(input())

    # Calculate consumed gasoline
    distance_x = abs(city_x - current_x)
    distance_y = abs(city_y - current_y)
    distance = (distance_x ** 2 + distance_y ** 2) ** (1 / 2)
    gasoline -= distance / performance

    # Check travel
    # Case go to start point
    if city_x == 0 and city_y == 0:
        gasoline = 0
        print(f"recorrerá {visited_cities} ciudad(es)")
        print("vuelve al punto de partida")

    # Case next city
    elif gasoline >= 0:
        visited_cities +=1
        current_x = city_x
        current_y = city_y

    # Case no more gasoline
    else:
        print(f"recorrerá {visited_cities} ciudad(es)")
        print("no alcanza a llegar a la última ciudad y se acaba el combustible")
