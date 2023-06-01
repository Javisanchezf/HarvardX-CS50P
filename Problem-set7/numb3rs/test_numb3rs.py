from numb3rs import validate


def test_valid_ip():
    assert validate("192.168.0.1") == True
    assert validate("10.0.0.10") == True
    assert validate("172.16.0.254") == True


def test_invalid_ip():
    assert validate("256.168.0.1") == False
    assert validate("25.168.4.a") == False
    assert validate("10.0.0.256") == False
