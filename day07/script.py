# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
import re
from collections import Counter

part_1_ranks = [
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
part_2_ranks = [
    'J', # 0
    '1', 
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'T',
    'Q',
    'K',
    'A' # 13
]
is_part_1 = True

class CamelCardHand:
    cards : str
    pretend_cards : str
    bid : int
    def __init__(self, hand : str):
        m = re.match(r'(?P<cards>\w+) (?P<bid>\d+)', hand)
        self.cards = m['cards']
        self.bid = int(m['bid'])
        self.pretend_cards = self.cards    
    def replace_wildcards(self):
        pass
    def __str__(self) -> str:
        return f"'{self.cards}' ({self.pretend_cards}) {self.bid}"
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.cards == self.cards and other.bid == self.bid
        return NotImplemented
    def __gt__(self, other):
        ranks = part_1_ranks if is_part_1 else part_2_ranks
        # Counters produce dictionaries of the counts of each rank in the hands.
        self_counter = dict(Counter([*self.pretend_cards]))
        other_counter = dict(Counter([*other.pretend_cards]))
        # Counts are just the values from the counters; just he cardinalities.
        self_counts = list(self_counter.values())
        other_counts = list(other_counter.values())
        # Count down from five-of-a-kind down to singles to return which hand is a winner.
        for x in range(5,0,-1):
            if self_counts.count(x) > other_counts.count(x):
                return True
            elif self_counts.count(x) < other_counts.count(x):
                return False
            # Check for Full House
            elif x == 3 and self_counts.count(3) == 1 and other_counts.count(3) == 1 and self_counts.count(2) > other_counts.count(2):
                return True
            elif x == 3 and self_counts.count(3) == 1 and other_counts.count(3) == 1 and self_counts.count(2) < other_counts.count(2):
                return False
            # Compare lexicographically when the hands have the same winning condition.
            elif self_counts.count(x) == other_counts.count(x) and self_counts.count(x) > 0 and other_counts.count(x) > 0:
                for y in range(5):
                    if ranks.index(self.cards[y]) > ranks.index(other.cards[y]):
                        return True
                    elif ranks.index(self.cards[y]) < ranks.index(other.cards[y]):
                        return False

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
    def get_winnings(self):
        result = 0
        for i in range(len(self.hands)):
            hand = self.hands[i]
            logging.debug(f"{i:3}: {list(dict(Counter([*hand.cards])).values())} {hand}")
            result = result + ((i + 1) * hand.bid)
        return result
    def part_1(self):
        self.hands.sort()
        result = self.get_winnings()
        print(f"Part 1: {result}")
    def part_2(self):
        is_part_1 = False
        for x in self.hands:
            x.replace_wildcards()
        self.hands.sort()
        result = self.get_winnings()
        print(f"Part 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
solver.parse_input()
# Solve the puzzles.
solver.part_1()
solver.part_2()