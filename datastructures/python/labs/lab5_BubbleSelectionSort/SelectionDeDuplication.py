def make_array() -> list[int]:
    # user decides how long they want the array
    length = int(input("How long would you like to make your array? "))

    # if user enters a non positive number, prompt them to enter a positive
    while length <= 0:
        length = int(input("Please enter a positive number. "))

    arr = []
    # have the user enter all the elements for the array
    for i in range(length):
        arr.append(int(input(f"Enter element {i+1} for your array. ")))

    return arr


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


def remove_duplicates_optimized(arr: list[int], list_length: int) -> int:
    # if array has a length of 0 or 1 then it is sorted already
    if list_length == 0 or list_length == 1:
        return list_length
    uniques = 0

    # if i!=i+1 then it is unique so place i
    # at the next unique index of the array
    for i in range(list_length - 1):
        if arr[i] != arr[i + 1]:
            arr[uniques] = arr[i]
            uniques += 1

    # add last unique number and increment counter
    arr[uniques] = arr[-1]
    uniques += 1

    return uniques


if __name__ == "__main__":
    arr = make_array()
    selection_sort(arr)
    last_unique_index = remove_duplicates_optimized(arr, len(arr))
    print(arr[:last_unique_index])
