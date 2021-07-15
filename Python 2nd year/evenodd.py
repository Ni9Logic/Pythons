number = float(input('Enter Number: '))
number = round(number) #Rounds of the number into a proper decimal interger either an even or false.
if number % 2 == 0:
    print("Number is even")
elif number % 2 == 1:
    print("Number is odd")