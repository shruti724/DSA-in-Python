def merge(arr1, arr2):
    i = 0
    j = 0
    len1 = len(arr1)
    len2 = len(arr2)
    merged_arr = []
    while (i < len1) and (j < len2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i= i+1
        else:
            merged_arr.append(arr2[j])
            j= j+1

    while i<len1:
        merged_arr.append(arr1[i])
        i = i+1

    while j<len2:
        merged_arr.append(arr2[j])
        j += 1

    return merged_arr


arr1 = [1, 3, 5, 6]
arr2 = [8, 9, 12, 14]
print(merge(arr1, arr2))
