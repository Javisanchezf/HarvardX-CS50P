from random import randint


def main():
    max, min = get_level()
    score = 0
    for _ in range(10):
        score += get_answer(max, min)
    print(f"Score: {score}")


def get_level():
    while 1:
        try:
            nbr = int(input("Level: "))
            if nbr > 0 and nbr < 4:
                max = 10**nbr - 1
                min = 10 ** (nbr - 1)
                if min == 1:
                    min = 0
                return (max, min)
        except ValueError:
            pass


def get_answer(max, min):
    tries = 0
    x = randint(min, max)
    y = randint(min, max)
    z = x + y
    while tries < 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == z:
                return 1
            raise ValueError
        except ValueError:
            print("EEE")
            tries += 1
            pass
    print(x, "+", y, "=", z)
    return 0


if __name__ == "__main__":
    main()
