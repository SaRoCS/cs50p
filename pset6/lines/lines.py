import sys

#test arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")

count = 0

#try to open file
try:
    with open(sys.argv[1]) as file:
        for line in file:
            line = line.lstrip()
            #test line
            if line == "" or line.startswith("#"):
                continue
            else:
                count += 1
        print(count)
except FileNotFoundError:
    sys.exit("File does not exist")