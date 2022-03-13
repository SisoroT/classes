arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

# continuously check to see if the number at j is > j+1 and swap if true
for _ in arr:
    for inner in range(len(arr) - 1):
        if arr[inner] > arr[inner + 1]:
            arr[inner], arr[inner + 1] = arr[inner + 1], arr[inner]

print(arr)
