name = input("camelCase: ").strip()

for letter in name:
    if letter.isupper():
        name = name.replace(letter, "_" + letter.lower())

print("snake_case: " + name)