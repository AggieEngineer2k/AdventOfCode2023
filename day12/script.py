# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
import re

# Define the puzzle solver.
# Following https://www.bing.com/videos/riverview/relatedvideo?q=advent+of+code+2023+day+12&mid=73D0A428926E008801EB73D0A428926E008801EB&FORM=VIRE
class Solver:
    def __init__(self, input = []):
        self.input = input

    def parse_record(self, record : str) -> tuple:
        condition, check = record.split()
        return condition, list(map(int, check.split(',')))

    def count_arrangements(self, condition : str, check : "list(int)") -> int:
        # Return a valid arrangement if we reached the end of the condition with an empty check.
        if condition == "":
            return 1 if check == [] else 0
        
        # Return a valid arrangement if we reached the end of the check with no remaining broken springs left to count.
        # Assume any remaining ? to be working springs.
        if check == []:
            return 0 if '#' in condition else 1
        
        number_of_arrangements = 0

        # For leading '.' character.
        if condition[0] in '.?':
            # Add arrangements without the leading character.
            number_of_arrangements += self.count_arrangements(condition[1:], check)

        # For leading '#' character.
        if condition[0] in '#?':
            # Ensure enough contiguous broken '#' or unknown '?' (i.e. not working '.') springs left at front of condition to satisfy first check,
            # and the condition is either exactly enough remaining springs OR is NOT followed by another broken spring.
            if len(condition) >= check[0] and '.' not in condition[:check[0]] and (len(condition) == check[0] or condition[check[0]] != '#'):
                # Add the number of arrangements of the condition with the first check removed (and the succeeding '.') and the checks with the first removed.
                number_of_arrangements += self.count_arrangements(condition[check[0] + 1:], check[1:])

        return number_of_arrangements
   
    def part_1(self):
        result = 0
        for record in self.input:
            condition, check = self.parse_record(record)
            result += self.count_arrangements(condition, check)
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