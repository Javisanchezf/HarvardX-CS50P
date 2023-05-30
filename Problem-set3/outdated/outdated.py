months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while 1:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                mm, dd, yyyy = date.split("/")
            elif "," in date:
                mmdd, yyyy = date.split(", ")
                mm, dd = mmdd.split(" ")
                mm = months.index(mm.title()) + 1
            if not (int(mm) > 0 and int(mm) < 13 and int(dd) < 31 and int(dd) > 0):
                raise ValueError
            print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
            break
        except (
            AttributeError,
            ValueError,
            NameError,
            KeyError,
            EOFError,
            KeyboardInterrupt,
        ):
            pass


if __name__ == "__main__":
    main()
