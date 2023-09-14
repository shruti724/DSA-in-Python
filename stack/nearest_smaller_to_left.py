def nearest_smaller_to_left(arr):
    stack = []
    lis = []
    n = len(arr)
    for i in range(n):
        if not stack:
            lis.append(-1)
        elif stack:
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if not stack:
                lis.append(-1)
            else:
                lis.append(stack[-1])
        stack.append(arr[i])

    return lis


arr = [4, 5, 2, 10, 8]
print(nearest_smaller_to_left(arr))
