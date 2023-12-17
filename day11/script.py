# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
from common.grid import Grid
import itertools

SPACE = '.'
GALAXY = '#'
MILLION = 'M'

# Define the puzzle solver.
class Solver:
    grid : Grid

    def __init__(self, input = []):
        self.input = input

    def parse_input(self, input : "list(str)" = None):
        input_to_parse = input or self.input
        self.grid = Grid()
        self.grid.initialize_from_strings(input_to_parse)

    def double_space(self):
        for x in range(self.grid.height-1, -1, -1):
            row_elements = self.grid.get_row(x)
            if all(element == SPACE for element in row_elements):
                self.grid.insert_row(x, SPACE)
        for x in range(self.grid.width-1, -1, -1):
            column_elements = self.grid.get_column(x)
            if all(element == SPACE for element in column_elements):
                self.grid.insert_column(x, SPACE)

    def expand_space(self):
        for x in range(self.grid.height-1, -1, -1):
            row_elements = self.grid.get_row(x)
            if all(element in [SPACE,MILLION] for element in row_elements):
                self.grid.remove_row(x)
                self.grid.insert_row(x, MILLION)
        for x in range(self.grid.width-1, -1, -1):
            column_elements = self.grid.get_column(x)
            if all(element in [SPACE,MILLION] for element in column_elements):
                self.grid.remove_column(x)
                self.grid.insert_column(x, MILLION)

    def find_paths(self):
        galaxies = [(x['row'],x['start']) for x in self.grid.find_tokens_in_rows('#')]
        logging.debug(f"Found {len(galaxies)} galaxies.")
        paths = list(itertools.combinations(galaxies,2))
        logging.debug(f"Found {len(paths)} paths.")
        return paths

    def calculate_distance(self, from_galaxy, to_galaxy):
        min_row = min(from_galaxy[0],to_galaxy[0])
        max_row = max(from_galaxy[0],to_galaxy[0])
        min_col = min(from_galaxy[1],to_galaxy[1])
        max_col = max(from_galaxy[1],to_galaxy[1])
        diff_row = max_row - min_row
        diff_col = max_col - min_col
        row_millions = sum(1 for x in [self.grid.elements[x][0] for x in range(min_row+1,max_row)] if x == MILLION)
        column_millions = sum(1 for x in [self.grid.elements[min_row][x] for x in range(min_col+1,max_col)] if x == MILLION)
        distance = int(diff_row - row_millions + (row_millions * 1e6)) + int(diff_col - column_millions + (column_millions * 1e6))
        return distance
    
    def part_1(self):
        self.double_space()
        result = sum(self.calculate_distance(x[0],x[1]) for x in self.find_paths())
        print(f"Part 1: {result}")

    def part_2(self):
        self.expand_space()
        result = sum(self.calculate_distance(x[0],x[1]) for x in self.find_paths())
        print(f"Part 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
# Solve the puzzles.
solver.parse_input()
solver.part_1()
solver.parse_input()
solver.part_2()