from working import convert
import pytest


testing = {
    "12:00 AM to 01:00 PM": "00:00 to 13:00",
    "09:30 AM to 10:45 AM": "09:30 to 10:45",
    "11:00 PM to 01:30 AM": "23:00 to 01:30",
    "05:15 PM to 05:15 PM": "17:15 to 17:15",
    "12 AM to 12 PM": "00:00 to 12:00",
    "12:00 AM to 12:00 PM": "00:00 to 12:00",
}


def test_convert():
    for test in testing:
        assert convert(test) == testing[test]


def test_value_error():
    with pytest.raises(ValueError):
        convert("10AM 5PM")
    with pytest.raises(ValueError):
        convert("15:00 AM to 42:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
