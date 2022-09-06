import random

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass
    else:
        if n > 0:
            break

x = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess < x:
            print("Too small!")
        elif guess > x:
            print("Too large!")
        else:
            print("Just right!")
            break