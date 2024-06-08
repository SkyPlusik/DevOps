import pytest

from code/calculator import Calculator

calc = Calculator

@pytest.mark.parametrize(
    ('a', 'b', 'result'), [
        (-3, 2, -1),
        (0, 0, 0),
        (-6, -8, -14),
        (-3, 5, 2),
        (5, 9, 14),
    ]
)
def test_add(a, b, result):
    assert calc.add(a, b) == result

@pytest.mark.parametrize(
    ('a', 'b', 'result'), [
        (-3, 2, -5),
        (0, 0, 0),
        (-6, -8, 2),
        (6, 5, 1),
        (5, 9, -4),
    ]
)
def test_sub(a, b, result):
    assert calc.sub(a, b) == result

@pytest.mark.parametrize(
    ('a', 'b', 'result'), [
        (-3, 2, -6),
        (0, 0, 0),
        (4, 2, 8),
        (-6, -5, 30),
        (5, -1, -5),
    ]
)
def test_multy(a, b, result):
    assert calc.multy(a, b) == result

@pytest.mark.parametrize(
    ('a', 'b', 'result'), [
        (-6, 2, -3),
        (8, 2, 4),
        (30, -5, -6),
        (-5, -1, 5),
    ]
)
def test_div(a, b, result):
    assert calc.div(a, b) == result

def test_div_fail():
    with pytest.raises(ZeroDivisionError):
        calc.div(6, 0)
