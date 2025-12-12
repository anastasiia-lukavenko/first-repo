# import pytest
# from src.calculator import add, div
# def test_add_positive_num():
#     result = add(2, 3)
#     assert result == 5

# def test_div_positive_num():
#     result = div(10, 1)
#     assert result == 10

# def test_div_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         div(10, 0)

# import pytest
# from src.calculator import add

# @pytest.mark.parametrize(
#     "a, b, expected",            
#     [
#         (1, 2, 3),              
#         (5, 5, 10),             
#         (-1, 3, 2),
#         (8, 4, 12),             
#     ]
# )
# def test_add_parametrized(a, b, expected):

#     result = add(a, b)
#     assert result == expected

# from src.calculator import sub

# @pytest.mark.parametrize(
#     "a, b, expected",
#     [
#         (5, 2, 3),
#         (10, 5, 5),
#         (-1, -1, 0),
#         (0, 5, -5),
#     ]
# )
# def test_sub_parametrized(a, b, expected):
#     result = sub(a, b)
#     assert result == expected

# from src.calculator import div

# @pytest.mark.parametrize(
#     "a, b, expected",
#     [
#         (10, 2, 5),
#         (-9, 3, -3),
#         (5, 2, 2.5),
#     ],
#     ids=["10/2=5", "-9/3=-3", "5/2=2.5"]
# )
# def test_div_ok(a, b, expected):
#     assert div(a, b) == expected

# def test_div_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         div(10,0)

# from src.calculator import Calculator
# @pytest.mark.parametrize(
#     "operation, a, b, expected",
#     [
#         ("add", 2, 3, 5),
#         ("sub", 5, 2, 3),
#         ("mul", 3, 4, 12),
#         ("div", 10, 2, 5)
#     ]
# )
# def test_calculator_operations(operation, a, b, expected):
# calc = Calculator()
# function = getattr(calc, operation)
# assert function(a, b) == expected

from src.calculator import Calculator
import pytest

@pytest.fixture
def calc():
    return Calculator()

def test_add_slow(calc):
    assert calc.add(2, 3) == 5

def test_div(calc):
    assert calc.div(10, 2) == 5

def test_sub_smoke(calc):
    assert calc.sub(5, 2) == 3

def test_mul(calc):
    assert calc.mul(3, 4) == 12

import pytest
from src.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (5, 5, 10),
    ],
    ids=["2+3=5", "-1+1=0", "5+5=10"]
)
def test_add_param_(calc, a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 8),
        (3, 7, -4),
        (0, 5, -5),
    ],
    ids=["10-2=8", "3-7=-4", "0-5=-5"]
)
def test_sub_param(calc, a, b, expected):
    assert calc.sub(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 12),
        (-2, 5, -10),
        (0, 999, 0),
    ],
    ids=["3*4=12", "-2*5=-10", "0*999=0"]
)
def test_mul_param(calc, a, b, expected):
    assert calc.mul(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (-9, 3, -3),
        (5, 2, 2.5),
    ],
    ids=["10/2=5", "-9/3=-3", "5/2=2.5"]
)
def test_div_param(calc, a, b, expected):
    assert calc.div(a, b) == expected

def test_div_by_zero_raises(calc):
    with pytest.raises(ZeroDivisionError):
        calc.div(10, 0)

