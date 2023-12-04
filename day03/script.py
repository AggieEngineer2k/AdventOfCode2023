# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
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
            logging.debug(f"Found {token['value']} in row {token['row']} starting at position {token['start']} to {token['end']}.")
            adjacent_characters = [x['value'] for x in grid.get_surrounding_elements(token['row'],token['start'],token['end'])]
            if set(adjacent_characters).issubset(self.nonsymbol_characters):
                logging.debug(f"Number '{token['value']}' is not a part number.")
            else:
                logging.debug(f"Number '{token['value']}' is a part number.")
                partNumbers.append(int(token['value']))
        return partNumbers
    
    def extract_gear_ratios(self, schematic : "list(str)") -> "list(int)":
        parts_with_gears = []
        grid = Grid()
        grid.initialize_from_strings(schematic)
        for token in grid.find_tokens_in_rows(r"(\d+)"):
            surrounding_gears = [x for x in grid.get_surrounding_elements(token['row'],token['start'],token['end']) if x['value'] == '*']
            if len(surrounding_gears) > 0:
                logging.debug(f"Part {token['value']} has gear(s) {[(x['row'],x['column']) for x in surrounding_gears]}.")
                parts_with_gears.append({
                    'part': token,
                    # Assumption: A part number may only be adjacent to at most 1 gear.
                    'gear': surrounding_gears[0]
                })
        for token in grid.find_tokens_in_rows(r"[*]"):
            adjacent_parts = [x for x in parts_with_gears if (x['gear']['row'],x['gear']['column']) == (token['row'],token['start'])]
            logging.debug(f"Gear at [{token['row']},{token['start']}] has {len(adjacent_parts)} parts.")
            if(len(adjacent_parts) == 2):
                yield (int(adjacent_parts[0]['part']['value']) * int(adjacent_parts[1]['part']['value']))

    def day_1(self):
        result = sum(self.extractPartNumbers(self.input))
        print(f"Day 1: {result}")

    def day_2(self):
        result = sum(self.extract_gear_ratios(self.input))
        print(f"Day 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
# Solve the puzzles.
solver.day_1()
solver.day_2()