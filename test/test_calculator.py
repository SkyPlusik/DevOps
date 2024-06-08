import pytest

from main.calculator import Calculator

def test_add():
    assert Calculator.add(-3, 2) == -1
    assert Calculator.add(0, 0) == 0
    assert Calculator.add(-6, -8) == -14
    assert Calculator.add(-3, 5) == 2
    assert Calculator.add(5, 9) == 14


def test_sub():
    assert Calculator.sub(-3, 2) == -5
    assert Calculator.sub(0, 0) == 0
    assert Calculator.sub(-6, -8) == 2
    assert Calculator.sub(6, 5) == 1
    assert Calculator.sub(5, 9) == -4


def test_multy():
    assert Calculator.multy(-3, 2) == -6
    assert Calculator.multy(0, 0) == 0
    assert Calculator.multy(4, 2) == 8
    assert Calculator.multy(-6, -5) == 30
    assert Calculator.multy(5, -1) == -5


def test_div():
    assert Calculator.div(-6, 2) == -3
    assert Calculator.div(8, 2) == 4
    assert Calculator.div(30, -5) == -6
    assert Calculator.div(-5, -1) == 5


def test_div_fail():
    with pytest.raises(ZeroDivisionError):
        Calculator.div(6, 0)
