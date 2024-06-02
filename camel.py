def main():
    camel_c = input("camelCase: ")
    snake_c = convert(camel_c)
    print("snake_case:", snake_c)
    
def convert(camel_c):
    snake = []
    for i in camel_c:
        if i.islower() == False:
            i = ("_"+i.lower())
            snake.append(i)
        else:
            snake.append(i)
    return(''.join(snake))

main()
