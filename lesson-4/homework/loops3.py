text = input("Enter a string: ")
vowels = {'a', 'e', 'i', 'o', 'u'}
result = []
counter = 0
used_with_underscore = set()

i = 0
while i < len(text):
    result.append(text[i])
    counter += 1

    if counter % 3 == 0 and i < len(text) - 1 and text[i] not in used_with_underscore:
        if text[i] in vowels:
            j = i + 1
            while j < len(text) and text[j] in vowels:
                result.append(text[j])
                j += 1

            if j < len(text):
                result.append(text[j])
                result.append('_')
                used_with_underscore.add(text[j])
                i = j
        else:
            result.append('_')
            used_with_underscore.add(text[i])

    i += 1

if result[-1] == '_':
    result.pop()

print(''.join(result))