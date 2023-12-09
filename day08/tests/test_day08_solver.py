import pytest
from day08.script import Solver

input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

def test_Solver_parse_input():
    solver = Solver()
    i = input.split('\n')
    solver.parse_input(i)
    assert solver.directions == "RL"
    assert len(solver.nodes) == 7
    assert list(solver.nodes.keys()) == ["AAA","BBB","CCC","DDD","EEE","GGG","ZZZ"]
    assert solver.nodes["AAA"] == {
        "L": "BBB",
        "R": "CCC"
    }
    assert solver.nodes["ZZZ"] == {
        "L": "ZZZ",
        "R": "ZZZ"
    }
