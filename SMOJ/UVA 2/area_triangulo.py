# Input
side1 = float(input())
side2 = float(input())
side3 = float(input())

# Calculate area
semiperimeter = (side1 + side2 + side3) / 2
area = round(
    (
        semiperimeter
        * (semiperimeter - side1)
        * (semiperimeter - side2)
        * (semiperimeter - side3)
    )
    ** (1 / 2),
    2,
)

# Output
print(area)
