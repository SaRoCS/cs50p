exp = input("Expression: ").strip().lower().split(" ")
x = float(exp[0])
y = exp[1]
z = float(exp[2])

if y == "+":
    out = x + z
elif y == "-":
    out = x - z
elif y == "*":
    out = x * z
else:
    out = x / z

print(round(out, 1))