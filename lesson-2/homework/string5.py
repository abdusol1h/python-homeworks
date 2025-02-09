str = input("Enter a string: ")
consonants = 0
vowels = 0
for i in str:
    if i.lower() in 'aiueo':
        vowels += 1
    else:
        consonants += 1

print(f"{vowels=}")
print(f"{consonants=}")