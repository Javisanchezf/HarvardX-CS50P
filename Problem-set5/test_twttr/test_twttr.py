from twttr import shorten


def test_output_twitter():
    assert shorten("Twitter") == "Twttr"


def test_output_whats_your_name():
    assert shorten("What's your name?") == "Wht's yr nm?"


def test_output_cs50():
    assert shorten("CS50") == "CS50"


def test_finaltest():
    assert (
        shorten("QWERTYUIOPASDFGHJKLÑZXCVBNMwertyuiopasdfghjklñzxcvbnm1234567890")
        == "QWRTYPSDFGHJKLÑZXCVBNMwrtypsdfghjklñzxcvbnm1234567890"
    )
