# max. sum of k element in a subarray of the array

def fixed_sliding_window(arr, k):
    current_subarray = sum(arr[:k])
    result = [current_subarray]
    for i in range(1, len(arr)-k+1):
        current_subarray = current_subarray - arr[i-1]
        current_subarray = current_subarray + arr[i+k-1]
        result.append(current_subarray)
    return result


arr = [1, 2, 3, 4, 5]
k = 3
print(fixed_sliding_window(arr, k))
