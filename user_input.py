def get_user_input():
    """
    This Function will return the user input values.
    """
    pass_information = {}
    choices = ['yes', 'no', 'y', 'n']
    while True:
        try: pass_length = int(input("Enter the length of Password: "))
        except ValueError: print("Invalid Input!!")
        else:
            if pass_length >= 4:
                pass_information['length'] = pass_length
                break
            else:
                print("Minimum Length required is 4!")

    while True:
        begin_letter = input("Do you want your password to begin with a letter? (yes/no)\n")
        if begin_letter.lower() not in choices: print("Invalid Input")
        elif begin_letter.lower() == 'yes' or begin_letter == 'y':
            pass_information['begin_with_letter'] = True
            break
        else: 
            pass_information['begin_with_letter'] = False 
            break

    if pass_information["begin_with_letter"] == False:
        while True:
            while True:
                include_numbers = input("Do you want to include numbers in your Password? (yes/no)\n")
                if include_numbers.lower() not in choices:
                    print("Invalid Input")
                elif include_numbers.lower() == 'yes' or include_numbers == 'y':
                    pass_information['numbers'] = True
                    break
                else: 
                    pass_information['numbers'] = False
                    break
        
            while True:
                include_symbols = input("Do you want to include symbols in your Password? (yes/no)\n")
                if include_symbols.lower() not in choices: print("Invalid Input")
                elif include_symbols.lower() == 'yes' or include_symbols == 'y':
                    pass_information['symbols'] = True
                    break
                else: 
                    pass_information['symbols'] = False 
                    break
            if pass_information['numbers'] == True or pass_information['symbols'] == True:
                break
            else:
                print("You must select numbers or symbols because you chose not to begin password with a letter!\n")

        while True:
            include_lowercase = input("Do you want to include lowercase letters in your Password? (yes/no)\n")
            if include_lowercase.lower() not in choices: 
                print("Invalid Input")
            elif include_lowercase.lower() == 'yes' or include_lowercase == 'y':
                pass_information['lowercase'] = True
                break
            else:
                pass_information['lowercase'] = False 
                break
        
        while True:
            include_uppercase = input("Do you want to include uppercase letters in your Password? (yes/no)\n")
            if include_uppercase.lower() not in choices: 
                print("Invalid Input")
            elif include_uppercase.lower() == 'yes' or include_uppercase == 'y':
                pass_information['uppercase'] = True
                break
            else: 
                pass_information['uppercase'] = False 
                break
    else:
        while True:
            while True:
                include_lowercase = input("Do you want to include lowercase letters in your Password? (yes/no)\n")
                if include_lowercase.lower() not in choices: 
                    print("Invalid Input")
                elif include_lowercase.lower() == 'yes' or include_lowercase == 'y':
                    pass_information['lowercase'] = True
                    break
                else: 
                    pass_information['lowercase'] = False 
                    break
        
            while True:
                include_uppercase = input("Do you want to include uppercase letters in your Password? (yes/no)\n")
                if include_uppercase.lower() not in choices: 
                    print("Invalid Input")
                elif include_uppercase.lower() == 'yes' or include_uppercase == 'y':
                    pass_information['uppercase'] = True
                    break
                else: 
                    pass_information['uppercase'] = False 
                    break
            if pass_information['uppercase'] == True or pass_information['lowercase'] == True:
                break
            else:
                print("You must select lowercase or uppercase to begin password with a letter!\n")
        
        while True:
                include_numbers = input("Do you want to include numbers in your Password? (yes/no)\n")
                if include_numbers.lower() not in choices:
                    print("Invalid Input")
                elif include_numbers.lower() == 'yes' or include_numbers == 'y':
                    pass_information['numbers'] = True
                    break
                else: 
                    pass_information['numbers'] = False
                    break
        
        while True:
            include_symbols = input("Do you want to include symbols in your Password? (yes/no)\n")
            if include_symbols.lower() not in choices: print("Invalid Input")
            elif include_symbols.lower() == 'yes' or include_symbols == 'y':
                pass_information['symbols'] = True
                break
            else: 
                pass_information['symbols'] = False 
                break
    return pass_information