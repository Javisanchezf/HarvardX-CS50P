from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    try:
        birth = (date.today() - date.fromisoformat(input("Date of Birth: "))).days
        print(diff(int(birth)))
    except ValueError:
        sys.exit("Invalid date")


def diff(input):
    return f"{(p.number_to_words(input * 24 * 60, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()
