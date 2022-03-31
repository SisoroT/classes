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


def merge(arr: list[int], first: int, mid: int, last: int):
    size_of_left = mid - first + 1
    size_of_right = last - mid

    # create temp arrays
    left_arr = [0] * (size_of_left)
    right_arr = [0] * (size_of_right)

    # copy data to temp arrays left[] and right[]
    for i in range(size_of_left):
        left_arr[i] = arr[first + i]
    for i in range(size_of_right):
        right_arr[i] = arr[mid + 1 + i]

    left_idx = 0  # initial index of first subarray
    right_idx = 0  # initial index of second subarray
    merged_idx = first  # initial index of merged subarray

    # merge the temp arrays back into arr[first..last]
    while left_idx < size_of_left and right_idx < size_of_right:
        if left_arr[left_idx] <= right_arr[right_idx]:
            arr[merged_idx] = left_arr[left_idx]
            left_idx += 1
        else:
            arr[merged_idx] = right_arr[right_idx]
            right_idx += 1
        merged_idx += 1

    # copy the remaining elements of left[], if there are any
    while left_idx < size_of_left:
        arr[merged_idx] = left_arr[left_idx]
        left_idx += 1
        merged_idx += 1

    # copy the remaining elements of right[], if there are any
    while right_idx < size_of_right:
        arr[merged_idx] = right_arr[right_idx]
        right_idx += 1
        merged_idx += 1


# first is first index and last is last
# index of the sub-array of arr to be sorted
def merge_sort(arr: list[int], first: int, last: int):
    if first < last:
        # same as (first+last)//2, but avoids overflow for large l and h
        mid = first + (last - first) // 2

        # sort first and second halves
        merge_sort(arr, first, mid)
        merge_sort(arr, mid + 1, last)
        merge(arr, first, mid, last)


if __name__ == "__main__":
    # arr = make_array()
    arr = [50, 11, 33, 21, 40, 50, 40, 40, 21]
    merge_sort(arr, 0, len(arr) - 1)
    last_unique_index = remove_duplicates_optimized(arr, len(arr))
    print(arr[:last_unique_index])
