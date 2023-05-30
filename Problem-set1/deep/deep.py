def deep():
    answer = input(
        "What is the Answer to the Great Question of Life, Universe, and Everithing? "
    )
    if (
        answer.strip() == "42"
        or answer.lower().strip() == "forty-two"
        or answer.lower().strip() == "forty two"
    ):
        print("Yes")
    else:
        print("No")


def main():
    deep()


if __name__ == "__main__":
    main()
