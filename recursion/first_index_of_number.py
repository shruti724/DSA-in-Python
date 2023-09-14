# 1. Base Case
# 2. Induction Hypothisis (I.H)
# 3. Induction Step (I.S)

def firstOccurence(arr, x):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == x:
        return 0
    smallerList = firstOccurence(arr[1:], x)

    if smallerList == -1:
        return -1
    else:
        return smallerList + 1


arr = [1, 2, 8, 5, 46]
print(firstOccurence(arr, 46))
