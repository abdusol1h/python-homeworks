def factors(num):
    for i in range(num):
        if num % (i+1) == 0:
            print(f"{i+1} is a factor of {num}.")

num = int(input("Enter a positive integer: "))
if num > 0:
    factors(num)
else:
    print("Invalid input.") 