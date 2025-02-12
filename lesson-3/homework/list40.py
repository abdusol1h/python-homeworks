mylist = eval(input("Enter a list: "))
uniqueList = []

for item in mylist:
    if item not in uniqueList:
        uniqueList.append(item)

print(uniqueList)