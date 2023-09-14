def LIS(arr, i, n):
    including_max = 1
    for j in range(i+1, n):
        if arr[j] >= arr[i]:
            further_including_max = LIS()


n = int(input())
li = [int(ele) for ele in input().split()]
ans = LIS(li, 0, n)
