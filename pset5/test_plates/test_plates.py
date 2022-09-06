from plates import is_valid

def test_first_letters():
    assert is_valid("Shhhh") == True
    assert is_valid("12shh") == False
    assert is_valid("s1hhh") == False
    assert is_valid("1shhh") == False
    assert is_valid("1234") == False


def test_length():
    assert is_valid("s") == False
    assert is_valid("shhhhhh") == False
    assert is_valid("shhh") == True


def test_punctuation():
    assert is_valid("sh,.;:") == False
    assert is_valid("sh!_-/") == False
    assert is_valid("sh@#%^") == False
    assert is_valid("sh)+=[") == False
    assert is_valid("sh{}<>") == False
    assert is_valid("sh'?&$") == False
    assert is_valid("sh*(]|") == False
    assert is_valid("sh`~") == False


def test_numbers():
    assert is_valid("shh50") == True
    assert is_valid("sh50h") == False
    assert is_valid("shh05") == False