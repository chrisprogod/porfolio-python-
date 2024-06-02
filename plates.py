def vanity():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    count = 0
    not_legal = [" ", ",", ".", ":", "'", '"']
    F2C = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for i in s:
        count += 1
        if i in not_legal:
            return False
        if count <= 2 and i in F2C:
            return False
    if count < 2 or count > 6:
        return False
    for x in s:
        if x.isalpha() == False:
            if x == "0":
                return False
            else:
                break
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i + 1].isalpha():
            return False
    return True

vanity()
