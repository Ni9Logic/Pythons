principal = input("Enter principal: ")
principal = float(principal)
rate = input("Enter rate: ")
rate = float(rate)
time = input("Enter time: ")
time = float(time)

interest = (principal *rate* time)/100
interest = float(interest)

print("Interest is: ", interest)