from bank import value

def test_hello():
    greetings = ["hello", "hello, world"]

    for greeting in greetings:
        assert value(greeting) == 0


def test_h():
    greetings = ["h", "hI", "How are you"]

    for greeting in greetings:
        assert value(greeting) == 20


def test_else():
    greetings = ["Good morning!", "ugh"]

    for greeting in greetings:
        assert value(greeting) == 100