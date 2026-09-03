from app import add, subtract, multiply, divide


def test_add():
    assert add(10, 20) == 30


def test_subtract():
    assert subtract(30, 10) == 20


def test_multiply():
    assert multiply(6, 7) == 42


def test_divide():
    assert divide(20, 5) == 4


def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError:
        pass
