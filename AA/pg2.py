import time

def quick_sort(arr, low, high):
    if low >= high:
        return

    start = low
    end = high
    mid = start + (end - start) // 2
    pivot = arr[mid]

    while start <= end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Recursively sort the two halves
    quick_sort(arr, low, end)
    quick_sort(arr, start, high)

# Sample height list
heights = [5, 4, 3, 2, 1]

# Start time
start_time = time.time()

# Perform Quick Sort
quick_sort(heights, 0, len(heights) - 1)

# End time
end_time = time.time()

# Print results
print("Sorted heights:", heights)
print("Time taken for sorting:", (end_time - start_time), "seconds")
