from numb3rs import validate

def test_pattern():
    assert validate("abcd") == False
    assert validate("a.b.c.d") == False
    assert validate("1234") == False
    assert validate(",.?!;:") == False
    assert validate("1234.0") == False
    assert validate("1234.567.8.9") == False
    assert validate("1.2.3.4.5") == False


def test_value():
    assert validate("123.456.78.9") == False
    assert validate("-1.0.0.512") == False
    assert validate("127.0.0.1") == True
    assert validate("1.2.3.4") == True

