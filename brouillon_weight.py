import re



def main():
    weight = (input("Quel ton poid en Kg: "))
    false = re.compile("[qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP/|!@#$%?&*()_+=,'éàèÀÈÉ;:^¨.]")

    if false.search(weight) == None:
        Unité = input("Sur quel planète:\nMercure\nVénus\nTerre\nMars\nJupiter\nSaturne\nUranus\nNeptune\nPluton\nLune\n: ")


        # Mercure
        if Unité == "Mercure":
            converted = int(weight) / 2.64367816091954
            print("Poid sur Mercure: " + str(converted) + " kg")

        # Vénus
        elif Unité == "Vénus":
            converted = int(weight) / 1.105769230769231
            print("Poid sur Vénus: " + str(converted) + " kg")

        # Terre
        elif Unité == "Terre":
            print("Ton poid sur Terre: " + str(weight) + " kg")

        # Mars
        elif Unité == "Mars":
            converted = int(weight) / 2.64367816091954
            print("Poid sur Mars: " + str(converted) + " kg")

        # Jupiter
        elif Unité == "Jupiter":
            converted = int(weight) * 2.526086956521739
            print("Poid sur Jupiter: " + str(converted) + " kg")

        # Saturne
        elif Unité == "Saturne":
            converted = int(weight) * 1.065217391304348
            print("Poid sur Saturne: " + str(converted) + " kg")

        # Uranus
        elif Unité == "Uranus":
            converted = int(weight) / 1.105769230769231
            print("Poid sur Uranus: " + str(converted) + " kg")

        # Neptune
        elif Unité == "Neptune":
            converted = int(weight) * 1.134782608695652
            print("Poid sur Neptune: " + str(converted) + " kg")

        # Pluton
        elif Unité == "Pluton":
            converted = int(weight) / 15.33333333333333
            print("Poid sur Pluton: " + str(converted) + " kg")

        # Lune
        elif Unité == "Lune":
            converted = int(weight) / 6.052631578947368
            print("Poid sur la Lune: " + str(converted) + " kg")
        else:
            input("Assure toi que le nom de la planète est bien épeler comme dans la liste ci-dessus.")

    else:
        print("Ton poid doit être un nombre.")
run = 1
main()
while run == 1:
    restart = input("Would you like to restart? Oui/Non: ")
    if restart == "Oui":
        main()


