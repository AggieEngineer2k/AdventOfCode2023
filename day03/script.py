# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser

# Define the puzzle solver.
class Solver: 
    def __init__(self, input):
        self.input = input

    def day_1(self):
        result = None
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