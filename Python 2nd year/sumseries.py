def sumserie(n):
    n = int(input("Enter the number of terms: "))
    sum = 0
    for i in range(1, n+1):
        sum += (1/i)
    sumrounded = round(sum)
    print("The sum of series is: ", sumrounded)
    return sumrounded

n = 0
sumserie(n)