import sys

def min_step_memo(n, dp):
    if n == 1:
        return 0

    pass


n = int(input())
dp = [-1 for i in range(n+1)]
print(min_step_memo(n, dp))
