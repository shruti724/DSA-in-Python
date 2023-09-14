# def printNatural(n):
#     if n == 0:
#         return
#     printNatural(n-1)
#     print(n)
#     return


# n = int(input())
# printNatural(n)


def printReverseNatural(n):
    if n == 0:
        return
    print(n)
    printReverseNatural(n -1)
    return


n = int(input())
printReverseNatural(n)
