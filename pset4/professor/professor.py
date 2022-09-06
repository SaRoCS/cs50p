import random


def main():
    level = get_level()
    points = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 3

        while tries > 0:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                continue
            else:
                if answer == x + y:
                    points += 1
                    break
                else:
                    print("EEE")
                    tries -= 1
        if tries == 0:
            print(f"{x} + {y} = {x+y}")
    print(f"Score: {points}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 0 < level < 4:
                return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
    else:
        raise ValueError

    return x


if __name__ == "__main__":
    main()