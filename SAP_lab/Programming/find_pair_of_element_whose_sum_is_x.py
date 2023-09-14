def PairsCount(li, n, sum):
    ans_dict = {}
    count = 0
    for i in range(n):
        if sum - li[i] in ans_dict:
            count += ans_dict[sum - li[i]]
        if li[i] in ans_dict:
            ans_dict[li[i]] += 1
        else:
            ans_dict[li[i]] = 1
    return count


arr = [1, 5, 7, -1]
n = len(arr)
sum = 6
print(PairsCount(arr, n, sum))
