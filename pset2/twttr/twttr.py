text = input("Input: ")
txt = ""

for letter in text:
    if letter.lower() not in "aeiou":
        txt += letter

print("Output: " + txt)