mytuple = eval(input("Enter a tuple: "))
x = int(input("Enter the amount of repetitions: "))
newtuple = ()
for element in mytuple:
    for i in range(x):
        newtuple += (element, )

print(newtuple)