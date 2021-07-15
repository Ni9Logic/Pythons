from random import randint as r

correct_guess = r(0, 9)
guess = 0
while correct_guess != guess:
    guess = int(input("Enter guess:"))

if guess == correct_guess:
    print("You Won!")