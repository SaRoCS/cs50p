from twttr import shorten

def test_vowels():
    assert shorten("Banana") == "Bnn"
    assert shorten("eel") == "l"
    assert shorten("diD") == "dD"
    assert shorten("bOom") == "bm"
    assert shorten("FLU") == "FL"


def test_other_chars():
    assert shorten("12om3") == "12m3"
    assert shorten(",.;mo!?") == ",.;m!?"
    assert shorten("@#$%^&*()-_=+[]{}\\|'\"<>/`~") == "@#$%^&*()-_=+[]{}\\|'\"<>/`~"


def test_all():
    assert shorten("A quick brown fox jumps over the lazy dog") == " qck brwn fx jmps vr th lzy dg"