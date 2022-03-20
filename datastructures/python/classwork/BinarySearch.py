def binary_search_recursive(arr: list, low: int, high: int, target: int):
    mid = (low + high) // 2
    if low <= high:
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return binary_search_recursive(arr, mid + 1, high, target)
        if arr[mid] > target:
            return binary_search_recursive(arr, low, mid - 1, target)
    return -1


arr = [0, 1, 2, 3, 5, 7, 9, 12, 13]
print(f"The target is found at index {binary_search_recursive(arr, 0, len(arr), 9)}")
