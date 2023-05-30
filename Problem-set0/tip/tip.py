def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    try:
        return float(d.strip().replace("$", ""))
    except ValueError:
        print("Error: Input must be a number.")


def percent_to_float(p):
    try:
        return float(p.strip().replace("%", "")) / 100
    except ValueError:
        print("Error: Input must be a number.")


if __name__ == "__main__":
    main()
