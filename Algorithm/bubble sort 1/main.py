import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

n = int(input("Enter number of elements: "))

print("Enter the elements:")
arr = []
for i in range(n):
    arr.append(int(input()))

start = time.perf_counter()

bubble_sort(arr)

end = time.perf_counter()

print("\nSorted Array:", arr)
print("Execution Time: {:.10f} seconds".format(end - start))

print("\nTime Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n^2)")
print("Worst Case   : O(n^2)")
print("Space Complexity: O(1)")