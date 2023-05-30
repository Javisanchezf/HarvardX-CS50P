def main():
    while 1:
        try:
            tank = input("Tank: ").strip().split("/")
            tank = list(map(int, tank))
            if tank[1] > 0 and tank[0] <= tank[1]:
                fuel(tank)
                break
        except ValueError:
            print("Error, enter only numbers.")


def fuel(tank):
    current_tank = round(tank[0] / tank[1] * 100)
    if current_tank > 75:
        print("F")
    elif current_tank < 25:
        print("E")
    else:
        print(current_tank, "%", sep="")


if __name__ == "__main__":
    main()
