#getting the list from user
mylist = eval(input("Enter a list: "))
#checking for palindrome using slicing
if mylist == mylist[::-1]:
    print("The given list is a palindrome.")
else:
    print("The given list is not a palindrome.")