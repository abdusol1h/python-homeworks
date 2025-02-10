mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(int(input("Enter a number: ")))

even = 0
for number in mylist:
    if number % 2 == 0:
        even += 1

print(f"There are {even} even numbers in this list.")