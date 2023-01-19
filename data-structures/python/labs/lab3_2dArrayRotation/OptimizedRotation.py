def optimized_clockwise_rotation(arr: list):
    arr_len = len(arr)

    # rotate a group of 4 elements at a time in a clockwise
    # direction collapsing towards the middle of the
    # array until the whole array has been rotated
    for i in range(0, int(arr_len / 2)):
        for j in range(i, arr_len - i - 1):

            # store current cell in temp variable
            temp = arr[i][j]
            # move value from bottom-left to top-left
            arr[i][j] = arr[arr_len - 1 - j][i]
            # move value from bottom-right to bottom-left
            arr[arr_len - 1 - j][i] = arr[arr_len - 1 - i][arr_len - 1 - j]
            # move value from top-right to bottom-right
            arr[arr_len - 1 - i][arr_len - 1 - j] = arr[j][arr_len - 1 - i]
            # assign temp to top-right
            arr[j][arr_len - 1 - i] = temp

    return arr


if __name__ == "__main__":
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    print(f"Before Rotation: {arr}")
    optimized_clockwise_rotation(arr)
    print(f"After Rotation: {arr}")
