mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(input("Enter an element: "))

reverse_list = mylist[::-1]
if mylist == []:
    print("You have entered an empty list!")
else:
    print(reverse_list)