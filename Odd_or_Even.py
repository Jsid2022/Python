# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. Hint: how does an even / odd 
# number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.

# Ask the user for two numbers: one number to check (call it num) and 
# one number to divide by (check). If check divides evenly into num, 
# tell that to the user. If not, print a different appropriate message.

def mulitple_of_4(num):
    """Check if the number is multiple of 4."""
    if num % 4 == 0:
        return True
    return False

def odd_or_even(num):
    """Check if the number is odd or even."""
    number = int(num)
    if (number % 2 == 0) and (mulitple_of_4(number) == True):
        print("Yes, your Number is Even and is also a Multiple of 4.")
    elif (number % 2 == 0) and (mulitple_of_4(number) == False):
        print("Yes, your Number is Even.")
    else:
        print("Your Number is Odd.")

def is_divisible(divisor, dividend_number):
    """Check if the number is divisible by number ot not."""
    if int(dividend_number) % int(divisor) == 0:
        print("{0} is divisible by {1}.".format(divisor, dividend_number))
    else:
        print("{0} is not divisible by {1}.".format(divisor, dividend_number))


number = input("Enter a Number: ")
divisor = input("Enter Divisor: ")
# odd_or_even(number)
is_divisible(divisor, number)
