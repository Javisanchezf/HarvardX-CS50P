def main():
    camelCase(input("camelCase: "))


def camelCase(phrase):
    for _ in phrase:
        if _.isupper():
            print("_", _.lower(), end="", sep="")
        else:
            print(_, end="")
    print("\n", end="")


if __name__ == "__main__":
    main()
