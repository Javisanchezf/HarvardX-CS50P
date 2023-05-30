def main():
    check_hour(convert(input("What time is it? ")))


def check_hour(time):
    if time > 24 or time < 0:
        print("Error: Out of limits")
        exit(1)
    elif time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    time = time.replace(":", " ").split()
    try:
        h = float(time[0])
        m = float(time[1])
    except ValueError:
        print("Error: Valid formats: ##:## / ##:## a.m / ##:## p.m.")
        exit(1)
    if len(time) == 2:
        decimal_time = h + m / 60
    elif len(time) == 3:
        if time[2].lower() == "a.m.":
            decimal_time = h + m / 60
        elif time[2].lower() == "p.m.":
            decimal_time = 12 + h + m / 60
        else:
            print("Error: Valid formats: ##:## / ##:## a.m / ##:## p.m.")
            exit(1)
    else:
        print("Error: Invalid number of arguments")
        exit(1)
    return decimal_time


if __name__ == "__main__":
    main()
