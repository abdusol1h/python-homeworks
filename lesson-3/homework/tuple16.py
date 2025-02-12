mytuple = eval(input("Enter a tuple: "))
isSorted = True

for i in range(len(mytuple)-1):
    if mytuple[i] > mytuple[i+1]:
        isSorted = False

if isSorted:
    print("The tuple is sorted.")
else:
    print("The tuple is not sorted.")