mytuple = eval(input("Enter a tuple: "))
unique_sorted = sorted(set(mytuple))

if len(unique_sorted) < 2:
    print("The second smallest element does not exist.")
else:
    second_smallest = unique_sorted[1]
    print(f"The second smallest element of the tuple is {second_smallest}")