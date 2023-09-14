# Best use of XOR

def uniqueNumber(x):
    ans = 0
    for num in x:
        ans = ans ^ num
    return ans


lis = [-1, 0, 1, 9, -2, 11, 0, 1, -2, 9, 11]
print(uniqueNumber(lis))

