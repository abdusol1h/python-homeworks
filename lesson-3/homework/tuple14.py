element = input("Enter an element: ")

if element.isdigit():
    element = int(element)
elif element.replace(".", "", 1).isdigit():
    element = float(element)

mytuple = (element, )
print(mytuple)