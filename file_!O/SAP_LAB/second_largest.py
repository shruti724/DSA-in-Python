import math


def print2largest(arr, n):
    first, second = -math.inf, -math.inf
    for i in range(n):
        if arr[i]> first:
            second = first
            first = arr[i]
        if (arr[i]> first) and (arr[i]< second):
            second = arr[i]
    return second


n = 6
arr = [12, 35, 1, 10, 34, 1]
print(print2largest(arr, n))

