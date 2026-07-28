import time

# Input from user
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start timer
start_time = time.perf_counter()

# Selection Sort
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Stop timer
end_time = time.perf_counter()

# Display sorted array
print("\nSorted Array:")
print(arr)

# Display time complexity
print("\nTime Complexity:")
print("Best Case   : O(n²)")
print("Average Case: O(n²)")
print("Worst Case  : O(n²)")
print("Space Complexity: O(1)")

# Display execution time
execution_time = end_time - start_time
print(f"\nExecution Time: {execution_time:.10f} seconds")