mytuple = eval(input("Enter a tuple: "))
element = input("Which element are you searching for? ")

#changing data type of element to avoid integer/float being treated as string
if element.isdigit():
    element = int(element)
elif element.replace(".", "", 1).isdigit():
    element = float(element)

if element in mytuple:
    print("The element is present in the tuple")
else:
    print("The element is not present in the tuple")