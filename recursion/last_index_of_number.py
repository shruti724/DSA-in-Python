# Using List slicing

def lastIndex(arr, x):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == x:
        smallerList = arr[1:]
        smallerListOutput = lastIndex(smallerList, x)

    if smallerListOutput == -1:
        return -1
    else:
        return smallerListOutput + 1