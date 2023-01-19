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


def partition(arr: list[int], first: int, last: int) -> int:
    pivot = arr[last]  # pivot
    i = first - 1  # index of smaller element

    for j in range(first, last):
        # if current element is less than or equal
        # to pivot, increment i and swap i and j
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot in correct place and return its index
    arr[i + 1], arr[last] = arr[last], arr[i + 1]
    return i + 1


def quick_sort(arr: list[int], first: int, last: int):
    if len(arr) == 1:
        return arr
    if first < last:
        # pi is partitioning index, arr[p] is now
        # at right place
        part_index = partition(arr, first, last)

        # separately sort elements before and after partition
        quick_sort(arr, first, part_index - 1)
        quick_sort(arr, part_index + 1, last)


if __name__ == "__main__":
    # arr = make_array()
    arr = [50, 11, 33, 21, 40, 50, 40, 40, 21]
    quick_sort(arr, 0, len(arr) - 1)
    last_unique_index = remove_duplicates_optimized(arr, len(arr))
    print(arr[:last_unique_index])
