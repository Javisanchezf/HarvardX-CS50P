import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(sys.argv[1], "r") as input_file, open(
            sys.argv[2], "w"
        ) as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)
            writer.writerow(["first", "last", "house"])
            for _ in reader:
                name = _[0].split(",")
                try:
                    writer.writerow([name[1].strip(), name[0].strip(), _[1]])
                except IndexError:
                    pass

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
