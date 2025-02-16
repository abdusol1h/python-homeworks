dictionary = {
    'name': 'Alice', 
    'age': 26,
    'job_city': 'New York',
    'city': 'New York', 
    'job': 'Software Engineer'
}

list = []
for value in dictionary.values():
    if value not in list:
        list.append(value)

print("There are", len(list), "unique values in this dictionary")