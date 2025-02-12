mylist = eval(input("Enter a list: ")) #getting the list from the user  
subGroupSize = int(input("Enter the subgroup size: "))  

newlist = []  
sublist = []  
counter = 0  

for item in mylist:  
    sublist.append(item)  
    counter += 1  
    # creating newsublist after sublist size is equal to group size given by the user
    if counter == subGroupSize:  
        newlist.append(sublist)  
        sublist = []  
        counter = 0  

# Add any remaining elements as the last sublist  
if sublist:  
    newlist.append(sublist)  

print(newlist)