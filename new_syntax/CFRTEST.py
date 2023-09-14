t = int(input())
for i in range(t):
    n = int(input())
    l= list(map(int, input().split()))
    print(len(set(l)))

# arr = [1, 2, 3, 3, 5, 2, 4]
# print(set(arr))
# {1, 2, 3, 4, 5}
