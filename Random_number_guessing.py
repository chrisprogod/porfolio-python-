from random import randrange
x = input("What would like the range to be in: ")
n = randrange(int(x))
if n < 10:
    print("The range has to be above 10.")
else:
    print("Have fun guessing the Mystery Number!\nType what you think is the correct number below:")
    while True:
        v = int(input())
        if n == v:
            print('You guessed the Mystery Number!')
            break
        print('Smaller' if (n < v) else 'Bigger')

