import random

number = random.randint(-20, 40)

temperature = number
print("The temperature is " + str(number) + "°")

if temperature > 26:
    print("It's really hot today.")
    print("You should bring a water bottle.")
elif temperature > 20:
    print("It's a nice day today.")
elif temperature > -5:
    print("It's quite cold outside today")
else:
    print("It's really cold")
print("\nDone")

