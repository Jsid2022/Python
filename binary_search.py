from random import randint


def linear_search(target, list):
    """Search your target through Linear search."""
    result = []
    for item in list:
        if item == target: 
            result.append(item)
            print("Your Number {0} is in the list.".format(item))

def binary_search(target, list):
    """Search Your target through Binary search."""
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
        if middle_index == 0 and target != item:
            return -1
        elif target == item:  # Item Found.(Can Exit loop)
            print("Yes your Number is in list")
            break
        # if search is smaller at middle index's item
        # remove all the items smaller than middle index's item.
        elif target < item: 
            copy_list = copy_list[:middle_index]
        # else vice versa.
        else:
            copy_list = copy_list[middle_index:]


# Make a random list of 100 Integers.
random_list1 = set()
while len(random_list1) != 100:
    random_list1.add(randint(1, 10000))

# Make a list of random 10 integers.
random_list2 = set()
while len(random_list2) != 10:
    random_list2.add(randint(1, 10000))

sorted_list = sorted(list(random_list1))
search_list = sorted(list(random_list2))

for item in search_list:
    linear_search(item, search_list)
