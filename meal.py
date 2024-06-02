def main():
    time = input("What time is it?: ")
    conv_time = convert(time)
    if conv_time >= 7 and conv_time <= 8:
        print("breakfast time")
    elif conv_time >= 12 and conv_time <= 13:
        print("lunch time")
    elif conv_time >= 18 and conv_time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    float_time = float(hours) + (float(minutes) / 60)
    return(float_time)


if __name__ == "__main__":
    main()
