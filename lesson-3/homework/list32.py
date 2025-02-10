list1 = []

#getting the list from the user
list1_length = int(input("Enter the amount of elements in the list: "))
for x in range(list1_length):
    list1.append(input("Enter an element: "))

list2 = []

#getting the list from the user
list2_length = int(input("Enter the amount of elements in the list: "))
for x in range(list2_length):
    list2.append(input("Enter an element: "))

merged = list1 + list2
merged.sort()

print(merged)