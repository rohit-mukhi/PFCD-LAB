#selection sort

def Selection_Sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

arr = [50, 35, 51, 143, 36]
arr = Selection_Sort(arr)
print(arr)
