import time
from random import randint

def linear_search(target, list):
    """Search your target through Linear search."""
    for item in list:
        if item == target: 
            return True
    return False

def binary_search(target, list):
    """Search Your target through Binary search."""
    # Copy of Original List.
    low = 0
    high = len(list)
    while True:
        # Get the middle index of list.
        middle_index = (low + high) // 2
        # Item at middle index.
        item_at_mid = list[middle_index]
        
        if item_at_mid == target:  # Item Found.(Can Exit loop)
            return True
        elif item_at_mid < target:  # If item at mid is smalled then tagret
            low = middle_index + 1  # Look for the Upper half of in list
        else:                       # else
            high = middle_index     # Look for lower half in list.

# Make a random list of 100 Integers.
random_list1 = set()
while len(random_list1) != 10000:
    random_list1.add(randint(1, 10000))

# Sort list.
sorted_list = sorted(list(random_list1))

# Measure time for both searches.

# Linear Seach
start = time.process_time()
for item in sorted_list:
    linear_search(item, sorted_list)
end = time.process_time()
print("Linear Search Time: {0}".format(end - start))

# Binary Search.
start = time.process_time()
for item in sorted_list:
    binary_search(item, sorted_list)
end = time.process_time()
print("Binary Search Time: {0}".format(end - start))
