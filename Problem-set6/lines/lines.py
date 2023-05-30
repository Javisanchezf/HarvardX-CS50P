import sys


def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        exit(1)
    if not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        exit(1)
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
    i = 0
    for _ in lines:
        if not _.strip().startswith("#") and _.strip():
            i += 1
    print(i)


if __name__ == "__main__":
    main()
