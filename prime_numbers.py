# Ask the user for a number and determine whether the number is prime or not.

def is_prime(input_number):
    """
    This Function will Tell if the Number is prime or not.
    """
    number = int(input_number)
    numbers_list = [i for i in range(2, number)]
    for n in numbers_list:
        if number % n == 0:
            return False
    return True

user_number = input("Enter a Number and check if it is prime or not: ")
if is_prime(user_number):
    print("Your number {0} is a prime number!".format(user_number))
else: print("Your number {0} is not a prime number!".format(user_number))
