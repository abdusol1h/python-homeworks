mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(int(input("Enter an element: ")))

start = int(input("Select the start of the interval(included): "))
end = int(input("Select the end of the interval(excluded): "))

newlist = mylist[start:end]
newlist.sort()
print("The maximum number in the specified sublist is:", newlist[-1])