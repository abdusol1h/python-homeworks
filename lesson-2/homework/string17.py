str = input("Enter a string: ")
x = len(str)
for i in range(x):
    if(str[i] in 'aiueo'):
        str = str.replace(str[i], '*')

print(str)