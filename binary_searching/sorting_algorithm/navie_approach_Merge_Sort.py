# def merge_sort(a, b):
#     ans = a+b
#     ans.sort()
#     return ans

def merge_sort(a, b):
    res = []
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i]>a[j]:
            res.append(b[j])
            j += 1

    pass


a = [1,5,10]
b = [2, 4, 8]
print(merge_sort(a, b))
