def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            count = count + 1
        arr[j + 1] = key
    return count


arr = [35, 143, 50, 51, 36]
print("Original list:", arr)
count = insertion_sort(arr)
print("Sorted by insertion sort:", arr)
print("Number of shifts:", count)
