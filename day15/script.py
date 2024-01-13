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
        boxes = [dict() for x in range(256)]
        for step in re.split(',',self.input):
            label, operation, focal_length = re.match(r"(\w+)([-=])(\d+)?",step).groups()
            box_number = self.algorithm(label)
            box = boxes[box_number]
            if operation == '=':
                #logging.debug(f"Adding/updating lens '{label}' with focal length {focal_length} to box #{box_number}.")
                box[label] = focal_length
            if operation == '-':
                if label in box:
                    #logging.debug(f"Removing lens '{label}' from box #{box_number}.")
                    box.pop(label)
                else:
                    #logging.debug(f"Couldn't remove lens '{label}' from box #{box_number}.")
                    pass
        result = 0
        for box_number in range(len(boxes)):
            box = boxes[box_number]
            result += sum([(1 + box_number) * (index + 1) * (int(focal_length)) for index, (label, focal_length) in enumerate(box.items())])
        print(f"Part 2: {result}")

# Parse the input file.
input = InputParser.parse_line(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
# Solve the puzzles.
solver.part_1()
solver.part_2()