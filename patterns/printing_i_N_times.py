def diagonalDifference(arr):
    sum_lr = 0
    sum_rl = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                sum_lr += arr[i][j]

    i = 0
    while i < len(arr):
        k = 0
        while k <= len(arr)-i:
            sum_rl += arr[i][k]
            k += 1
        i += 1
    return len(arr)


arr = [[11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]]
print(diagonalDifference(arr))
