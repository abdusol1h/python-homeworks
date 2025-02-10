mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for x in range(list_length):
    mylist.append(int(input("Enter a number: ")))

odd = 0
for number in mylist:
    if number % 2 == 1:
        odd += 1

print(f"There are {odd} odd numbers in this list.")