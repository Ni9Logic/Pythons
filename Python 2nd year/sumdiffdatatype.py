def sumdiffnum(num, num1):
    num = float(input('Enter Float: '))
    num1 = int(input('Enter Int: '))

    res = num + num1
    print(res)
    return res
def sumdiffnum3(num, num1, num2):
    num = float(input('Enter Float: '))
    num1 = int(input('Enter Int: '))
    num2 = input("Enter String: ")
    num2 = int(num2)
    res = num + num1 + num2
    print(res)
    return res

a = 0.0 # Float
b = 0 # int
c = "0" # string

sumdiffnum(a, b)
sumdiffnum3(a, b, c)
