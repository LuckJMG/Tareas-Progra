# Variables
people_number = int(input())
patients = 0
times = []
real_times = []

# Input patients wait time
while people_number > 0:
    times.append(int(input()))
    people_number -= 1

# Calculate real time
for position in range(len(times)):
    real_time = times[position] + sum(times) / len(times) + position
    print(int(real_time))
