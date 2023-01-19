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
    arr = [2, 0, 9, 5, 7, 5, 2, 1]
    print(f"Before sorting\n{arr}")
    quick_sort(arr, 0, len(arr) - 1)
    print(f"\nAfter sorting\n{arr}")
