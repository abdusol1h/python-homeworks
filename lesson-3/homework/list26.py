import math
mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(input("Enter an element: "))

if list_length % 2 == 0:
    print("The middle elements of this list are:", mylist[(list_length//2)-1], "and", mylist[(list_length//2)])
else:
    print("The middle element of this list is:", mylist[(list_length//2)])