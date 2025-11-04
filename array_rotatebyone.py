def rotate_by_one(arr):
    last = arr[-1]          # Step 1
    for i in range(len(arr)-1, 0, -1):   # Step 2
        arr[i] = arr[i-1]
    arr[0] = last           # Step 3
    return arr
# Example
arr = [1, 2, 3, 4, 5]
print(rotate_by_one(arr))  # ✅ Output: [5, 1, 2, 3, 4]