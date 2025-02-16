mytuple = eval(input("Enter a tuple: "))
uniquelist = []
for item in mytuple:
    if item not in uniquelist:
        uniquelist.append(item)

uniquetuple = tuple(uniquelist)
print(uniquetuple)