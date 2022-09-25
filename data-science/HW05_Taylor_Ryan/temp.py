# returns an array containing how many ways you can make each number with n dice that have m sides
def fill_how_many_ways(arr):
    # Fill the array
    for i in range(1, num_sides + 1):
        arr[i] = 1

    for i in range(2, num_dice + 1):
        for j in range(sum_ub - 1, 0, -1):
            arr[j] = sum(arr[j - k] for k in range(1, num_sides + 1) if j - k > 0)
    return arr


# returns an array containing how many ways you can make each number with n dice that have m sides
def dice(n, m):
    # Initialize the array
    array = np.zeros(sum_ub, dtype=int)

    # Fill the array
    for i in range(1, m + 1):
        array[i] = 1

    for i in range(2, n + 1):
        for j in range(sum_ub - 1, 0, -1):
            array[j] = sum(array[j - k] for k in range(1, m + 1) if j - k > 0)

    return array
