import copy


def clockwise_rotation(arr: list[list[int]]):
    new_arr = copy.deepcopy(arr)
    # rewrite the rows of new_arr as the columns of arr
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            new_arr[i][j] = arr[len(arr[0]) - 1 - j][i]

    # overwrite arr with the contents of new_arr
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = new_arr[i][j]


if __name__ == "__main__":
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    print(f"Before Rotation: {arr}")
    clockwise_rotation(arr)
    print(f"After Rotation: {arr}")
