str = input("Enter a string: ")
start = input("Starts with: ")
end = input("Ends with: ")
words = str.split()
if ((words[0] == start) & (words[-1] == end)):
    print(True)
else:
    print(False)