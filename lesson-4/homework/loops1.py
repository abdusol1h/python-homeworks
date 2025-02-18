list1 = [1, 2, 3]
list2 = [4, 5, 6]
uncommon = []

isUnique = True

for item in list1:
    for x in list2:
        if item == x:
            isUnique = False
            list2.remove(x)
    if isUnique:
        uncommon.append(item)
         
uncommon += list2
print(uncommon)