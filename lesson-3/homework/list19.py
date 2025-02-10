mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(input("Enter an element: "))

replace_element = input("Replace: ")
new_element = input("With: ")

mylist[mylist.index(replace_element)] = new_element
print(mylist)