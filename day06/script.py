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
    
    def get_distance(self, time_held : int) -> int:
        time_remaining = self.time - time_held
        distance = time_remaining * time_held
        return distance
    
    def get_options(self) -> "list(tuple)":
        for time_held in range(self.time + 1):
            distance = self.get_distance(time_held)
            yield (time_held, distance)

    def get_winning_options(self):
        winning_options = []
        for time_held in range(self.time + 1):
            distance = self.get_distance(time_held)
            if(distance > self.record):
                winning_options.append((time_held, distance))
        return winning_options
    
    def get_number_of_winning_options(self):
        # Winning options are those between the loosing options.
        total_options = self.time + 1
        loosing_options = 0
        for x in range(0, self.time, 1):
            if self.get_distance(x) > self.record:
                break
        loosing_options = loosing_options + x
        for x in range(self.time, 0, -1):
            if self.get_distance(x) > self.record:
                break
        loosing_options = loosing_options + (self.time - x)
        return total_options - loosing_options

# Define the puzzle solver.
class Solver:
    races : "list(Race)"

    def __init__(self, input = []):
        self.input = input

    def parse_input(self, input : "list(str)" = None, is_part_2 : bool = False) -> "list(Race)":
        actual_input = input or self.input
        times = [int(x) for x in re.findall(r'(\d+)',actual_input[0])]
        records = [int(x) for x in re.findall(r'(\d+)',actual_input[1])]
        if is_part_2:
            times = [int(''.join([str(x) for x in times]))]
            records = [int(''.join([str(x) for x in records]))]
        self.races = [Race(times[x],records[x]) for x in range(len(times))]
        return self.races
    
    def part_1(self):
        solver.parse_input()
        ways_to_win = []
        for x in self.races:
            ways_to_win.append(len([y for y in x.get_winning_options()]))
        result = math.prod(ways_to_win)
        print(f"Part 1: {result}")

    def part_2(self):
        solver.parse_input(is_part_2=True)
        result = self.races[0].get_number_of_winning_options()
        print(f"Part 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
# Solve the puzzles.
solver.part_1()
solver.part_2()