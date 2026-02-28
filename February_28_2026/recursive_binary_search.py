def binarySearch(target, arr, first, last):
    if first > last:
        return -1
    
    mid = (first + last)//2
    
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binarySearch(target, arr, first, mid - 1)
    else:
        return binarySearch(target, arr, mid+1, last)
    
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
index = binarySearch(target, arr, 0, len(arr)-1)

if index != -1:
    print(target, "Found at index ", index)
else:
    print(target, "Not found!")
    
