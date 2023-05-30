from bank import value


def test_basic():
    assert value("hello world") == 0
    assert value("Hello world") == 0
    assert value("how you doing?") == 20
    assert value("How you doing?") == 20
    assert value("what's happening?") == 100
    assert value("What's happening?") == 100


def test_final():
    testing = "abcdefgijklmnopqrstuvwxyz"
    testing2 = testing.upper()
    for _ in testing:
        assert value(_) == 100
    for _ in testing2:
        assert value(_) == 100
    assert value("h") == 20
    assert value("H") == 20
    assert value("helloabcd") == 0
    assert value("HELLOabcd") == 0
