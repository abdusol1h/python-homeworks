start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: ")) + 1

list = []
for i in range(end-start):
    list.append(i+1)

print(list)