mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(int(input("Enter a number: ")))

mylist.sort()
print("The second largest number in the list is:", mylist[-2])