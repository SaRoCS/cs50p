import inflect

p = inflect.engine()
names = []

while True:
    try:
        names.append(input())
    except EOFError:
        break

print("Adieu, adieu, to " + p.join(names))