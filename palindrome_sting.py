# Ask the user for a string and print out whether this string is a palindrome 
# or not. (A palindrome is a string that reads the same forwards and backwards.)

def is_plaindrome(input_strng):
    """
    This function will check if the string is palindrome or not.
    """
    reverse_string = list(input_strng.lower())
    reverse_string.reverse()
    reverse_string = "".join(reverse_string)
    if reverse_string == input_strng.lower():
        print("\"{0}\" is a Palindrome!".format(input_strng))
    else:
        print("\"{0}\" is not a Palindrome!".format(input_strng))
        
user = input("Check if your word is a Palindrome or not: ")
print()
is_plaindrome(user)

