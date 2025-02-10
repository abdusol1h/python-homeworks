# Getting the list from the user
mylist = []
list_length = int(input("Enter the number of elements in the list: "))
for x in range(list_length):
    mylist.append(input("Enter an element: "))

# Get shift value
shift = int(input("Rotate by: ")) % list_length  # For shifts larger than length of list

# Performing rotation using slicing
rotated_list = mylist[-shift:] + mylist[:-shift]

print(rotated_list)