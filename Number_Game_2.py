"""" 
Number game 2. In this version the computer guesses which number you picked. It then has the chance to guess again
with a hint to guess lower or higher than the computer's first guess.
"""

import random

def try_again():
    again = input("Would you like to play again?\n")
    again = str(again.upper())
    if again == "YES":
        return com_random_number_game(1, 10)
    else:
        quit()

def com_random_number_game(a, b):
    guess = random.randint(a, b)
    print("Welcome to the number guessing game.")
    user_num = input("Enter a number between " + str(a) + " and " + str(b) + " for the computer to guess.\n")
    user_num = int(user_num)

    if guess == user_num:
        print("The computer guessed your number! The computer guessed " + str(guess) + ".")
        try_again()
    if guess < user_num:
        low_guess = guess + 1
        print("The computer guessed lower than your number. The computer guessed " + str(guess) + ". Time to guess again!\n")
        guess_two = random.randint(low_guess, b)
        if guess_two == user_num:
            print("The computer guessed your number! The computer guessed " + str(guess_two) + ".")
            try_again()
        else:
            print("The computer did not guess your number. The computer guessed " + str(guess_two) + ".")
            try_again()
    if guess > user_num:
        high_guess = guess - 1
        print("The computer guessed higher than your number. The computer guessed " + str(guess) + ". Time to guess again!\n")
        guess_two = random.randint(a, high_guess)
        if guess_two == user_num:
            print("The computer guessed your number! The computer guessed " + str(guess_two) + ".")
            try_again()
        else:
            print("The computer did not guess your number. The computer guessed " + str(guess_two) + ".")
            try_again()
  

com_random_number_game(1, 10)
