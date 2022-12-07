def determine_gems(stones):
    # Constants
    FORMAT = "abcdefghijklmnopqrstuvwxyz"

    # Variables
    minerals = {}
    gems = 0

    # Count minerals in gems
    for mineral in FORMAT:
        for stone in stones:
            if mineral in stone:
                if mineral not in minerals:
                    minerals[mineral] = 0
                minerals[mineral] += 1

    # Count actual gems
    for mineral in minerals:
        if minerals[mineral] == len(stones):
            gems += 1

    return gems


# Program
## Variables
stones = []

## Input
iterations = int(input())
while iterations > 0:
    stone = input()
    stones.append(stone)
    iterations -= 1

## Output
print(determine_gems(stones))
