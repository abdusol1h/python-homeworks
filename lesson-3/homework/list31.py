mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(input("Enter an element: "))

n = int(input("How many times do you want the elements to be repeated: "))

newlist = []

for item in mylist:
    for i in range(n):
        newlist.append(item)

print(newlist)