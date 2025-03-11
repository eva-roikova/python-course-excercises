#Test for simple_math.py
import simple_math

def test_simple_math():
    assert simple_math.simple_add(1, 2) == 3
    assert simple_math.simple_sub(2,1) == 1
    assert simple_math.simple_mult(2,2) == 4
    assert simple_math.simple_div(4,2) == 2
    assert simple_math.poly_first(2, 1, 2) == 5
    assert simple_math.poly_second(2, 1, 2, 2) == 13
