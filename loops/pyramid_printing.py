def printPyramid(a):
    i = 0
    while i <= a:
        j = 0
        while j < a - i:
            print(" ", end="")
            j += 1
        k = 0
        while k < i:
            print("*", end="")
            k += 1
        print()
        i += 1


a = 4
printPyramid(a)
