def main():
    playback(input("Say something: "))


def playback(phrase):
    print(phrase.replace(" ", "..."))


if __name__ == "__main__":
    main()
