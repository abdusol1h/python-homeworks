mytuple = eval(input("Enter a tuple: "))

start = int(input("Enter the start of subtuple(inclusive): "))
end = int(input("Enter the end of subtuple(exclusive): "))

max_element = max(mytuple[start:(end)])
print(f"{max_element=}")