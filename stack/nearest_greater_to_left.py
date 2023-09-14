def nearest_greater_to_left(arr):
    stack = []
    lis = []
    n = len(arr)
    for i in range(n):
        if not stack:
            lis.append(-1)
        elif stack:
            while len(stack) > 0 and stack[-1] <= arr[i]:
                stack.pop()
            if not stack:
                lis.append(-1)
            else:
                lis.append(stack[-1])
        stack.append(arr[i])
    return lis


arr = [1, 3, 2, 4]
print(nearest_greater_to_left(arr))

