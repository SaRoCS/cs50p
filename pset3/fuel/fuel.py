while True:
    #try convert to int or return to top
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
    except ValueError:
        continue
    #ensure will create a percentage
    if x <= y:
        try:
            percent = x / y
        except ZeroDivisionError:
            pass
        else:
            break

percent = round(percent * 100)

if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{percent}%")


