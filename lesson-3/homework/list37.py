mylist = eval(input("Enter a list: "))
sum = 0

for number in mylist:
    if number < 0:
        sum += number

print(f"The sum of the negative numbers in this list is : {sum}")