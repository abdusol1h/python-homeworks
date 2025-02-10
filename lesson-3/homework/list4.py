mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(int(input("Enter a number: ")))

smallest_element = mylist[0]

for number in mylist:
    if number < smallest_element:
        smallest_element = number

if mylist == []:
    print("You have entered an empty list!")
else:
    print(f"The smallest number in the list is: {smallest_element}")