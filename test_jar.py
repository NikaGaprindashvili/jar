from jar import Jar
import pytest

def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0
    assert str(jar) == ""

    with pytest.raises(ValueError):
        jar = Jar(-1)

    with pytest.raises(ValueError):
        jar = Jar("abc")

def test_deposit():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.size == 2
    assert str(jar) == "🍪🍪"

    with pytest.raises(ValueError):
        jar.deposit(-1)

    with pytest.raises(ValueError):
        jar.deposit(4)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(2)
    jar.withdraw(1)
    assert jar.size == 1
    assert str(jar) == "🍪"

    with pytest.raises(ValueError):
        jar.withdraw(-1)

    with pytest.raises(ValueError):
        jar.withdraw(2)

def test_size():
    jar = Jar(5)
    assert jar.size == 0
    jar.deposit(2)
    assert jar.size == 2
    jar.withdraw(1)
    assert jar.size == 1
    jar.withdraw(1)
    assert jar.size == 0

def test_str():
    jar = Jar(5)
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪"
