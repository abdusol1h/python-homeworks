mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(input("Enter an element: "))

indices = []
index = 0

element = input("Enter the element you are searching for: ")

for item in mylist:
    if item == element:
        indices.append(index)
    index += 1

print(indices)