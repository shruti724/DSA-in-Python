a = int(input())
for i in range(a):
    b = int(input())
    c = list()
    for j in range(b):
        x = int(input())
        c.append(x)
    c = sorted(c) + [100000]

    for k in range(0, b, 2):
        if (c[k] != c[k + 1]):
            print(c[k])
            break