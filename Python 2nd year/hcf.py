def HCF(n1,n2):
    n1 = int(input("Enter Variable 1: "))
    n2 = int(input("Enter Variable 2: "))
    hcf = 0
    temp = 0
    if n2 > n1:
        temp = n2
        n2 = n1
        n1 = temp
    for i in range(1, n2):  ##range(1, n2) 1 starts it from index 1 cuz if it's devided by zero then it returns error
        if n1 % i == 0 and  n2 % i == 0:
            hcf  = i

    print ("Print HCF = ", hcf)
    return hcf

n1 = n2 = 0
HCF(n1, n2)
