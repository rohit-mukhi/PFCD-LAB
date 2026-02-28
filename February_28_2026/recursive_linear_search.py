def linearSearch(target, arr, idx):
    
    if idx == len(arr):
        return -1
    else:
        if target == arr[idx]:
            return idx

    return linearSearch(target, arr, idx+1)
        
arr = [1, 2, 3, 4, 5]
target = 5
idx = linearSearch(target, arr, 0)
if(idx):
    print(target, "Found at index ", idx)
else:
    print(target, "Not present in the array!")
