def main():
    print(shorten(input("Input: ")))


def shorten(phrase):
    shortened = []
    for _ in phrase:
        if _.lower() not in ["a", "e", "i", "o", "u"]:
            shortened.append(_)
    return "".join(shortened)


if __name__ == "__main__":
    main()
