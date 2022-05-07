# Write a program that asks the user how many Fibonnaci numbers to generate and then 
# generates them. Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the 
# sequence to generate.

def fibonacci_numbers(input_number):
    """This Function will return the list of fibonacci numbers."""
    n = int(input_number)   # Convert the number to an Integer.
    fibonacci = []          # List to store fibonacci numbers.
    last_two_number_sum = 0 # Variable to sum last two numbers.
    ix = 0
    while ix < n:  # Add numbers till the user_input's number.
        if len(fibonacci) == 0: fibonacci.append(1)
        elif len(fibonacci) == 1: fibonacci.append(1)
        else:
            # Sum the last two numbers of fibonacci list
            last_two_number_sum = fibonacci[-2] + fibonacci[-1]
            # and add it to the list.
            fibonacci.append(last_two_number_sum)
        ix += 1

    return fibonacci


user = input("How many Fibonacci Numbers you want to Generate? ")
print(fibonacci_numbers(user))
