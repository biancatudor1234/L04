from exercise1 import is_even, rectangle_area, double

def test_is_even():
    assert is_even(4) == True

def test_is_odd():
    assert is_even(3) == False

def test_rectangle_area():
    assert rectangle_area(3, 4) == 12

def test_double():
    assert double(5) == 10
