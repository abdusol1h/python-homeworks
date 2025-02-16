dictionary = {
    'name': 'Alice', 
    'age': 26,
    'city': 'New York', 
    'job': 'Software Engineer'
}
key = input("Enter the key you want to remove: ")
if key in dictionary:
    dictionary.pop(key)
    print(dictionary)
else:
    print("The key does not exist in the dictionary")