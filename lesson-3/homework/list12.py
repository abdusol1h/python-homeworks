mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(input("Enter an element: "))

new_element = input("Enter the new element you want to insert: ")
index = int(input("Enter the index of new item you want to be inserted: "))
mylist.insert(index, new_element)
print(mylist)