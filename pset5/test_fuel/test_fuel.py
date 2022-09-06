from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert("c/c")
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    assert convert("1/2") == 50
    assert convert("4/5") == 80


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(10) == "10%"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"