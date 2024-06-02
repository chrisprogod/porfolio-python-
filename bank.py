greet = input("Greetings: ").strip().lower()
letter1 = greet[0]

if greet[0:5] == "hello":
    print("$0")
elif letter1 == "h":
    print("$20")
else:
    print("$100")



