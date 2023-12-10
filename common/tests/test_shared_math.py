import pytest
from common.math import *

@pytest.mark.parametrize("number,expected", [
    (1,{1}),
    (2,{1,2}),
    (3,{1,3}),
    (4,{1,2,4}),
])
def test_factors(number : int, expected : set):
    actual = factors(number)
    assert actual == expected

@pytest.mark.parametrize("numbers,expected", [
    ([2,3],6),
    ([1,2,3],6)
])
def test_lcm(numbers : "list(int)", expected : int):
    actual = lcm(numbers)
    assert actual == expected