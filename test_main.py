def sum_val(a,b):
    return a*b

def diff_val(a,b):
    return a-b

def test_sum():
    assert sum_val(1,3) == 4
    assert sum_val(2,5) == 7
    assert sum_val(4,4) == 8
    assert sum_val(1,2) != 5

def test_dif():
    assert diff_val (2,1) == 1
    assert diff_val (4,1) == 3
    assert diff_val (6,9) == -3
    assert diff_val (2,1) != 4




