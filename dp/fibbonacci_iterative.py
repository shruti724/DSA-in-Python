def fibb_i(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    i = 2
    while i <= n:
        dp[i] = dp[i-1] + dp[i-2]
        i += 1
    return dp[n]


n = int(input())
print(fibb_i(n))
