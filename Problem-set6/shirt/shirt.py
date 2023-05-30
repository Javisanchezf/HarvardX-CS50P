import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    format = [".jpg", ".jpeg", ".png"]
    input_image = os.path.splitext(sys.argv[1])
    output_image = os.path.splitext(sys.argv[2])
    if output_image[1].lower() not in format:
        sys.exit("Invalid output")
    elif input_image[1].lower() != output_image[1].lower():
        sys.exit("Input and output have different extensions")
    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, mask=shirt)
            input_cropped.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
