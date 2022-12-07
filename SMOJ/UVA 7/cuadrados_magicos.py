def magic_square(matrix):
    # Variables
    order = len(matrix)
    magic_number = []
    diagonal_sum1 = 0
    diagonal_sum2 = 0

    # Calculate rows magic number
    for row in matrix:
        magic_number.append(sum(row))

    for column in range(order):
        # Calculate diagonal magic number
        diagonal_sum1 += matrix[column][column]
        diagonal_sum2 += matrix[column][order - column - 1]

        # Calculate columns magic number
        sum_columns = 0
        for row in matrix:
            sum_columns += row[column]
        magic_number.append(sum_columns)

    magic_number.append(diagonal_sum1)
    magic_number.append(diagonal_sum2)

    # Check if the matrix is a magic square
    if sum(magic_number) / magic_number[0] == (order + 1) * 2:
        return magic_number[0]
    else:
        return "NO"

# Variables
matrix = []
order = int(input())

# Generate matrix
for number in range(order):
    row = []

    for number2 in range(order):
        row.append(int(input()))

    matrix.append(row)

# Output
print(magic_square(matrix))
