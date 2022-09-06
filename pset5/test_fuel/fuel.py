def main():
    while True:
        fraction = input("Fraction: ")
        try:
            fraction = convert(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            print(gauge(fraction))
            break


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    percent = x / y
    return round(percent * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()