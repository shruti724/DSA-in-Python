# Using start pointer

def first_index(arr, si, x):
    n = len(arr)
    if si == n:
        return -1
    if arr[si] == x:
        return si
    smallListOutput = first_index(arr, si + 1, x)
    return smallListOutput


arr = [1, 2, 4, 5, 22, 3, 4]
print(first_index(arr, 0, 2))
