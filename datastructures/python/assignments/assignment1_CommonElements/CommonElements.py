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


if __name__ == "__main__":
    print("Array 1:")
    arr1 = make_array()
    print("Array 2:")
    arr2 = make_array()
    common_array = []

    arr1_uniques = remove_duplicates_optimized(arr1, len(arr1))
    arr2_uniques = remove_duplicates_optimized(arr2, len(arr2))

    for i in arr1[:arr1_uniques]:
        for j in arr2[:arr2_uniques]:
            if i == j:
                common_array.append(i)

    print(f"The common elements are {common_array}")
