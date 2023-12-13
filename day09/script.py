# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
import re

# Define the puzzle solver.
class Solver:
    histories : "list(list(int))"

    def __init__(self, input = []):
        self.input = input

    def parse_input(self, input : "list(str)" = None):
        self.histories = []
        input_to_parse = input or self.input
        for line in input_to_parse:
            numbers = [int(x) for x in re.findall(r"(-?\d+)",line)]
            self.histories.append(numbers)

    def extrapolate_next_history(self, numbers : "list(int)") -> int:
        logging.debug(f"Extrapolating from numbers: {numbers}")
        if all([x==0 for x in numbers]):
            return 0
        else:
            differences = [numbers[x + 1] - numbers[x] for x in range(len(numbers) - 1)]
            logging.debug(f" Differences: {differences}")
            extrapolated = self.extrapolate_next_history(differences)
            logging.debug(f" Extrapolated: {extrapolated}")
            if extrapolated == 0:
                return numbers[-1]
            else:
                return numbers[-1] + extrapolated
    
    def part_1(self):
        extrapolations = [self.extrapolate_next_history(self.histories[x]) for x in range(len(self.histories))]
        result = sum(extrapolations)
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