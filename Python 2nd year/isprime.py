isPrime = False
n = int(input("Input a positive integer: "))
if (n == 0 or n == 1):
    isPrime = False
else:
    for i in range(2, int(n/2)):
        if i % 2 == 0:
            isPrime = False
            break
if isPrime:
    print (n, "is A prime Integer")
else:
    print (n, "is not A prime Integer")
