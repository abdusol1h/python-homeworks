n = int(input("Enter a number: "))
if (n % 3 == 0) & (n % 5 == 0):
    print("The number is divisible by both 3 and 5")
elif (n % 3 == 0):
    print("The number is divisible by 3, but not by 5")
elif (n % 5 == 0):
    print("The number is divisible by 5, but not by 3")
else:
    print("The number is not divisible by 3 or 5")