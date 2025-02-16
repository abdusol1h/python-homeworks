dictionary = {
    'name': 'Alice', 
    'age': 26,
    'city': 'New York', 
    'job': 'Software Engineer'
}
element = input("What value are you looking for? ")

if element.isdigit():
    element = int(element)
elif element.replace(".", "", 1).isdigit():
    element = float(element)

counter = 0

for item in dictionary.values():
    if item == element:
        counter += 1

print(f"There are {counter} occurances of this value in this dictionary.")