import math


def min_cost(cost, i, j):
    m = len(cost)
    n = len(cost[0])
    # Special case
    if i == m-1 and j == n-1:
        return cost[i][j]
    # base case
    if i >= m:
        return math.inf
    if j >= n:
        return math.inf

    min_ans = cost[i][j] + min(min_cost(cost, i+1, j), min_cost(cost, i, j+1), min_cost(cost, i+1, j+1))
    return min_ans


cost = [[1,5,11], [8,13,12], [15,16,18]]
ans = min_cost(cost, 0, 0)
print(ans)
