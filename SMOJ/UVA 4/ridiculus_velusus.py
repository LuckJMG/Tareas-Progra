# Constants
RECOLLECTED_SEEDS = int(input())

# Variables
day = 0
yesterday_seeds = 0
today_seeds = 1
total_seeds = 0

# Calculate days needed
while RECOLLECTED_SEEDS > total_seeds:
    day += 1
    tmp = today_seeds
    today_seeds += yesterday_seeds
    total_seeds += today_seeds
    yesterday_seeds = tmp

# Output
print(day)
