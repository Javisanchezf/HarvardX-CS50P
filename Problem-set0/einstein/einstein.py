def main():
    while 1:
        try:
            m = int(input("Enter mass: "))
            print(einstein(m))
            break
        except ValueError:
            print("Error, enter only numbers.")


def einstein(m):
    return m * (300000000**2)


if __name__ == "__main__":
    main()
