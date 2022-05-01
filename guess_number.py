from random import randint

def guess_number():
    """Guess the Number Between 1 to 20."""
    random_number = randint(1, 20)
    print(random_number)
    strng = "Welcome, Guess a number between 1 to 20\n"
    strng += "If you guess the correct number in first 5 attempts you win,\n"
    strng += "else you die!\n"
    print(strng)
    guess = 0         # Initialize the guess number to 0.
    count = 0         # count the number of inputs
    correct = True    # check if user guessed the correct number or not.

    while guess != random_number:
        try:
            guess = int(input("Guess a number between 1 to 20. --> "))
        except ValueError:
            print("Invalid input!")  # If user's input is not int.
        else:
            if guess == random_number:
                correct = True
                count += 1
            elif guess < random_number:
                print("\nSorry, guess again. Too low!")
                correct = False
                count += 1
                print("Attempts left: {0}\n".format(5 - count))
            elif guess > random_number:
                print("Sorry, guess again. Too high!")
                correct = False
                count += 1
                print("Attempts left: {0}\n".format(5 - count))

        if count == 5:
            break
    
    if count == 5 and correct == False:
        print("You failed to guess the correct number, now you die!")
    elif count == 1:
        print("Impressive! You guessed the correct number {0} in first attempt.".format(random_number))
    else:
        print("Yay, congrats! You guessed the correct number {0}, in {1} attempts.".format(random_number, count))

guess_number()
input("")
