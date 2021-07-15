def reversecountdown(Self):
    Self = int(input('Enter Any Number: '))
    for i in range(Self, -1, -1):
        print (i)
    return Self

Self = 0
reversecountdown(Self)