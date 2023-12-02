# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Parse input file.
import re
from common.input_parser import InputParser

# Define the script to solve the puzzle.
class Solver:
    input : "list(str)"

    # These are the replacements to make.
    replacements : dict = [
        ("one"  , "1"),
        ("two"  , "2"),
        ("three", "3"),
        ("four" , "4"),
        ("five" , "5"),
        ("six"  , "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine" , "9")
    ]
    
    def __init__(self, input : str = []):
        self.input = input

    # Returns the first and last digits in the string, converted to a two digit numeric value.
    def findFirstAndLastDigits(self, string : str) -> int:
        matches = re.findall(r"\d", string)
        return int(matches[0] + matches[-1])
    
    # Returns the first and last digits in the string, converted to a two digit numeric value, after peforming text replacements.
    def findFirstAndLastReplacedDigits(self, string : str) -> int:
        copy = string

        # Replace the earliest occurrence of a number.
        indices = [len(copy) if copy.find(x[0]) == -1 else copy.find(x[0]) for x in self.replacements]
        minIndex = indices.index(min(indices))
        if indices[minIndex] != len(copy):
            copy = copy.replace(self.replacements[minIndex][0], self.replacements[minIndex][1], 1)
        firstDigit = re.findall(r"\d", copy)[0]

        # Replace the latest occurrence of a number.
        copy = string
        copy = copy[::-1]
        indices = [len(copy) if copy.find(x[0][::-1]) == -1 else copy.find(x[0][::-1]) for x in self.replacements]
        minIndex = indices.index(min(indices))
        if indices[minIndex] != len(copy):
            copy = copy.replace(self.replacements[minIndex][0][::-1], self.replacements[minIndex][1], 1)
        copy = copy[::-1]
        lastDigit = re.findall(r"\d", copy)[-1]

        result = int(firstDigit + lastDigit)
        return result
    
    def day_1(self):
        numbers = [self.findFirstAndLastDigits(string) for string in self.input]
        result = sum(numbers)
        print(f"Day 1: {result}")

    def day_2(self):
        numbers = [self.findFirstAndLastReplacedDigits(string) for string in self.input]
        result = sum(numbers)
        print(f"Day 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
# Solve the puzzles.
solver.day_1()
solver.day_2()