#Guessing game where the user guesses the number the computer generated

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print('Sorry, guess again. Too high')
    
    print(f'Congrats, you have guessed the number {random_number} correctly')

x = int(input("Tell me a number that will be the limit of our guessing game "))
guess(x)

