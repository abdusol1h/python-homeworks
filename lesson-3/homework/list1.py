# n to store the amount of elements user is looking for  
n = 0
mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(input("Enter an element: "))

element = input("Please enter the element you are looking for: ")
for item in mylist:
    if item == element:
        n += 1

# returning amount of elements the user is looking for
print(f"There are {n} of the elements you are looking for in this list.")