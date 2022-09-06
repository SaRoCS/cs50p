import sys
import csv
from tabulate import tabulate

#test arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        reader = list(csv.reader(file))
        header = reader[0]
        table = reader[1:]
        print(tabulate(table, header, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")