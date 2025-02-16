set = {1, 2, 3, 4, 5, 6}
element = int(input("Which element do you want to add: "))
if element not in set:
    set.add(element)

print(set)