keys = ['name', 'age', 'city']
values = ['John', 23, 'London']
dictionary = dict.fromkeys(keys, 'Unknown')
for i in range(len(dictionary)):
    dictionary[keys[i]] = values[i]

print(dictionary)