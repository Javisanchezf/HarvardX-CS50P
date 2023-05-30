import pyfiglet
import random
import argparse

fonts = pyfiglet.FigletFont.getFonts()


def main():
    parser = argparse.ArgumentParser(
        prog="figlet", description="Ascii-art Word generator"
    )
    parser.add_argument("-f", "--format", type=str, help="Font type format.")
    format = parser.parse_args().format
    if format is None:
        format = random.choice(fonts)
    elif format not in fonts:
        exit("Invalid font type.")
    print(pyfiglet.figlet_format(input("Text to convert: "), font=format))


if __name__ == "__main__":
    main()
