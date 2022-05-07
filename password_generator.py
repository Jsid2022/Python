from random import choice, shuffle
import string
# Write a password generator in Python. Be creative with how you generate passwords
# - strong passwords have a mix of lowercase letters, uppercase letters,
# numbers, and symbols. The passwords should be random, generating a new password 
# every time the user asks for a new password. Include your run-time code in a main method.

def password_generator(input_length):
    """
    This function will generate a random Strong password,
    consisting a lowercase letters, uppercase letters,
    numbers, and symbols.
    """
    # List of ABCDEFGHIJKLMNOPQRSTUVWXYZ
    upper_letters = list(string.ascii_uppercase)
    # list of abcdefghijklmnopqrstuvwxyz
    lower_letters = list(string.ascii_lowercase)
    # List of 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    digits = [str(i) for i in range(10)]    
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '~', '?']
    # Combine all List togethor
    combined_list = upper_letters + lower_letters + digits + symbols
    # Shuffle the combined list
    shuffle(combined_list)
    # Select random characters from each list
    rand_upper = choice(upper_letters)
    rand_lower = choice(lower_letters)
    rand_digit = choice(digits)
    rand_symbol = choice(symbols)
    temp_pass = []
    # and append it to temp_pass(Temporary Password).
    temp_pass.append(rand_upper), 
    temp_pass.append(rand_lower)
    temp_pass.append(rand_digit)
    temp_pass.append(rand_symbol)
    shuffle(temp_pass)  # Shuffle List(So no one can predict it).
    while len(temp_pass) != input_length:
        shuffle(combined_list)  # Shuffle again on each iteration
        rand_item = choice(combined_list)  # Select random char from combined_list
        temp_pass += rand_item  # and add it to list temp_pass
        shuffle(temp_pass)  # Shuffle the temp_list on each iteration
    random_pass = "".join(temp_pass)  # Convert all the items to String.
    return random_pass

print(password_generator(10))