mytuple = eval(input("Enter a tuple: "))
element = input("Enter the element you are looking for: ")

if element.isdigit():
    element = int(element)
elif element.replace(".", "", 1).isdigit():
    element = float(element)

position = mytuple.index(element)
newtuple = mytuple[0:position] + mytuple[(position+1):]
print(newtuple)