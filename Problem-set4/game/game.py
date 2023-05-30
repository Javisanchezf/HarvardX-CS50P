from random import randint


def main():
    level = randint(1, take_nbr("Level: ", 1))
    while 1:
        guess = take_nbr("Guess: ", 1)
        if guess == level:
            print("Just right!")
            break
        elif guess > level:
            print("Too large!")
        elif guess < level:
            print("Too small!")


def take_nbr(prompt, min):
    while 1:
        try:
            nbr = int(input(prompt))
            if nbr >= min:
                return nbr
        except ValueError:
            pass
        except EOFError:
            exit


if __name__ == "__main__":
    main()
