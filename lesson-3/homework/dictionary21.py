dictionary = {
    'name': 'Alice', 
    'city': 'New York', 
    'job': 'Software Engineer'
}

sorted_dict = dict(sorted(dictionary.items(), key = lambda item: item[1]))

print(sorted_dict)