dictionary = {
    'name': 'Alice', 
    'age': 26,
    'key': 26,
    'city': 'New York', 
    'job': 'Software Engineer'
}
list = []

val = input("Enter the value you are looking for: ")

if val.isdigit():
    val = int(val)
elif val.replace(".", "", 1).isdigit():
    val = float(val)

for key, value in dictionary.items():
    if value == val:
        list.append(key)

print(list)