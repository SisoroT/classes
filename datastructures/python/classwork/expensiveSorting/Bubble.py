def bubble_sort(arr):
    arr_len = len(arr)

    # traverse through all array elements
    for i in range(arr_len - 1):
        for j in range(0, arr_len - i - 1):
            # swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    arr = [8, 3, 4, 1, 2]
    bubble_sort(arr)
    print(arr)
