dictionary1 = {
    'name': 'Alice', 
    'age': 26,
    'city': 'New York', 
    'job': 'Software Engineer'
}

dictionary2 = {
    'name': 'Bob', 
    'age': 32,
    'home': 'London', 
    'work': 'Engineer'
}

set1 = set()
set2 = set()

for key in dictionary1.keys():
    set1.add(key)

for key in dictionary2.keys():
    set2.add(key)

set3 = set1.intersection(set2)
print(set3)