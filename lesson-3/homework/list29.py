mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(input("Enter an element: "))

index = int(input("Enter the index of the element you want to be removed: "))
if index >= list_length:
    print("The index you provided is out of range.")
else:
    mylist.pop(index)
    print(mylist)