mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of numbers in the list: "))
for x in range(list_length):    
    element = int(input("Enter a number: "))
    mylist.append(element)

#calculating the sum
sum = 0
for i in mylist:
    sum += i

if mylist == []:
    print("You have entered an empty list!")
else:
    print(f"The sum of the numbers in the list is: {sum}")