def power(x, n):
    if n == 0:
        return 1
    if x == 0:
        return 0
    smallOutput = power(x, n - 1)
    output = smallOutput * x
    return output


x = int(input())
n = int(input())
print(power(x, n))
