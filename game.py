print("Welcome! to number Guessing game ")
print("Lets begin")

import random

guesses = 0
random_num = random.randint(0, 100)

while guesses < 10:

    guessed_num = int(input("Enter Number: "))

    if guessed_num == random_num:
        print('You Won!!')
        break
    elif guessed_num < random_num:
        print('Guess is low')
    else:
        print('Guess is high')
    guesses += 1
