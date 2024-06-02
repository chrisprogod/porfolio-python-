def main():
    inp = input("Input: ")
    output = convert(inp)
    print("Output:", output)


def convert(inp):
    out = []
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in inp:
        if i in vowels:
            i =("")
            out.append(i)
        else:
            out.append(i)
    return (''.join(out))

main()
