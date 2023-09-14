def fib(n):
    if n == 1 or n == 2:
        return 1
    smallOutput1 = fib(n-1)
    smallOutput2 = fib(n-2)
    output = smallOutput1 + smallOutput2
    return output


n = 40
print(fib(n))
