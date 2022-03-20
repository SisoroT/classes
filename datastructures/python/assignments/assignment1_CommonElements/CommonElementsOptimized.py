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


def binary_search_recursive(arr: list[int], low: int, high: int, target: int):
    mid = (low + high) // 2
    if low <= high:
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return binary_search_recursive(arr, mid + 1, high, target)
        if arr[mid] > target:
            return binary_search_recursive(arr, low, mid - 1, target)
    return -1


if __name__ == "__main__":
    print("Array 1:")
    arr1 = make_array()
    print("Array 2:")
    arr2 = make_array()

    common_array = []

    for i in range(len(arr1)):
        # if i is not the last element and it
        # is equal to i+1 then skip that number
        if i < len(arr1) - 1 and arr1[i] == arr1[i + 1]:
            continue
        # binary search for the current element in the second array
        found = binary_search_recursive(arr2, 0, len(arr2), arr1[i])
        # if the number exists in the second array, add it to the common_array
        if found != -1:
            common_array.append(arr1[i])

    print(f"The common elements are {common_array}")
