import random
num = random.randint(1, 100)
conditions = ['Y', 'YES', 'y', 'yes', 'ok']
condition = True
while condition:
    for i in range(10):
        guess = int(input("Guess: "))
        if guess == num:
            print("Congrats, you found the number!")
            break
        elif guess > num:
            print("Too high!")
        elif guess < num:
            print("Too low!")
    again = input("Press Y, YES, y, yes or ok to play again. ")

    if again not in conditions:
        condition = False
    else:
        num = random.randint(1, 100)