from bank import value

def test_return_zero():
    assert value("hello") == 0
    assert value("HELLO darling") == 0
    assert value("Hello") == 0

def test_return_twenty():
    assert value("Hi") == 20
    assert value("hey") == 20

def test_return_hundred():
    assert value("Monrning!") == 100
    assert value("Whatsup!") == 100
