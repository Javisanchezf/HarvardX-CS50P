def main():
    twttr(input("Input: "))


def twttr(phrase):
    for _ in phrase:
        if _.lower() not in ["a", "e", "i", "o", "u"]:
            print(_, end="", sep="")
    print("\n", end="", sep="")


if __name__ == "__main__":
    main()
