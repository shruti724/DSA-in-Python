def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        is_swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swapped = True
        if is_swapped is False:
            return


arr = [1,2,3,4]
bubblesort(arr)
print(arr)



