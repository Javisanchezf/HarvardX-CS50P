list = {}


def main():
    while 1:
        try:
            item = input().strip().upper()
            if item not in list:
                list[item] = 0
            list[item] += 1
        except EOFError:
            print_sorted_dic(list)
            break
        except KeyError:
            pass


def print_sorted_dic(dic):
    for value, variable in sorted(dic.items()):
        print(f"{variable} {value}")


if __name__ == "__main__":
    main()
