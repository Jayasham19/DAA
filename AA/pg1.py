import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Merge the two halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Sample age list
ages = [5, 4, 3, 2, 1]

# Start timing
start_time = time.time()

# Perform merge sort
sorted_ages = merge_sort(ages)

# End timing
end_time = time.time()

# Print results
print("Sorted ages:", sorted_ages)
print("Time taken for sorting:", (end_time - start_time), "seconds")
