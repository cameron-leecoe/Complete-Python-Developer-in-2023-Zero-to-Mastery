import sys
import random

"""
This is an exercise for sys.argv from The Complete Python Developer in 2023: Zero to Mastery.
Project done by Cameron Coe.

This game will run when you input "python guessing_game.py 0 100" in the python terminal.
the two numbers can be replaced with any integer to scale difficulty.
"""

# Sets the range for what the integer can be
min = int(sys.argv[1])
max = int(sys.argv[2])
guess = 0

answer = random.randint(min, max)
gameGoing = True

print(f"\nHello, I would like you to guess a number between {min} and {max}.\n")

while (gameGoing):
    # Ensures the input is an integer
    try:
        guess = int(input("Take a Guess: "))
    except:
        print("\n* Make sure you're only entering a variable.")

    # Checks your guess
    if answer < guess:
        print(f"\nGood guess, but my number is LOWER than {guess}.")
    elif answer > guess:
        print(f"\nGood guess, but my number is HIGHER than {guess}.")
    else:
        gameGoing = False
        print(f"\nGreat Job! {answer} was the right number!")
