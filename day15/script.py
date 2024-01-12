# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
import re

class Solver:
    def __init__(self, input = ''):
        self.input = input

    def algorithm(self, step : str) -> int:
        result = 0
        for character in [*step]:
            result = ((result + ord(character)) * 17) % 256
        return result

    def part_1(self):
        result = sum([self.algorithm(x) for x in re.split(',',self.input)])
        print(f"Part 1: {result}")

    def part_2(self):
        result = None
        print(f"Part 2: {result}")

# Parse the input file.
input = InputParser.parse_line(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
# Solve the puzzles.
solver.part_1()
solver.part_2()