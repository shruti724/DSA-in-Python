def sortZero(arr):
    arrNew = []
    for _ in arr:
        if _ != 0:
            arrNew.append(_)
    for _ in arr:
        if _ == 0:
            arrNew.append(_)
    return arrNew


arr = [1,2,3,0,6,0,0,4,5]
print(sortZero(arr))
