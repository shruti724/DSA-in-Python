import math, sys

def minsqttoN(n):
    if n == 0:
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1, root+1):
        currAns = 1 + minsqttoN(n-(i**2))
        ans = min(currAns, ans)
    return ans


n = int(input())
print(minsqttoN(n))
