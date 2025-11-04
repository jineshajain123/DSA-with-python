def is_subset(a, b):
    freq = {}

    # Count frequency of each element in array a
    for x in a:
        freq[x] = freq.get(x, 0) + 1

    # Check if each element of b is available in a with enough count
    for x in b:
        if x in freq and freq[x] > 0:
            freq[x] -= 1
        else:
            return False  # Not found or count exhausted

    return True


# Example
a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]

print(is_subset(a, b))  # ✅ Output: True
