import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.search(r"src=\"https?://(www\.)?youtube\.com/(embed/)?(\w+)\"", s):
        return f"https://youtu.be/{link.group(3)}"
    return None


if __name__ == "__main__":
    main()
