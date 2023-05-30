import requests
import sys


def main():
    if len(sys.argv) < 2:
        print("Missing command-line argument")
        exit(1)
    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        price = float(requests.get(url).json()["bpi"]["USD"]["rate_float"]) * float(
            sys.argv[1]
        )
        print(f"${price:,.4f}")
    except requests.RequestException:
        print("Request Exception.")
        exit(1)
    except ValueError:
        print("Command-line argument is not a number.")
        exit(1)


if __name__ == "__main__":
    main()
