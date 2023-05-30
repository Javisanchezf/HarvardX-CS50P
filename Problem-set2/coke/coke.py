def main():
    coke()


def coke():
    c = 50
    while c > 0:
        print("Amount Due:", c)
        n = take_int("Insert coin: ")
        if n == 5 or n == 10 or n == 25 or n == 50 or n == 100:
            c -= n
    print("Change Owed:", -c)


def take_int(prompt):
    while 1:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error, enter only numbers. Try again: ")


if __name__ == "__main__":
    main()
