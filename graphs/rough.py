def printNumber(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("CodeQuotient")
        elif i % 3 == 0:
            print("Code")
        elif i % 5 == 0:
            print("Quotient")
        else:
            print(i)

n = 100
printNumber(n)
