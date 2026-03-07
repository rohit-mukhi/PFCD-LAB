def merge_two_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
        
    return merged

def merge_k_arrays(arrays):
    if not arrays:
        return []
    
    while len(arrays) > 1:
        merged_list = []
        for i in range(0, len(arrays), 2):
            if i + 1 < len(arrays):
                merged_result = merge_two_arrays(arrays[i], arrays[i+1])
                merged_list.append(merged_result)
            else:
                merged_list.append(arrays[i])
        arrays = merged_list
        
    return arrays[0]


arrays = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

arr = merge_k_arrays(arrays)
print("Merged sorted array:", arr) 

