def get_nearest_sum(list_A, list_B, number):
    # Variables
    nearest_sum = [list_A[0], list_B[1]]

    # Check every possible sum
    for number_A in list_A:
        for number_B in list_B:
            tmp = number_A + number_B

            if abs(number - tmp) < abs(number - sum(nearest_sum)):
                nearest_sum[0] = number_A
                nearest_sum[1] = number_B

    return nearest_sum
