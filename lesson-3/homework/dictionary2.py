dictionary = {
    'name': 'Alice', 
    'age': 26,
    'city': 'New York', 
    'job': 'Software Engineer'
}
key = input("What are you looking for? ")

if key in dictionary:
    print("The key is present in the dictionary.")
else:
    print("The key is not present in the dictionary.")