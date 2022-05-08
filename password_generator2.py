from user_input import get_user_input
from random import choice, shuffle
import string

def generate_password(inp_dict):
    """
    This Function will Generate a random password,
    according to user's requirements.
    """
    uppercase_letters = list(string.ascii_uppercase)
    lowercase_letters = list(string.ascii_lowercase)
    digits = list(string.digits)
    symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '?']
    combined_list = []
    temp_password = []
    random_password = ""
    if inp_dict["begin_with_letter"] == False:
        if inp_dict["numbers"] == True:
            combined_list.extend(digits)
            temp_password.append(choice(digits))
        if inp_dict["symbols"] == True:
            combined_list.extend(symbols)
            temp_password.append(choice(symbols))
        shuffle(temp_password)
        rand_letter = choice(temp_password)
        random_password += rand_letter
        temp_password.remove(rand_letter)
        if inp_dict["lowercase"] == True:
            combined_list.extend(lowercase_letters)
            temp_password.append(choice(lowercase_letters))
        if inp_dict["uppercase"] == True:
            combined_list.extend(uppercase_letters)
            temp_password.append(choice(uppercase_letters))
        shuffle(temp_password)
        shuffle(combined_list)
        random_password += "".join(temp_password)
    else:
        if inp_dict["lowercase"] == True:
            combined_list.extend(lowercase_letters)
            temp_password.append(choice(lowercase_letters))
        if inp_dict["uppercase"] == True:
            combined_list.extend(uppercase_letters)
            temp_password.append(choice(uppercase_letters))
        shuffle(temp_password)       
        rand_letter = choice(temp_password)
        random_password += rand_letter
        temp_password.remove(rand_letter)
        if inp_dict["numbers"] == True:
            combined_list.extend(digits)
            temp_password.append(choice(digits))
        if inp_dict["symbols"] == True:
            combined_list.extend(symbols)
            temp_password.append(choice(symbols))
        shuffle(temp_password)
        shuffle(combined_list)
        random_password += "".join(temp_password)
    shuffle(combined_list)
    while len(random_password) != inp_dict["length"]:
        random_password += choice(combined_list)
    print("Random Password:",random_password)


user = get_user_input()
generate_password(user)