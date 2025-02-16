ages = {
    'Bob': 17,
    'Alice': 20,
    'John': 18,
    'Mike': 16
}
copy = ages.copy()

for key, value in ages.items():
    if value < 18:
        copy.pop(key)

print(copy)