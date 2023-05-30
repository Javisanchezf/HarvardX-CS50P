def main():
    faces(input("Say something emotional: "))


def faces(phrase):
    print(phrase.replace(":)", "🙂").replace(":(", "🙁"))


if __name__ == "__main__":
    main()
