mainlist = []

#getting the list from the user
list_length1 = int(input("Enter the amount of elements in the main list: "))
for x in range(list_length1):
    mainlist.append(input("Enter an element: "))

sublist = []

#getting the list from the user
list_length2 = int(input("Enter the amount of elements in the sublist: "))
for x in range(list_length2):
    sublist.append(input("Enter an element: "))

# function for determining if sublist is within main list
def is_sublist(mainlist, sublist):
    if not sublist:  # An empty sublist is always present
        return True
    if not mainlist:  # If the main list is empty, sublist can't exist
        return False

    for i in range(len(mainlist) - len(sublist) + 1):
        if mainlist[i:i + len(sublist)] == sublist:
            return True
    return False

if is_sublist(mainlist, sublist):
    print("The main list contains the sublist")
else:
    print("The main list does not contain the sublist")