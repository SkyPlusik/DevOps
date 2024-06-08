import pytest

from main.calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(-3, 2) == -1
    assert calc.add(0, 0) == 0
    assert calc.add(-6, -8) == -14
    assert calc.add(-3, 5) == 2
    assert calc.add(5, 9) == 14
    
def test_sub():
    assert calc.sub(-3, 2) == -5
    assert calc.sub(0, 0) == 0
    assert calc.sub(-6, -8) == 2
    assert calc.sub(6, 5) == 1
    assert calc.sub(5, 9) == -4

def test_multy():
    assert calc.multy(-3, 2) == -6
    assert calc.multy(0, 0) == 0
    assert calc.multy(4, 2) == 8
    assert calc.multy(-6, -5) == 30
    assert calc.multy(5, -1) == -5

def test_div():
    assert calc.div(-6, 2) == -3
    assert calc.div(8, 2) == 4
    assert calc.div(30, -5) == -6
    assert calc.div(-5, -1) == 5

def test_div_fail():
    with pytest.raises(ZeroDivisionError):
        calc.div(6, 0)
