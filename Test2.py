n = int(input())
if n % 2 != 0 and (n < 20):
    print("Weird")
elif n == 4 or n == 2:
    print("Not Weird")
elif n % 2 == 0 and n >= 6 and n <= 20:
    print("Weird")
elif (n % 2 == 0) and (n > 20):
    print("Not Weird")

