import pytest
from day06.script import Solver,Race

input = """Time:      7  15   30
Distance:  9  40  200"""

def test_Solver_parse_input():
    solver = Solver()
    races = solver.parse_input(input.split('\n'))
    assert len(races) == 3
    assert races[0] == Race(7, 9)
    assert races[1] == Race(15, 40)
    assert races[2] == Race(30, 200)