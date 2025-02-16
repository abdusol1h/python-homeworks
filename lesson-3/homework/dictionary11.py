dictionary = {
    'name': 'Alice', 
    'age': 26,
    'city': 'New York', 
    'job': 'Software Engineer'
}
key = input("What key do you want to update: ")
value = input("What is the new value to be assigned: ")

if value.isdigit():
    value = int(value)
elif value.replace(".", "", 1).isdigit():
    value = float(value)

if key in dictionary:
    dictionary[key] = value
else:
    print("The key does not exist")