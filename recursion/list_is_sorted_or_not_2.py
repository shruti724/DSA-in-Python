# 2. Using start index

def sort(arr, si):
    n = len(arr)
    if si == n - 1 or si == n:
        return True
    if arr[si] > arr[si + 1]:
        return False
    smallerList = sort(arr, si+1)
    return smallerList


arr = [1, 2, 3, 4]
print(sort(arr, 0))


