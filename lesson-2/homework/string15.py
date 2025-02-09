str = input("Enter a sentence: ")
words = str.split()
acronym = ''
for w in words:
    acronym += w[0]

print(acronym)