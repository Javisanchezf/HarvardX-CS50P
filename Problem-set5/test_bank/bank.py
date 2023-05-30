def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(answer):
    if answer.lower().strip().startswith("hello"):
        return 0
    elif answer.lower().strip()[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
