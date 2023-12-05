# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
import re, math

# Define the puzzle solver.
class Solver:
    def __init__(self, input = []):
        self.input = input

    def parse_input(self, input : "list(str)") -> "list":
        cards = {}
        for card in input:
            sections = re.split(r':|\|',card)
            card_number = int(re.search(r'(\d+)',sections[0]).group(0))
            winning = [x for x in re.findall(r'(\d+)',sections[1])]
            have = [x for x in re.findall(r'(\d+)',sections[2])]
            matches = len([x for x in set(winning) & set(have)])
            points = 0
            if matches > 0:
                points = int(math.pow(2, matches - 1))
            cards[card_number] = {
                'quantity': 1,
                'winning': winning,
                'have': have,
                'matches': matches,
                'points': points
            }
        return cards

    def part_1(self):
        cards = self.parse_input(self.input)
        result = sum([cards[x]['points'] for x in cards])
        print(f"Part 1: {result}")

    def part_2(self):
        cards = self.parse_input(self.input)
        for i in range(len(cards)):
            card_number = i + 1
            quantity = cards[card_number]['quantity']
            matches = cards[card_number]['matches']
            logging.debug(f"Inspecting card {card_number}, which has quantity {quantity} and {matches} matches.")
            for j in range(matches):
                card_number_to_increase = card_number + 1 + j
                original_quantity = cards[card_number_to_increase]['quantity']
                new_quantity = original_quantity + quantity
                logging.debug(f"Increasing card {card_number_to_increase} quantity from {original_quantity} to {new_quantity}.")
                cards[card_number_to_increase]['quantity'] = new_quantity
        result = sum([cards[x]['quantity'] for x in cards])
        print(f"Part 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
# Solve the puzzles.
solver.part_1()
solver.part_2()