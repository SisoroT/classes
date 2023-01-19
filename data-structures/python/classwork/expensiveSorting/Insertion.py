def insertion_sort(arr):
    for i in range(1, len(arr)):
        # save current value we're looking at
        curr = arr[i]
        prev = i - 1

        # make each number equal to the number before it
        while prev >= 0 and curr < arr[prev]:
            arr[prev + 1] = arr[prev]
            prev -= 1
        # set first number equal to the current number
        arr[prev + 1] = curr


if __name__ == "__main__":
    arr = [8, 3, 4, 1, 2]
    insertion_sort(arr)
    print(arr)
