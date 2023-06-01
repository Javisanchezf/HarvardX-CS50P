import re


def main():
    print(ip_validator(input("IPv4 Address: ")))


def validate(ip):
    if re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        sub_ips = ip.split(".")
        for sub_ip in sub_ips:
            if int(sub_ip) > 255:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
