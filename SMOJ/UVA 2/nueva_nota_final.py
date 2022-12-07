# Input
test1 = int(input())
test2 = int(input())
test3 = int(input())
test4 = int(input())
test5 = int(input())

# Calculate final note
z_average = round(((test2 + test3 + test4) / 3) * ((test1 + test5) / 200), 1)
average = round((test1 + test2 + test3 + test4 + test5) / 5, 1)

# Output
print(f"Nota Final Z: {z_average}")
print(f"Nota Final tradicional: {average}")
