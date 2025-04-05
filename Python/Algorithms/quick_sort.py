def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    pivot = arr[0]  # Choose the first element as the pivot
    left = [x for x in arr[1:] if x < pivot]  # Elements smaller than the pivot
    right = [x for x in arr[1:] if x >= pivot]  # Elements greater than or equal to the pivot

    return quick_sort(left) + [pivot] + quick_sort(right)


nums = [8, 3, 1, 7, 0, 10, 2]
sorted_nums = quick_sort(nums)
print(sorted_nums)  # 👉 [0, 1, 2, 3, 7, 8, 10]

