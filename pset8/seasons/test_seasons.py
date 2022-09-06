from seasons import get_date, convert
import pytest
from datetime import date

def test_get_date():
    tests = ["", "January 1, 2000", "1/1/2000", "01/01/2000", "2000/01/01", "2000/1/1", "01-01-2000", "2000-1-1"]
    for test in tests:
        with pytest.raises(SystemExit):
            get_date(test)

    assert type(get_date("2000-01-02")) == date

#tests only good for 2022-06-16
def test_convert():
    assert convert(date(2021, 6, 16)) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert(date(2020, 6, 16)) == "One million, fifty-one thousand, two hundred minutes"