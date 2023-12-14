import pytest
from day10.script import Solver

simple_input = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

complex_input = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

@pytest.mark.parametrize('input,expected', [
    (simple_input,9),
    (complex_input,17)
])
def test_Solver_find_length(input : str, expected : int):
    solver = Solver(input.split('\n'))
    solver.parse_input()
    actual = solver.find_length()
    assert actual == expected

@pytest.mark.parametrize('input,expected', [
("""...........
.S-------7.
.|F-----7|.
.||OOOOO||.
.||OOOOO||.
.|L-7OF-J|.
.|II|O|II|.
.L--JOL--J.
.....O.....""",4),
("""..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........""",4),
(""".F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...""",8)
])
def test_Solver_find_tiles_inside_path(input : str, expected : int):
    solver = Solver(input.split('\n'))
    solver.parse_input()
    path = [*solver.find_path()]
    inside_tiles = [*solver.find_tiles_inside_path(path)]
    actual = len(inside_tiles)
    assert actual == expected

# @pytest.mark.parametrize('numbers,expected', [
#     ([0,3,6,9,12,15],18),
#     ([1,3,6,10,15,21],28),
#     ([10,13,16,21,30,45],68)
# ])
# def test_Solver_extrapolate_next_history(numbers : "list(int)", expected : int):
#     solver = Solver()
#     actual = solver.extrapolate_next_history(numbers)
#     assert expected == actual

# @pytest.mark.parametrize('numbers,expected', [
#     ([0,3,6,9,12,15],-3),
#     ([1,3,6,10,15,21],0),
#     ([10,13,16,21,30,45],5)
# ])
# def test_Solver_extrapolate_previous_history(numbers : "list(int)", expected : int):
#     solver = Solver()
#     actual = solver.extrapolate_previous_history(numbers)
#     assert expected == actual