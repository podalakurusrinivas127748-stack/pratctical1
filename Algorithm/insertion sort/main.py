import time

# Insertion Sort Function
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# User Input
n = int(input("Enter number of elements: "))

print("Enter the elements:")
arr = []

for i in range(n):
    arr.append(int(input()))

# Measure execution time
start = time.perf_counter()

insertion_sort(arr)

end = time.perf_counter()

# Output
print("\nSorted Array:", arr)
print("Execution Time: {:.10f} seconds".format(end - start))

print("\nTime Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n^2)")
print("Worst Case   : O(n^2)")
print("Space Complexity: O(1)")