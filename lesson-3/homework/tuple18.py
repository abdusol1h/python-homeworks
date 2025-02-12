mytuple = eval(input("Enter a tuple: "))

start = int(input("Enter the start of subtuple(inclusive): "))
end = int(input("Enter the end of subtuple(exclusive): "))

min_element = min(mytuple[start:(end)])
print(f"{min_element=}")