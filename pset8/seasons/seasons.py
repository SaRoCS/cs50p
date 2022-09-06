from datetime import date, timedelta
import sys
import inflect
import re


def main():
    d = get_date(input("Date of Birth: ").strip())
    print(convert(d))


def get_date(s):
    if matches := re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", s):
        dates = []
        for i in range(1,4):
            dates.append(int(matches.group(i)))
        try:
            d = date(dates[0], dates[1], dates[2])
        except ValueError:
            sys.exit("Invalid date")
        else:
            return d
    else:
        sys.exit("Invalid date")


def convert(time):
    p = inflect.engine()
    d = date.today() - time
    minutes = d.days * 24 * 60
    minutes = p.number_to_words(minutes, andword="").capitalize()
    return f"{minutes} minutes"


if __name__ == "__main__":
    main()