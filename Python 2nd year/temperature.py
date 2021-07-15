Choice = int(input("Choose\n1 --> Farenheight\n2 --> Celcius\nEnter: "))
if Choice == 1:
    Farenheight = float(input("Enter Farenheight: "))
    Celcius = (Farenheight - 32)*5/9
    print("Temperature Converted from ", Farenheight, " Farenheight to ", Celcius, " Celcius")
elif Choice == 2:
    Celcius = float(input("Enter Celcius: "))
    Farenheight = (Celcius*(9/5)) + 32
    print("Temperature Converted from ", Celcius, " Celcius to ", Farenheight, " Farenheight")
else:
    print("Kindly Choose Correct Option\n")
    