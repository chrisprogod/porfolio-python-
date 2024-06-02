ad = 50
while ad > 0:
    print("Amount Due:", ad)
    ic = int(input("Insert Coin: "))
    if ic == 10 or ic == 25 or ic == 5:
        ad = ad - ic
    else:
        continue
if ic > ad:
    print("Change Owed:", ic - (ic + ad))
