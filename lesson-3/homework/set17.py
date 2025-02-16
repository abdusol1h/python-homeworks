set = {1, 2, 3, 4, 5, 6, 7, 8}
newset = set.copy()
for element in set:
    if element % 2 == 0:
        newset.remove(element)
        
print(newset)