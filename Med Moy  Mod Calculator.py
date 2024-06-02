import statistics
numbers = []

list_size = int(input("Quelle est la longueur de votre liste :"))

for x in range(list_size):
    n = int(input("Entrez votre nombre : "))
    numbers.append(n);



def calMed():
    sorted_list = sorted(numbers)
    med = statistics.median(sorted_list)
    print("La mediane de votre liste est de", med)



def calMoy():
    listsum = sum(numbers)
    avrage = listsum / list_size
    print("La moyenne de votre liste est de", avrage)



def calMod():
    print("\nVotre liste:", numbers)
    mode = statistics.mode(numbers)
    print("Le mode de votre liste est de", mode)

calMod()
calMed()
calMoy()
