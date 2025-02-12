mytuple = eval(input("Enter a tuple: "))
element = input("Enter the element you are looking for: ")

if element.isdigit():
    element = int(element)
elif element.replace(".", "", 1).isdigit():
    element = float(element)

indices = []

for i in range(len(mytuple)):
    if mytuple[i] == element:
        indices.append(i)

print(indices)        