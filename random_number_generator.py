import random

error = 1
Nums = []

print("GENERATE RANDOM NUMBERS")
num1 = input("FROM: ")
num2 = input("TO: ")
if int(num1) >= int(num2):
    print("ERROR! You CANNOT COMPLETE THIS OPERATION")
    exit()

else:

    x = input("HOW MANY NUMBERS WOULD YOU LIKE TO GENERATE: ")
    for i in range(int(x)):
        number = random.randint(int(num1), int(num2))
        Nums.append(number)
print(Nums)

y = len(Nums)

while error == 1:
    SaveFile = input("Do you want to save? (y/n): ")
    if SaveFile == "y":
        print("\nYour list has bee saved in a file named RGN_list in your venv library")
        for x in range(y):
            f = open("RGN_list.txt", "w+")
            f.write(str(Nums))

        error = 0
    elif SaveFile == "n":
        error = 0
        print("\nThis list will not be saved")
    else:
        print("error_001")