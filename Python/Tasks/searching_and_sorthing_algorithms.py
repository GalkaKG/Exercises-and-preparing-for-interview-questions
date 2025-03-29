# Linear Search (O(n))
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i  # Found at index i
    return -1  # Not found

# Example
print(linear_search([1, 3, 5, 7, 9], 5))  # Output: 2



# Binary Search (O(log n)) - Requires a sorted array
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found

# Example
print(binary_search([1, 3, 5, 7, 9], 7))  # Output: 3


# Bubble Sort (O(n²)) - Simple but inefficient
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  # Swap if needed
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example
print(bubble_sort([5, 2, 9, 1, 5, 6]))  # Output: [1, 2, 5, 5, 6, 9]


# Selection Sort (O(n²)) - More efficient than bubble sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # Find the minimum element
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
    return arr

# Example
print(selection_sort([64, 25, 12, 22, 11]))  # Output: [11, 12, 22, 25, 64]



# Insertion Sort (O(n²)) - Efficient for small data sets
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example
print(insertion_sort([5, 2, 9, 1, 5, 6]))  # Output: [1, 2, 5, 5, 6, 9]


# Quick Sort (O(n log n) average case) - Fast and commonly used

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose a pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort


# Merge Sort (O(n log n)) - Stable and efficient

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Sort left half
    right_half = merge_sort(arr[mid:])  # Sort right half
    return merge(left_half, right_half)  # Merge sorted halves

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])  # Append remaining elements
    result.extend(right[j:])
    return result
