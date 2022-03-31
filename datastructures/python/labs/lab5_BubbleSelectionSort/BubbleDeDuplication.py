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


def bubble_sort(arr):
    arr_len = len(arr)

    # traverse through all array elements
    for i in range(arr_len - 1):
        for j in range(0, arr_len - i - 1):
            # swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    arr = make_array()
    bubble_sort(arr)
    last_unique_index = remove_duplicates_optimized(arr, len(arr))
    print(arr[:last_unique_index])
