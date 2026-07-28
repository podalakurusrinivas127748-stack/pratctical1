import time

# Partition function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quick Sort function
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Input from user
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start timer
start_time = time.perf_counter()

# Perform Quick Sort
quick_sort(arr, 0, n - 1)

# Stop timer
end_time = time.perf_counter()

# Display sorted array
print("\nSorted Array:")
print(arr)

# Display time complexity
print("\nTime Complexity:")
print("Best Case   : O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case  : O(n²)")
print("Space Complexity: O(log n)")

# Display execution time
execution_time = end_time - start_time
print(f"\nExecution Time: {execution_time:.10f} seconds")