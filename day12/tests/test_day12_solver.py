import pytest
from day12.script import Solver

@pytest.mark.parametrize('record,expected', [
    ('#.#.### 1,1,3','#.#.###'),
    ('.#...#....###. 1,1,3','.#...#....###.'),
    ('.#.###.#.###### 1,3,1,6','.#.###.#.######'),
    ('####.#...#... 4,1,1','####.#...#...'),
    ('#....######..#####. 1,6,5','#....######..#####.'),
    ('.###.##....# 3,2,1','.###.##....#')
])
def test_Solver_extract_condition(record : str, expected : str):
    solver = Solver()
    actual = solver.extract_condition(record)
    assert actual == expected

@pytest.mark.parametrize('record,expected', [
    ('#.#.### 1,1,3',[1,1,3]),
    ('.#...#....###. 1,1,3',[1,1,3]),
    ('.#.###.#.###### 1,3,1,6',[1,3,1,6]),
    ('####.#...#... 4,1,1',[4,1,1]),
    ('#....######..#####. 1,6,5',[1,6,5]),
    ('.###.##....# 3,2,1',[3,2,1])
])
def test_Solver_extract_check(record : str, expected : "list(int)"):
    solver = Solver()
    actual = solver.extract_check(record)
    assert actual == expected

@pytest.mark.parametrize('record,expected', [
    ('#.#.###',[1,1,3]),
    ('.#...#....###.',[1,1,3]),
    ('.#.###.#.######',[1,3,1,6]),
    ('####.#...#...',[4,1,1]),
    ('#....######..#####.',[1,6,5]),
    ('.###.##....#',[3,2,1])
])
def test_Solver_get_nonogrid(record : str, expected : "list(int)"):
    solver = Solver()
    actual = solver.get_nonogrid(record)
    assert actual == expected

@pytest.mark.parametrize('record,expected', [
    ('???.### 1,1,3',1),
    ('.??..??...?##. 1,1,3',4),
    ('?#?#?#?#?#?#?#? 1,3,1,6',1),
    ('????.#...#... 4,1,1',1),
    ('????.######..#####. 1,6,5',4),
    ('?###???????? 3,2,1',10)
])
def test_Solver_find_arrangements(record : str, expected : int):
    solver = Solver()
    actual = len(solver.find_arrangements(record))
    assert actual == expected