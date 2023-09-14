def tocheckprime(a):
    isPrime = False
    for i in range(2, a):
        if a % i == 0:
            isPrime = False
        else:
            isPrime = True
    if isPrime:
        print(a, "is prime")
    else:
        print(a, "is not prime")
    return isPrime


a = 5
tocheckprime(a)

