mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(input("Enter an element: "))

check = input("Enter the element you are looking for: ")

if mylist == []:
    print("You have entered an empty list!")
elif check in mylist:
    print("The element you are looking for is in the list")
else:
    print("The element you are looking for is not on the list")