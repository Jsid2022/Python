# Create a program that asks the user for a number and then prints out a 
# list of all the divisors of that number.

# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


def print_divisors(input_number):
    """
    This function will print out all the divisors,
    of a given number.
    """
    number_list = [i for i in range(1, input_number+1)]
    divisors = []
    for number in number_list:
        if input_number % number == 0:
            divisors.append(number)
    print_divisors = [print(str(i+1)+".", divisor) for i, divisor in enumerate(divisors)]

user_number = int(input("Enter a Number: "))
print_divisors(user_number)
