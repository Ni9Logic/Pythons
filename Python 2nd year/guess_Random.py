from random import randint
random = input("Guess The Random Number: ")
randomint = randint(0, 10)
if randomint == random:
    print("Yes you won!")
else:
    print("NO~ You lost!")