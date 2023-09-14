# Sum of n natural numbers

def sum_n(n):
    if n == 0:
        return 0
    smallOutput = sum_n(n-1)
    output = n + smallOutput
    return output


n = int(input())
print(sum_n(n))
