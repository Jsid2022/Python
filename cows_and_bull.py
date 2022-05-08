from random import randint

# Create a program that will play the “cows and bulls” game with the user.
# The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
# For every digit that the user guessed correctly in the correct place, 
# they have a “cow”. For every digit the user guessed correctly in the wrong 
# place is a “bull.” Every time the user makes a guess, tell them how many “cows” 
# and “bulls” they have. Once the user guesses the correct number, the game 
# is over. Keep track of the number of guesses the user makes throughout 
# the game and tell the user at the end.

def get_user_number():
    """This Function will get the user Number."""
    nums = [i for i in range(10)]
    while True:
        try: 
            num = int(input("\nGive me a Number: "))
            if num not in nums:
                raise ValueError
        except ValueError: print("You can only guess a number from 0 to 9.")
        else: break
    return str(num)

def cows_and_bulls():
    """Start the game."""
    random_number = randint(1000, 9999)  # Genrate Random Number.
    num_list = list(str(random_number))  # Make a list of that Random Number.
    used_number = []                     # Empty list to store user_number
    guessed_number = ["_" for i in range(4)]  # List to print Correctly guessed number.
    cows = 0                             # Track score for correct guess.
    bulls = 0                            # Track score for wrong guess.
    while "_" in guessed_number:  # End loop if All numbers are correctly guessed.
        ix = 0
        user = get_user_number()
        if user not in used_number:
            used_number.append(user)
            if user in num_list:
                while ix < len(guessed_number):
                    if num_list[ix] == user:
                        guessed_number[ix] = user
                    ix += 1
                cows += 1
                ix = 0
                print("".join(guessed_number))
                print("{0} cows, {1} bulls.".format(cows, bulls))
            else:
                bulls += 1
                print("{0} cows, {1} bulls.".format(cows, bulls))
        else:
            print("You have Guessed that Number!")
        if bulls == 4:
            print("You Failed to guess all numbers correctly!")
            break
    if cows == 4:
        print("You won!")
    

cows_and_bulls()