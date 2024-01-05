# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
from common.grid import Grid

class Solver:
    grids : "list(Grid)"

    def __init__(self, input = []):
        self.input = input
        self.grids = self.parse_grids(self.input)

    def parse_grids(self, input = None) -> "list(Grid)":
        if input is None:
            input = self.input
        grids = []
        rows = []
        def append_grid():
            grid = Grid()
            grid.initialize_from_strings(rows)
            grids.append(grid)
            rows.clear()
        for row in input:
            if row != "":
                rows.append(row)
            elif len(rows) > 0:
                append_grid()
        if len(rows) > 0:
            append_grid()
        return grids
    
    def find_mirror_column(self, grid : Grid) -> int:
        # Test for a mirror between adjacent columns.
        for c in range(grid.width - 1):
            i = 0
            reflection = True
            while reflection and c-i>=0 and c+1+i <= grid.width-1:
                reflection = grid.get_column(c-i) == grid.get_column(c+1+i)
                i += 1
            if reflection:
                return c + 1
        return 0
    
    def find_mirror_row(self, grid : Grid) -> int:
        # Test for a mirror between adjacent rows.
        for r in range(grid.height - 1):
            i = 0
            reflection = True
            while reflection and r-i>=0 and r+1+i <= grid.height-1:
                reflection = grid.get_row(r-i) == grid.get_row(r+1+i)
                i += 1
            if reflection:
                return r + 1
        return 0
  
    def part_1(self):
        result = 0
        for grid in self.grids:
            result += self.find_mirror_column(grid)
            result += 100 * self.find_mirror_row(grid)
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