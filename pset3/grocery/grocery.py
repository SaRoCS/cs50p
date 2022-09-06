groceries = {}

while True:
    try:
        item = input().upper()
    except EOFError:
        print()
        break
    if item in groceries:
        groceries[item] += 1
    else:
        groceries[item] = 1

for item in sorted(groceries.keys()):
    print(groceries[item], item)