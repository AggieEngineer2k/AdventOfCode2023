import pytest
from day07.script import Solver

input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

def test_Solver_parse_input():
    solver = Solver()
    solver.parse_input(input.split('\n'))
    assert len(solver.hands) == 5
    assert solver.hands[0].cards == '32T3K'
    assert solver.hands[0].bid == 765
    assert solver.hands[1].cards == 'T55J5'
    assert solver.hands[1].bid == 684
    assert solver.hands[2].cards == 'KK677'
    assert solver.hands[2].bid == 28
    assert solver.hands[3].cards == 'KTJJT'
    assert solver.hands[3].bid == 220
    assert solver.hands[4].cards == 'QQQJA'
    assert solver.hands[4].bid == 483

def test_Solver_compare_camel_card_hands():
    solver = Solver()
    solver.parse_input(input.split('\n'))
    solver.hands.sort(key=solver.compare_camel_card_hands)
    assert solver.hands[0].cards == '32T3K'
    assert solver.hands[1].cards == 'KK677'
    assert solver.hands[2].cards == 'KTJJT'
    assert solver.hands[3].cards == 'T55J5'
    assert solver.hands[4].cards == 'QQQJA'