import sys
import csv

#test arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

after = []

try:
    with open(sys.argv[1]) as file:
        #read file and split names
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(", ")
            row = {"first" : first, "last" : last, "house" : row["house"]}
            after.append(row)
except FileNotFoundError:
    sys.exit("Could not open file")
#write file
with open(sys.argv[2], "w") as file:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for row in after:
        writer.writerow(row)