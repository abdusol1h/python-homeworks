mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(input("Enter an element: "))

new_list = []

for i in mylist:
    if i not in new_list:
        new_list.append(i)

print(new_list)