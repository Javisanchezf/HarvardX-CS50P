def calculator(x, y, operator):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "/":
        return x / y
    elif operator == "*":
        return x * y
    else:
        return "Error: Invalid operand."


def interpreter():
    while 1:
        values = input("File name: ").split()
        if len(values) == 3:
            try:
                x = float(values[0])
                y = float(values[2])
                operator = values[1]
                break
            except ValueError:
                print("Error: Input must be a number.")
        else:
            print("Error: Invalid input.")
    print(calculator(x, y, operator))


def main():
    interpreter()


if __name__ == "__main__":
    main()
