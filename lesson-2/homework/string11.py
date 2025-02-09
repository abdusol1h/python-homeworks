str = input("Enter a string: ")
if any(i.isdigit() for i in str):
    print("String contains a digit")
else:
    print("The string does not contain any digits")