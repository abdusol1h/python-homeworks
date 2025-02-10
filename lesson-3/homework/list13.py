mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(input("Enter an element: "))

search = input("Enter the element you are looking for: ")
for i in range(len(mylist)):
    if mylist[i] == search:
        print("The item you are looking for is at index", i)
        break
