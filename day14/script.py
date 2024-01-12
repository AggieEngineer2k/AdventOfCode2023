# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
from common.grid import Grid
import re

ROCK = 'O'
CUBE = '#'
SPACE = '.'

class Solver:
    grid : Grid

    def __init__(self, input = []):
        self.input = input

    def initialize_from_input(self):
        self.grid = Grid()
        self.grid.initialize_from_strings(self.input)

    def roll_north(self, grid : Grid = None):
        grid = grid or self.grid
        for c in range(grid.width):
            #logging.debug(f"Column {c}")
            column = ''.join(grid.get_column(c))
            #logging.debug(f"from: {column}")
            column = column.replace(ROCK,'0')
            column = column.replace(SPACE,'1')
            groups = re.split(CUBE, column)
            rolled = CUBE.join([''.join(sorted(group)) for group in groups])
            rolled = rolled.replace('0',ROCK)
            rolled = rolled.replace('1',SPACE)
            #logging.debug(f"  to: {rolled}")
            grid.replace_column(c,[*rolled])
            #weight += sum([i for i,c in enumerate(reversed(rolled),1) if c == 'O'])
    
    def roll_south(self, grid : Grid = None):
        grid = grid or self.grid
        for c in range(grid.width):
            #logging.debug(f"Column {c}")
            column = ''.join(grid.get_column(c))
            #logging.debug(f"from: {column}")
            column = column.replace(ROCK,'1')
            column = column.replace(SPACE,'0')
            groups = re.split(CUBE, column)
            rolled = CUBE.join([''.join(sorted(group)) for group in groups])
            rolled = rolled.replace('1',ROCK)
            rolled = rolled.replace('0',SPACE)
            #logging.debug(f"  to: {rolled}")
            grid.replace_column(c,[*rolled])
            #weight += sum([i for i,c in enumerate(rolled,1) if c == 'O'])
    
    def roll_west(self, grid : Grid = None):
        grid = grid or self.grid
        for r in range(grid.height):
            #logging.debug(f"Row {r}")
            row = ''.join(grid.get_row(r))
            #logging.debug(f"from: {row}")
            row = row.replace(ROCK,'0')
            row = row.replace(SPACE,'1')
            groups = re.split(CUBE, row)
            rolled = CUBE.join([''.join(sorted(group)) for group in groups])
            rolled = rolled.replace('0',ROCK)
            rolled = rolled.replace('1',SPACE)
            #logging.debug(f"  to: {rolled}")
            grid.replace_row(r,[*rolled])
            #weight += sum([i for i,c in enumerate(reversed(rolled),1) if c == 'O'])
    
    def roll_east(self, grid : Grid = None):
        grid = grid or self.grid
        for r in range(grid.height):
            #logging.debug(f"Row {r}")
            row = ''.join(grid.get_row(r))
            #logging.debug(f"from: {row}")
            row = row.replace(ROCK,'1')
            row = row.replace(SPACE,'0')
            groups = re.split(CUBE, row)
            rolled = CUBE.join([''.join(sorted(group)) for group in groups])
            rolled = rolled.replace('1',ROCK)
            rolled = rolled.replace('0',SPACE)
            #logging.debug(f"  to: {rolled}")
            grid.replace_row(r,[*rolled])
            #weight += sum([i for i,c in enumerate(rolled,1) if c == 'O'])

    def get_weight(self, grid : Grid = None) -> int:
        grid = grid or self.grid
        return sum([sum([i for i,c in enumerate(reversed(grid.get_column(col)),1) if c == 'O']) for col in range(grid.width)])
  
    def part_1(self):
        self.initialize_from_input()
        self.roll_north()
        result = self.get_weight()
        print(f"Part 1: {result}")

    def part_2(self):
        cache = {}
        cycles = 1000000000
        self.initialize_from_input()
        cache[str(self.grid)] = 0
        for x in range(1, cycles + 1):
            self.roll_north()
            self.roll_west()
            self.roll_south()
            self.roll_east()
            if(str(self.grid) in cache):
                logging.debug(f"State after cycle {x} matched state from cycle {cache[str(self.grid)]}.")
                remaining_steps = cycles - x
                cycle_length = x - cache[str(self.grid)]
                remainder = remaining_steps % cycle_length
                logging.debug(f"Remainder of cycle length {cycle_length} after {remaining_steps} steps is {remainder}.")
                if remainder == 0:
                    print(f"Found a cycle that will repeat {remaining_steps / cycle_length} times.")
                    break
            else:
                cache[str(self.grid)] = x
        result = self.get_weight()
        print(f"Part 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
# Solve the puzzles.
solver.part_1()
solver.part_2()