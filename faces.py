def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return(text)

def main():
    user_inp = input("")
    conv_user_inp = convert(user_inp)
    print(conv_user_inp)

main()