from um import count

testing = {
    "yummy": 0,
    "um": 1,
    "UM? um!": 2,
    "um um um mu mu mu": 3,
    "Um, with um. symbols ,um .um": 4,
    "1 UM 2 uM 3 Um 4 um 5 this not but um yes": 5,
    "UMumumuuuumumum muum mu un": 0,
}


def test_basic():
    for test in testing:
        assert count(test) == testing[test]
