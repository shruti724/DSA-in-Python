def geometric_sum(a, b, k):
    # till 1/2**k
    if k < 0:
        return 1
    sum = a/b**k


a = 1
k = 3
print(geometric_sum(a, k))

