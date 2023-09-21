from seasons import diff

testing = {
    0: "Zero minutes",
    365: "Five hundred twenty-five thousand, six hundred minutes",
}


def test_basic():
    for test in testing:
        assert diff(test) == testing[test]
