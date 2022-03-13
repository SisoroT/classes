def binary_search_recursive(arr: list, target: int, low: int, high: int):
    mid = (low + high) // 2
    if low <= high:
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        if arr[mid] > target:
            return binary_search_recursive(arr, target, low, mid - 1)
        return -1


arr = [0, 1, 2, 3, 5, 7, 9, 12, 13]
print(f"The target is found at index {binary_search_recursive(arr, 9, 0, len(arr))}")
