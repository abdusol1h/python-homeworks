mylist = []
largest_element = 0

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(int(input("Enter a number: ")))

for number in mylist:
    if number > largest_element:
        largest_element = number

if mylist == []:
    print("You have entered an empty list!")
else:
    print(f"The largest number in the list is: {largest_element}")