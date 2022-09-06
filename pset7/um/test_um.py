from um import count

def test_counting():
    assert count("um") == 1
    assert count("um um um") == 3


def test_pattern():
    assert count("hello, world") == 0
    assert count("hmm...") == 0
    assert count("hello, um, world") == 1
    assert count("Um, hello, um world") == 2


def test_words():
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("jump") == 0