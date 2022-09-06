months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    #check format month day, year
    if "," in date:
        date = date.replace(",", "").split(" ")
        #check valid month
        if date[0] in months:
            month = months.index(date[0]) + 1
            #check only three items and if they are ints
            if len(date) == 3:
                try:
                    day = int(date[1])
                    year = int(date[2])
                except ValueError:
                    pass
                #validate length of month and year
                if 1 <= day <= 31 and year > 0:
                    break
    elif "/" in date:
        for char in date:
            if char.isspace():
                break
        else:
            date = date.split("/")
            #check only 3 items
            if len(date) == 3:
                for i in range(len(date)):
                    try:
                        date[i] = int(date[i])
                    except ValueError:
                        break
                else:
                    #validate the month and day and year
                    if 1 <= date[0] <= 12 and 1 <= date[1] <= 31 and date[2] > 0:
                        month, day, year = date
                        break

print(f"{year}-{month:02}-{day:02}")