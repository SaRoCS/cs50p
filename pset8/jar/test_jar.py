from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(4)
    assert jar.capacity == 4

    tests = ["a", -1, 0]
    for test in tests:
        with pytest.raises(ValueError):
            Jar(test)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    jar.deposit(1)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(16)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    jar.withdraw(4)
    assert jar.size == 1

    with pytest.raises(ValueError):
        jar.withdraw(5)