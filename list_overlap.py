from random import randint

# write a program that returns a list that contains only the elements that 
# are common between the lists (without duplicates). Make sure your program 
# works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at 
# this point - we’ll get to it soon)


def common_numbers_list(list1, list2):
    """
    This function will return the numbers,
    that are common in both lists.
    """
    result = set()
    for number in list2:
        if number in list1:
            result.add(number)
    return list(result)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89]
common = common_numbers_list(b, a)
strng = ''
for numbers in common:
    strng += str(numbers)+", "
strng_list = list(strng.rstrip())
strng_list[-1] = "."
print("Common numbers between both lists are","".join(strng_list))
