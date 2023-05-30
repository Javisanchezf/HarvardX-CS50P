def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s_len = len(s)
    if s_len > 6 or s_len < 2:
        return 0
    if not s[0].isalpha() or not s[1].isalpha():
        return 0
    for _ in range(s_len):
        if s[_].isdigit():
            if s[_] == "0":
                return 0
            while _ < s_len:
                if not s[_].isdigit():
                    return 0
                _ += 1
            break
    return 1


if __name__ == "__main__":
    main()
