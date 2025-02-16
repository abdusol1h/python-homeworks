dictionary = {
    'name': 'Alice', 
    'age': 26,
    'city': 'New York', 
    'job': 'Software Engineer'
}
key = input("What are you looking for? ")
print(dictionary.get(key, "Not found"))