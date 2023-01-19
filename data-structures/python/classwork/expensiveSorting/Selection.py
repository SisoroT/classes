def selection_sort(arr):
    for i in range(len(arr)):
        min_loc = i

        # find the minimum element in remaining unsorted array
        for j in range(i + 1, len(arr)):
            if arr[min_loc] > arr[j]:
                min_loc = j

        # swap the found minimum element with the
        # first element of the unsorted array
        arr[i], arr[min_loc] = arr[min_loc], arr[i]


if __name__ == "__main__":
    arr = [8, 3, 4, 1, 2]
    selection_sort(arr)
    print(arr)
