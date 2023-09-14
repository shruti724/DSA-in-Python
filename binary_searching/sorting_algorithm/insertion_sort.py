def insertion(arr):
    for i in range(1, len(arr)):
        j = i-1
        temp = arr[i]
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp


arr = [1, 3, 5, 2, 4]
insertion(arr)
print(arr)
