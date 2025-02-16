dictionary = {
    'name': 'Alice', 
    'age': 26,
    'city': 'New York', 
    'job': 'Software Engineer'
}

inverted = dict(zip(dictionary.values(), dictionary.keys()))
print(inverted)