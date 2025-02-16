set = set()
start = int(input("Start: "))
end = int(input("End: "))

for i in range(end-(start-1)):
    i += start
    set.add(i)

print(set)