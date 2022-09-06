def main():
    time = input("What time is it? ").strip()
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    total = float(hours) + (float(minutes) / 60)
    return total


if __name__ == "__main__":
    main()