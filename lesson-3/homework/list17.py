list1 = []

#getting the list1 from the user
list1_length = int(input("Enter the amount of elements in the first list: "))
for x in range(list1_length):
    list1.append(input("Enter an element: "))

list2 = []

#getting the list2 from the user
list2_length = int(input("Enter the amount of elements in the second list: "))
for x in range(list2_length):
    list2.append(input("Enter an element: "))

newlist = list1 + list2
print(newlist)