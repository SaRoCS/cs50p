x = input("Greeting: ").strip().lower()

if x[0:5] == "hello":
    print("$0")
elif x[0] == "h":
    print("$20")
else:
    print("$100")