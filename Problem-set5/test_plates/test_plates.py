from plates import is_valid


def test_basic_valid_plates():
    assert is_valid("CS50") == 1
    assert is_valid("ECTO88") == 1
    assert is_valid("NRVOUS") == 1


def test_basic_invalid_plates():
    assert is_valid("CS05") == 0
    assert is_valid("CS50P") == 0
    assert is_valid("PI3.14") == 0
    assert is_valid("H") == 0
    assert is_valid("OUTATIME") == 0


def test_without_beginning_alphabetical():
    assert is_valid("11111") == 0
    assert is_valid(".....") == 0
    assert is_valid("-----") == 0
