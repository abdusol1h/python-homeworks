mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(int(input("Enter a number: ")))

odd_list = []

for i in mylist:
    if i % 2 == 1:
        odd_list.append(i)

print(odd_list)