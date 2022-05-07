from random import randint

# write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has 
# all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.

# Ask the user for a number and return a list that contains only elements 
# from the original list a that are smaller than that number given by the user.

random_list = [randint(1, 100) for i in range(10)]

def less_than_5(list):
    """
    This function returns a list of numbers,
    that are less than 5.
    """
    result = []
    for number in list:
        if number < 5: result.append(number)
    return result

def less_than_user_input(input_number):
    """
    This function returns a list of numbers,
    that are less than user's Input.
    """
    result = []
    for numbers in random_list:
        if numbers < input_number: result.append(numbers)
    return result


print(random_list)
list = less_than_5(random_list)
print(list)

user_number = int(input("Enter a Number: "))
less_than_user_input(user_number)
