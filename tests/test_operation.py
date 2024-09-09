from src.math_operations import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(-1,1) == 0


def test_sub():
    assert subtract(1,3) == -2
    assert subtract(5,2) == 3
    