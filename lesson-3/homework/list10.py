mylist = []

#getting the list from the user
list_length = int(input("Enter the amount of elements in the list: "))
for j in range(list_length):
    mylist.append(int(input("Enter a number: ")))

swap = True

for i in range(list_length):
    for j in range(list_length-1):
        sawp = False
        if(mylist[j] > mylist[j+1]):
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
            swap = True
    if not swap:
        break

print(mylist)