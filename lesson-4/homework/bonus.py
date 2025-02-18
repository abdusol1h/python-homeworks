import random
options = ['rock', 'paper', 'scissors']
me, comp = 0, 0
while (True):
    c_choice = random.choice(options)
    choice = input("Enter your choice: ")
    if choice == 'rock':
        if c_choice == 'paper':
            comp += 1
            print(c_choice, 'I won')
        elif c_choice == 'scissors':
            me += 1
            print(c_choice, 'You won')
        else:
            print("Draw")
    elif choice == 'paper':
        if c_choice == 'scissors':
            comp += 1
            print(c_choice, 'I won')
        elif c_choice == 'rock':
            me += 1
            print(c_choice, 'You won')
        else:
            print("Draw")
    elif choice == 'scissors':
        if c_choice == 'rock':
            comp += 1
            print(c_choice, 'I won')
        elif c_choice == 'paper':
            me += 1
            print(c_choice, 'You won')
        else:
            print("Draw")
    print(f"You vs me: {me} - {comp}")

    if me == 5:
        print("You won")
        break
    elif comp == 5:
        print("You lost")
        break