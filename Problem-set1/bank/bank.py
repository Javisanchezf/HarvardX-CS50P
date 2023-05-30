def bank():
    answer = input("Greeting: ")
    print("$", end="")
    if answer.lower().strip().startswith("hello"):
        print("0")
    elif answer.lower().strip()[0] == "h":
        print("20")
    else:
        print("100")


def main():
    bank()


if __name__ == "__main__":
    main()
