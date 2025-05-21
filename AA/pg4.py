def heap_sort(arr):
    n = len(arr)

    # Step 1: Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Swap and heapify
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move max to end
        heapify(arr, i, 0)

def heapify(arr, size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    maxIndex = i

    if left < size and arr[left] > arr[maxIndex]:
        maxIndex = left

    if right < size and arr[right] > arr[maxIndex]:
        maxIndex = right

    if maxIndex != i:
        arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
        heapify(arr, size, maxIndex)

# Example usage
arr = [4, 10, 3, 5, 1]
heap_sort(arr)
print("Sorted array:", arr)
