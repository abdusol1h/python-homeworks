isPrime = True

for i in range(1, 100):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
    if isPrime:
        print(i)