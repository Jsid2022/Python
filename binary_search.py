from random import shuffle

def binary_search(search, list):
    """Search Your Number in the Given list."""
    # Copy of Original List.
    copy_list = sorted(list[:])
    while True:
        # Update length of List in each iteration.
        list_length = len(copy_list)

        # Get the middle index of list.
        middle_index = list_length // 2
        # Item at middle index.
        item = copy_list[middle_index]
        
        # If the middle_index is 0 and search is not item
        # exit loop
        if middle_index == 0 and search != item:
            return print("Your Number is not in the List.")
        elif search == item:  # Item Found.(Can Exit loop)
            print("Yes your Number is in list")
            break
        # if search is smaller at middle index's item
        # remove all the items smaller than middle index's item.
        elif search < item: 
            copy_list = copy_list[:middle_index]
        # else vice versa.
        else:
            copy_list = copy_list[middle_index:]


# List of number's between 1 to 1000.
number_list = [i for i in range(1, 1001)]
shuffle(number_list)  # Shuffle the list.
binary_search(1001, number_list)