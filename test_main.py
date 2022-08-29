import pytest

def sum_val(a,b):
    return a+b

def diff_val(a,b):
    return a-b

def multi_val(a,b):
    return a*b


def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by Zero')
    return a / b

def test_zero_division():
    with pytest.raises(ValueError) as err:
        divide(1, 0)
    assert str(err.value) == 'Cannot divide by Zero'

def test_sum():
    assert sum_val(1,3) == 4
    assert sum_val(2,5) == 7
    assert sum_val(4,4) == 8
    assert sum_val(1,2) != 5

def test_diff():
    assert diff_val (2,1) == 1
    assert diff_val (4,1) == 3
    assert diff_val (6,9) == -3
    assert diff_val (2,1) != 4

def test_multi():
    assert multi_val (2,1) == 2
    assert multi_val (4,1) == 4
    assert multi_val (6,9) == 54
    assert multi_val (2,1) != 3








