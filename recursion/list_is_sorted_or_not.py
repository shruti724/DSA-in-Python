# 1. Using list slicing

def sort(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True
    if arr[0] > arr[1]:
        return False
    smallerListOutput = sort(arr[1:])
    return smallerListOutput


arr = [1, 1, 1, 1]
print(sort(arr))


