import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = "(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
    if time := re.search(r"^" + regex + " to " + regex + "$", s.strip()):
        from_time = time_conversion(time.group(1), time.group(2), time.group(3))
        to_time = time_conversion(time.group(4), time.group(5), time.group(6))
        return f"{from_time} to {to_time}"
    raise ValueError


def time_conversion(h, min, x):
    if x == "AM":
        hour = f"{int(h):02}"
        if h == "12":
            hour = "00"
    else:
        hour = f"{int(h)+12}"
        if h == "12":
            hour = "12"
    if min == None:
        minute = "00"
    else:
        minute = f"{int(min):02}"
    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()
