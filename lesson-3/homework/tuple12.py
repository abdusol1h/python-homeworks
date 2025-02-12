mytuple = eval(input("Enter a tuple: "))
unique_sorted = sorted(set(mytuple), reverse=True)

if len(unique_sorted) < 2:
    print("The second largest element does not exist.")
else:
    second_largest = unique_sorted[1]
    print(f"The second largest element of the tuple is {second_largest}")