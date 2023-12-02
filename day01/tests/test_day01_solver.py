import pytest
from day01.script import Solver

@pytest.mark.parametrize('string,expected', [
    ("1abc2",12),
    ("pqr3stu8vwx",38),
    ("a1b2c3d4e5f",15),
    ("treb7uchet",77)
])
def test_solver_findFirstAndLastDigits(string : str, expected : int):
    solver = Solver()
    actual = solver.findFirstAndLastDigits(string)
    assert actual == expected

@pytest.mark.parametrize('string,expected', [
    ("two1nine",29),
    ("eightwothree",83),
    ("abcone2threexyz",13),
    ("xtwone3four",24),
    ("4nineeightseven2",42),
    ("zoneight234",14),
    ("7pqrstsixteen",76),
    # The following two test cases came from https://www.reddit.com/r/adventofcode/comments/1884fpl/2023_day_1for_those_who_stuck_on_part_2/
    ("eighthree",83),
    ("sevenine",79)
])
def test_solver_findFirstAndLastReplacedDigits(string : str, expected : int):
    solver = Solver()
    actual = solver.findFirstAndLastReplacedDigits(string)
    assert actual == expected