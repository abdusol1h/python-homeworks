dictionary = {
    'name': 'Alice', 
    'age': 26,
    'certificates': {'ielts' : 8.0, 'sat': 1500},
    'city': 'New York', 
    'job': 'Software Engineer'
}

isNested = False

for value in dictionary.values():
    if type(value) == dict:
        isNested = True

if isNested:
    print("The dictionary is nested dictionary")
else:
    print("The dictionary is not nested")