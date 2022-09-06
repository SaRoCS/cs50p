from working import convert
import pytest

def test_valid_formats():
    tests = ["Cat", "1234", ",.?!;:"]
    for test in tests:
        with pytest.raises(ValueError):
            convert(test)

    tests = ["9 to 5", "9-5", "9 am to 5 pm", "9 A.M. to 5 P.M.", "9:00:00 AM to 5:00:00 PM"]
    for test in tests:
        with pytest.raises(ValueError):
            convert(test)


def test_invalid_times():
    tests = ["23 AM to 5 PM", "9 AM to 0 PM", "9:78 AM to 5:36 PM"]
    for test in tests:
        with pytest.raises(ValueError):
            convert(test)


def test_converting():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"