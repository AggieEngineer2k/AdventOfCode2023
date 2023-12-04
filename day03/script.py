# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.WARNING)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
import re
from common.grid import Grid

# Define the puzzle solver.
class Solver:
    nonsymbol_characters = set('.0123456789')

    def __init__(self, input = []):
        self.input = input

    def extractPartNumbers(self, schematic : "list(str)") -> "list(int)":
        partNumbers = []
        grid = Grid()
        grid.initialize_from_strings(schematic)
        for token in grid.find_tokens_in_rows(r"(\d+)"):
            row = token[0]
            start = token[1]
            end = token[1] + len(token[2]) - 1
            number = token[2]
            logging.debug(f"Found {number} in row {row} starting at position {start} to {end}.")
            adjacent_characters = [x['value'] for x in grid.get_surrounding_elements(row,start,end)]
            if set(adjacent_characters).issubset(self.nonsymbol_characters):
                logging.debug(f"Number '{number}' is not a part number.")
            else:
                logging.debug(f"Number '{number}' is a part number.")
                partNumbers.append(int(number))
        return partNumbers
    
    def extract_gear_ratios(self, schematic : "list(str)") -> "list(int)":
        parts_with_gears = {}
        grid = Grid()
        grid.initialize_from_strings(schematic)
        for token in grid.find_tokens_in_rows(r"(\d+)"):
            pass

    def day_1(self):
        result = sum(self.extractPartNumbers(self.input))
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