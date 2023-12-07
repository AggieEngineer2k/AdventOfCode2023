# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
from enum import Enum
import re

ranks = [
    '1', # 0
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'T',
    'J',
    'Q',
    'K',
    'A' # 13
] 

class CamelCardHand:
    cards : str
    bid : int
    def __init__(self, hand : str):
        m = re.match(r'(?P<cards>\w+) (?P<bid>\d+)', hand)
        self.cards = m['cards']
        self.bid = int(m['bid'])
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.cards == self.cards and other.bid == self.bid
        return NotImplemented
    def __gt__(self, other):
        pass
    # Implementing because I'm not sure if Python will infer these correctly or not.
    def __lt__(self, other):
        eq = self.__eq__(other)
        gt = self.__gt__(other)
        if eq is NotImplemented or gt is NotImplemented:
            return NotImplemented
        return not eq and not gt
    def __le__(self, other):
        eq = self.__eq__(other)
        gt = self.__gt__(other)
        if eq is NotImplemented or gt is NotImplemented:
            return NotImplemented
        return eq or not gt
    def __ne__(self, other):
        x = self.__eq__(other)
        if x is NotImplemented:
            return NotImplemented
        return not x
    def __ge__(self, other):
        eq = self.__eq__(other)
        gt = self.__gt__(other)
        if eq is NotImplemented or gt is NotImplemented:
            return NotImplemented
        return eq or gt

def compare_camel_card_hands(left : CamelCardHand, right : CamelCardHand) -> int:
    for x in range(5):
        left_rank = ranks.index(left.cards[x])
        right_rank = ranks.index(right.cards[x])
        if left_rank > right_rank:
            return 1
        if right_rank < left_rank:
            return -1
    return 0

# Define the puzzle solver.
class Solver:
    hands : "list(CamelCardHand)"
    def __init__(self, input = []):
        self.input = input
    def parse_input(self, input : "list(str)" = None):
        self.hands = []
        use_input = input or self.input
        for line in use_input:
            self.hands.append(CamelCardHand(line))
    def part_1(self):
        result = None
        print(f"Part 1: {result}")
    def part_2(self):
        result = None
        print(f"Part 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
solver.parse_input()
# Solve the puzzles.
solver.part_1()
solver.part_2()