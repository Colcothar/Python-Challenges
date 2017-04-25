import random

# Generare a randome number between 1 and 10
secret_num = random.randint(1, 10)

def number_game():
    i = 0
    while i < 3:
        guess = input("Guess a number between 1 and 10: ")
        i += 1
        if guess.isdigit():
            guess = int(guess)
            if guess == secret_num:
                print("You got it! My number was {}.".format(secret_num))
                try_again()
            if i <= 2:
                if guess > secret_num:
                    print("That's too high! You have used {} out of 3 guesses!".format(i))
                else: 
                    print("That's too low! You have used {} out of 3 guesses!".format(i))
            if i > 2:
                print("You have run out of guesses!")
                try_again()
        else: 
            print("Please enter a number!")
            number_game()
        
def try_again():
    again = input("Would you like to play again?\n")
    again = again.upper()
    
    if again == "YES":
        number_game()
    else:
        quit()
                
            
            
number_game()
