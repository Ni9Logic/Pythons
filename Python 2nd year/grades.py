loop = 'y'
while loop == 'y' or loop == 'Y':
    marks = float(input('Enter your marks: '))
    if marks < 116:
        print("Your grade is F")
    elif marks >= 116 and marks < 170:
        print("Your grade is D")
    loop = input('Do you want to re-run the code?: ')