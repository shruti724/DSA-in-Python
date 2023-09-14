import math


def min_cost(dp, cost, i, j):
    m = len(cost)
    n = len(cost[0])
    # Special case
    if i == m - 1 and j == n - 1:
        return cost[i][j]
    # base case
    if i >= m:
        return math.inf
    if j >= n:
        return math.inf

    if dp[i+1][j] == -math.inf:
        ans1 = min_cost(dp, cost, i+1, j)
        dp[i+1][j] = ans1
    else:
        ans1 = dp[i+1][j]

    if dp[i][j+1] == -math.inf:
        ans2 = min_cost(dp, cost, i, j+1)
        dp[i][j+1] = ans2
    else:
        ans2 = dp[i][j+1]

    if dp[i+1][j+1] == -math.inf:
        ans3 = min_cost(dp, cost, i+1, j+1)
        dp[i+1][j+1] = ans3
    else:
        ans3 = dp[i+1][j+1]

    min_ans = cost[i][j] + min(ans1, ans2, ans3)
    return min_ans


cost = [[1,5,11], [8,13,12], [15,16,18]]
dp = [[-math.inf for i in range(len(cost)+1)] for j in range(len(cost[0])+1)]
# print(dp)
ans = min_cost(dp, cost, 0, 0)
print(ans)
