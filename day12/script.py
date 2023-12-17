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
    def __init__(self, input = []):
        self.input = input

    def get_nonogrid(self, record):
        group_lengths = [len(group) for group in re.findall(r"(#+)",record)]
        return group_lengths
    
    def extract_condition(self, record):
        condition = re.match(r"([#.?]+)",record).group(1)
        return condition
    
    def extract_check(self, record):
        check = [int(x) for x in re.findall(r"(\d+)", record)]
        return check
    
    def find_arrangements(self, record):
        condition = self.extract_condition(record)
        check = self.extract_check(record)
        possible_arrangements = strings.all_replacements(condition,'?',['.','#'])
        acceptable_arrangements = [x for x in possible_arrangements if self.get_nonogrid(x) == check]
        return acceptable_arrangements
   
    def part_1(self):
        result = sum(len(self.find_arrangements(x)) for x in self.input)
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