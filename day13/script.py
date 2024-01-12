# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
from common.grid import Grid
import copy

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
    
    def find_mirror_column(self, grid : Grid, exclude : int = None) -> int:
        # Test for a mirror between adjacent columns.
        for c in range(grid.width - 1):
            i = 0
            reflection = True
            while reflection and c-i>=0 and c+1+i <= grid.width-1:
                reflection = grid.get_column(c-i) == grid.get_column(c+1+i)
                i += 1
            if reflection and (c + 1) != exclude:
                return c + 1
        return 0
    
    def find_mirror_row(self, grid : Grid, exclude : int = None) -> int:
        # Test for a mirror between adjacent rows.
        for r in range(grid.height - 1):
            i = 0
            reflection = True
            while reflection and r-i>=0 and r+1+i <= grid.height-1:
                reflection = grid.get_row(r-i) == grid.get_row(r+1+i)
                i += 1
            if reflection and (r + 1) != exclude:
                return r + 1
        return 0
  
    def part_1(self):
        result = 0
        for grid in self.grids:
            result += self.find_mirror_column(grid)
            result += 100 * self.find_mirror_row(grid)
        print(f"Part 1: {result}")

    def part_2(self):
        def get_differences(x, y):
            'Returns the number of dissimilar elements in the same positions in two collections.'
            return sum(1 for a,b in zip(x,y) if a != b)
        result = 0
        for g in range(len(self.grids)):
            logging.debug(f"Processing grid #{g}.")
            grid = self.grids[g]
            original_mirror_column = self.find_mirror_column(grid)
            original_mirror_row = self.find_mirror_row(grid)
            logging.debug(f"Original mirror column: {original_mirror_column if original_mirror_column > 0 else 'None'}")
            logging.debug(f"Original mirror row: {original_mirror_row if original_mirror_row > 0 else 'None'}")
            new_mirror_column = 0
            new_mirror_row = 0
            logging.debug(f"grid dimensions: {grid.width}w X {grid.height}h")
            for l in range(grid.width - 1):
                for r in range(l + 1, grid.width):
                    left = grid.get_column(l)
                    right = grid.get_column(r)
                    differences = get_differences(left,right)
                    logging.debug(f"column {l}/{r}: {differences} diffs")
                    if differences == 1:
                        replaced = copy.deepcopy(grid)
                        replaced.replace_column(l, right)
                        mirror_column = self.find_mirror_column(replaced, original_mirror_column)
                        if(mirror_column > 0 and mirror_column != original_mirror_column):
                            logging.debug(f"Found new mirror column {mirror_column}.")
                            new_mirror_column = mirror_column
                        mirror_row = self.find_mirror_row(replaced, original_mirror_row)
                        if(mirror_row > 0 and mirror_row != original_mirror_row):
                            logging.debug(f"Found new mirror row {mirror_row}.")
                            new_mirror_row = mirror_row
            for t in range(grid.height - 1):
                for b in range(t + 1, grid.height):
                    top = grid.get_row(t)
                    bottom = grid.get_row(b)
                    differences = get_differences(top,bottom)
                    if differences == 1:
                        replaced = copy.deepcopy(grid)
                        replaced.replace_row(t, bottom)
                        mirror_column = self.find_mirror_column(replaced, original_mirror_column)
                        if(mirror_column > 0 and mirror_column != original_mirror_column):
                            logging.debug(f"Found new mirror column {mirror_column}.")
                            new_mirror_column = mirror_column
                        mirror_row = self.find_mirror_row(replaced, original_mirror_row)
                        if(mirror_row > 0 and mirror_row != original_mirror_row):
                            logging.debug(f"Found new mirror row {mirror_row}.")
                            new_mirror_row = mirror_row
            if (new_mirror_column > 0) and (new_mirror_row > 0):
                logging.warning(f"Two new mirror column/row {new_mirror_column}/{new_mirror_row}!")
            elif (new_mirror_column > 0) or (new_mirror_row > 0):
                logging.debug(f"Using new mirror column/row {new_mirror_column}/{new_mirror_row} instead of original {original_mirror_column}/{original_mirror_row}.")
                result += new_mirror_column
                result += 100 * new_mirror_row
            else:
                logging.debug(f"Using original mirror column/row {original_mirror_column}/{original_mirror_row}.")
                result += original_mirror_column
                result += 100 * original_mirror_row
            logging.debug(f"Running result: {result}")
        print(f"Part 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
# Solve the puzzles.
solver.part_1()
solver.part_2()