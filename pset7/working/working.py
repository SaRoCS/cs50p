import re

def main():
    print(convert(input("Hours:")))


def convert(s):
    if matches := re.search(r"^([1-9][0-2]?(?::[0-5][0-9])?) (A|P)M to ([1-9][0-2]?(?::[0-5][0-9])?) (A|P)M", s.strip()):
        times = [[matches.group(1), matches.group(2)], [matches.group(3), matches.group(4)]]
        converted = []
        for time in times:
            try:
                hour, minutes = time[0].split(":")
            except ValueError:
                hour = time[0]
                minutes = None

            hour = int(hour)

            if hour == 12:
                hour = 0

            if time[1] == "P":
                hour += 12

            if minutes:
                 converted.append(f"{hour:02}:{minutes}")
            else:
                converted.append(f"{hour:02}:00")

        return f"{converted[0]} to {converted[1]}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()