import pytest
from day07.script import Solver,CamelCardHand

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

@pytest.mark.parametrize('hands,expected', [
    (
        [CamelCardHand('33332 0'),CamelCardHand('2AAAA 0')],
        [CamelCardHand('2AAAA 0'),CamelCardHand('33332 0')]
    ),
    (
        [CamelCardHand('32T3K 765'),CamelCardHand('T55J5 684'),CamelCardHand('KK677 28'),CamelCardHand('KTJJT 220'),CamelCardHand('QQQJA 483')],
        [CamelCardHand('32T3K 765'),CamelCardHand('KTJJT 220'),CamelCardHand('KK677 28'),CamelCardHand('T55J5 684'),CamelCardHand('QQQJA 483')]
    ),
    # Need unit test(s) for Full House
])
def test_Solver_sort(hands : "list(CamelCardHand)", expected : "list(CamelCardHand)"):
    hands.sort()
    assert hands == expected

def test_Solver_get_winnings():
    solver = Solver()
    solver.parse_input(input.split('\n'))
    solver.hands.sort()
    actual = solver.get_winnings()
    assert actual == 6440