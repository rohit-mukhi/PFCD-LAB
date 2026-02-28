def firstOccurence(target, arr, first, last, res=-1):
    if first > last:
        return res
    
    mid = (first + last)//2
    
    if arr[mid] == target:
        res = mid
        return firstOccurence(target, arr, first, mid-1, res)
    elif target < arr[mid]:
        return binarySearch(target, arr, first, mid-1, res)
    else:
        return binarySearch(target, arr, mid+1, last, res)
    
arr = [1, 4, 5, 6, 7, 7, 7, 7, 8, 9]
target = 7
index = binarySearch(target, arr, 0, len(arr)-1)

if index != -1:
    print(target, "Found at index ", index)
else:
    print(target, "Not found!")
