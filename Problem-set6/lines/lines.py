import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    i = 0
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
        for _ in lines:
            if not _.strip().startswith("#") and _.strip():
                i += 1
        print(i)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
