import pytest
from day02.script import Solver

@pytest.mark.parametrize('game,expected', [
    ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",{
        "id": 1,
        "red": 4,
        "green": 2,
        "blue": 6
    }),
    ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",{
        "id": 2,
        "red": 1,
        "green": 3,
        "blue": 4
    }),
    ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",{
        "id": 3,
        "red": 20,
        "green": 13,
        "blue": 6
    }),
    ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",{
        "id": 4,
        "red": 14,
        "green": 3,
        "blue": 15
    }),
    ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",{
        "id": 5,
        "red": 6,
        "green": 3,
        "blue": 2
    })
])
def test_solver_learn(game : str, expected : dict):
    solver = Solver()
    actual = solver.learn(game)
    assert actual == expected

@pytest.mark.parametrize('learned,expected', [
    ({
        "id": 1,
        "red": 4,
        "green": 2,
        "blue": 6
    },True),
    ({
        "id": 2,
        "red": 1,
        "green": 3,
        "blue": 4
    },True),
    ({
        "id": 3,
        "red": 20,
        "green": 13,
        "blue": 6
    },False),
    ({
        "id": 4,
        "red": 14,
        "green": 3,
        "blue": 15
    },False),
    ({
        "id": 5,
        "red": 6,
        "green": 3,
        "blue": 2
    },True)
])
def test_solver_possible(learned : dict, expected : bool):
    solver = Solver()
    actual = solver.possible(learned)
    assert actual == expected

@pytest.mark.parametrize('learned,expected', [
    ({
        "id": 1,
        "red": 4,
        "green": 2,
        "blue": 6
    },48),
    ({
        "id": 2,
        "red": 1,
        "green": 3,
        "blue": 4
    },12),
    ({
        "id": 3,
        "red": 20,
        "green": 13,
        "blue": 6
    },1560),
    ({
        "id": 4,
        "red": 14,
        "green": 3,
        "blue": 15
    },630),
    ({
        "id": 5,
        "red": 6,
        "green": 3,
        "blue": 2
    },36)
])
def test_solver_power(learned : dict, expected : int):
    solver = Solver()
    actual = solver.power(learned)
    assert actual == expected