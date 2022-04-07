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


def remove_duplicates(arr: list[int], list_length: int) -> int:
    # if array has a length of 0 or 1 then it is sorted already
    if list_length == 0 or list_length == 1:
        return list_length
    temp = []

    # if current number doesn't equal the next then
    # that number is unique and add it to the temp array
    for i in range(list_length - 1):
        if arr[i] != arr[i + 1]:
            temp.append(arr[i])
    temp.append(arr[list_length - 1])

    # copy all the unique elements in order onto the original array
    for i in range(len(temp)):
        arr[i] = temp[i]

    # the length of the temp array is the
    # number of unique elements so return that
    uniques = len(temp)
    return uniques


if __name__ == "__main__":
    arr = make_array()
    last_unique_index = remove_duplicates(arr, len(arr))
    print(arr[:last_unique_index])
