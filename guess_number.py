from random import randint

def guess_number():
    """Guess the Number Between 1 to 20."""
    random_number = randint(1, 20)
    guess = 0  # Initialize the guess the number to 0.
    count = 0
    
    strng = "Welcome, Choose a number between 1 to 20\n"
    strng += "If you guess the number correctly in 5 attempts you win, else you die!"
    print(strng)

    
guess_number()
input("")