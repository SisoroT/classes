def optimized_clockwise_rotation(arr: list):
    arr_length = len(arr)

    for i in range(arr_length - 1):
        for j in range(arr_length - 1 - i):
            temp = arr[i][j]
            arr[i][j] = arr[arr_length - 1 - j][i]
            arr[arr_length - 1 - j][i] = arr[arr_length - 1 - i][arr_length - 1 - j]
            arr[arr_length - 1 - i][arr_length - 1 - j] = arr[j][arr_length - 1 - i]
            arr[j][arr_length - 1 - i] = temp
    return arr


if __name__ == "__main__":
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    print(f"Before Rotation: {arr}")
    optimized_clockwise_rotation(arr)
    print(f"After Rotation: {arr}")
