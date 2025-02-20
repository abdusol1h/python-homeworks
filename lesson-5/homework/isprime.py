import math

def is_prime(n):
    isPrime = True
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            isPrime = False
    
    print(isPrime)
    
num = int(input("Enter a number: "))
is_prime(num)