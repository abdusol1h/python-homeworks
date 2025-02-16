mytuple = eval(input("Enter a tuple: "))
length = len(mytuple)
isPalindrome = True
for i in range(length // 2):
    if mytuple[i] != mytuple[length-(i+1)]:
        isPalindrome = False

if isPalindrome:
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome.")