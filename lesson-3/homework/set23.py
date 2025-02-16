import random

size = int(input("Enter the size of the random set: "))
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

random_set = set(random.sample(range(start, (end+1)), size))
print(random_set)