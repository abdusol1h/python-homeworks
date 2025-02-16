dictionary = {
    'name': 'Alice', 
    'age': 26,
    'city': 'New York', 
    'job': 'Software Engineer'
}
key = input("Enter the key you are looking for: ")
if key in dictionary:
    print(key + ":", dictionary[key])
else:
    print("The key does not exist")