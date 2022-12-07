from math import pi

# Input
room_width = int(input())
room_length = int(input())
carpet_material = input()

# Variables
carpet_external_radius = room_width / 2
if carpet_material == "Algodon":
    carpet_internal_radius = carpet_external_radius / 5
elif carpet_material == "Bambu":
    carpet_internal_radius = carpet_external_radius / 4
elif carpet_material == "Nylon":
    carpet_internal_radius = carpet_external_radius / 3

# Calculate area
room_area = room_length * room_width
carpet_area = (carpet_external_radius**2 - carpet_internal_radius**2) * pi
carpet_area = round(carpet_area, 2)
carpet_coverage = (1 - (carpet_area / room_area)) * 100
carpet_coverage = round(carpet_coverage, 2)

# Output
print(carpet_area)
print(f"{carpet_coverage} %")
