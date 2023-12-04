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
            card_number = int(re.find(r'(\d+)',sections[0]))
            winning_numbers = [x for x in re.findall(r'(\d+)',sections[1])]
            have_numbers = [x for x in re.findall(r'(\d+)',sections[2])]
            matches = len([x for x in set(winning_numbers) & set(have_numbers)])
            points = 0
            if matches > 0:
                points = int(math.pow(2, matches - 1))
            cards[] = {}

    def get_card_score(self, card : str) -> int:
        sections = re.split(r':|\|',card)
        winning_numbers = [x for x in re.findall(r'(\d+)',sections[1])]
        have_numbers = [x for x in re.findall(r'(\d+)',sections[2])]
        matches = len([x for x in set(winning_numbers) & set(have_numbers)])
        if matches == 0:
            return 0
        else:
            return int(math.pow(2, matches - 1))

    def day_1(self):
        result = sum([self.get_card_score(x) for x in self.input])
        print(f"Day 1: {result}")

    def day_2(self):
        result = None
        print(f"Day 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
# Solve the puzzles.
solver.day_1()
solver.day_2()