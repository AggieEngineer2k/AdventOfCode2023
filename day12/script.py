# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
import re
from common import strings

# Define the puzzle solver.
class Solver:
    arrangements : dict

    def __init__(self, input = []):
        self.input = input
        self.arrangements = {}

    def get_nonogrid(self, record):
        group_lengths = [len(group) for group in re.findall(r"(#+)",record)]
        return group_lengths
    
    def extract_condition(self, record):
        condition = re.match(r"([#.?]+)",record).group(1)
        return condition
    
    def extract_check(self, record):
        check = [int(x) for x in re.findall(r"(\d+)", record)]
        return check
    
    def find_possible_arrangements(self, record) -> list:
        # Cache possible arrangements of the condition.
        condition = self.extract_condition(record)
        if condition not in list(self.arrangements.keys()):
            possible_arrangements = list(strings.all_replacements(condition,'?',['.','#']))
            logging.debug(f"Caching {len(possible_arrangements)} possible arrangements for '{condition}'.")
            self.arrangements[condition] = possible_arrangements
        return self.arrangements[condition]
    
    def find_acceptable_arrangements(self, record) -> list:
        # Filter on arrangements that satisfy the check.
        condition = self.extract_condition(record)
        possible_arrangements = self.find_possible_arrangements(condition)
        check = self.extract_check(record)
        acceptable_arrangements = [x for x in possible_arrangements if self.get_nonogrid(x) == check]
        logging.debug(f"Found {len(acceptable_arrangements)}/{len(possible_arrangements)} acceptable arrangements for '{condition}' matching '{check}'.")
        return acceptable_arrangements
   
    def part_1(self):
        for x in self.input:
            _ = self.find_possible_arrangements(x)
        result = 0
        for x in self.input:
            acceptable_arrangements = self.find_acceptable_arrangements(x)
            result += len(acceptable_arrangements)
        print(f"Part 1: {result}")

    def part_2(self):
        result = None
        print(f"Part 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
# Solve the puzzles.
solver.part_1()
solver.part_2()