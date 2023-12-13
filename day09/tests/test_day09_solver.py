import pytest
from day09.script import Solver

example_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
0 -1 2 -3"""

def test_Solver_parse_input():
    solver = Solver()
    x = example_input.split('\n')
    solver.parse_input(x)
    assert len(solver.histories) == 4
    assert solver.histories[0] == [0,3,6,9,12,15]
    assert solver.histories[1] == [1,3,6,10,15,21]
    assert solver.histories[2] == [10,13,16,21,30,45]
    assert solver.histories[3] == [0,-1,2,-3]

@pytest.mark.parametrize('numbers,expected', [
    ([0,3,6,9,12,15],18),
    ([1,3,6,10,15,21],28),
    ([10,13,16,21,30,45],68)
])
def test_Solver_extrapolate_next_history(numbers : "list(int)", expected : int):
    solver = Solver()
    actual = solver.extrapolate_next_history(numbers)
    assert expected == actual

@pytest.mark.parametrize('numbers,expected', [
    ([0,3,6,9,12,15],-3),
    ([1,3,6,10,15,21],0),
    ([10,13,16,21,30,45],5)
])
def test_Solver_extrapolate_previous_history(numbers : "list(int)", expected : int):
    solver = Solver()
    actual = solver.extrapolate_previous_history(numbers)
    assert expected == actual