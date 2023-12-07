# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
import re,math

class Race:
    time : int
    record : int

    def __init__(self, time : int, record : int):
        self.time = time
        self.record = record

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.time == self.time and other.record == self.record
        return NotImplemented
    
    def __ne__(self, other):
        x = self.__eq__(other)
        if x is NotImplemented:
            return NotImplemented
        return not x
    
    def __hash__(self):
        return hash((self.time,self.record))
    
    def get_options(self) -> "list(tuple)":
        for time_held in range(self.time + 1):
            time_remaining = self.time - time_held
            distance = time_remaining * time_held
            yield (time_held, distance)

    def get_winning_options(self):
        return [x for x in self.get_options() if x[1] > self.record]

# Define the puzzle solver.
class Solver:
    races : "list(Race)"

    def __init__(self, input = []):
        self.input = input

    def parse_input(self, input : "list(str)" = None) -> "list(Race)":
        actual_input = input or self.input
        times = [int(x) for x in re.findall(r'(\d+)',actual_input[0])]
        records = [int(x) for x in re.findall(r'(\d+)',actual_input[1])]
        self.races = [Race(times[x],records[x]) for x in range(len(times))]
        return self.races
    
    def part_1(self):
        ways_to_win = []
        for x in self.races:
            ways_to_win.append(len(x.get_winning_options()))
        result = math.prod(ways_to_win)
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