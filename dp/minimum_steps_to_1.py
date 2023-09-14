import sys


def min_step(n):
    if n == 1:
        return 0
    ans1 = sys.maxsize

    if n % 2 == 0:
        ans1 = min_step(n//2)

    ans2 = sys.maxsize
    if n % 3 == 0:
        ans2 = min_step(n//3)

    ans3 = min_step(n-1)

    ans = 1 + min(ans1, ans2, ans3)
    return ans


n = int(input())
print(min_step(n))

