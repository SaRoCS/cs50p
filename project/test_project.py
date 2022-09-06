from project import App, entropy, pool_size, patterns


def test_app():
    app = App()
    assert app.children["!label"]
    assert app.children["!entry"]
    assert app.children["!button"]


def test_entropy():
    e = entropy("123")
    assert e["bits"] == 9.97
    assert e["guesses"] == "500"

    e = entropy("abcd")
    assert e["bits"] == 18.80
    assert e["guesses"] == "228.5 thousand"

    e = entropy("AB")
    assert e["bits"] == 9.40
    assert e["guesses"] == "337"

    e = entropy("!@#$%^")
    assert e["bits"] == 30.00
    assert e["guesses"] == "536.9 million"

    e = entropy("AbCdE")
    assert e["bits"] == 28.5
    assert e["guesses"] == "190.1 million"

    e = entropy("ThisWasC$50")
    assert e["bits"] == 72.10
    assert e["guesses"] == "2.5 sextillion"


def test_pool_size():
    assert pool_size("abcd") == 26
    assert pool_size("a") == 26
    assert pool_size("1") == 10
    assert pool_size("A") == 26
    assert pool_size("&") == 32
    assert pool_size("abc123") == 36
    assert pool_size("aAbB") == 52
    assert pool_size("aA12") == 62
    assert pool_size("1!") == 42
    assert pool_size("@a") == 58
    assert pool_size("aA@1") == 94


def test_patterns():
    assert patterns("asdf") == "No repeated patterns found"
    assert patterns("aaaa") == 'Repeated patterns found: "a"'
    assert patterns("cs50cs50cs50") == 'Repeated patterns found: "cs50"'
    assert patterns("abcab") == 'Repeated patterns found: "ab"'
    assert patterns("cs50ics50") == 'Repeated patterns found: "cs50"'
