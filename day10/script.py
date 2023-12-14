# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
from common.grid import Grid
from enum import Enum
import math

class Pipe(Enum):
    NS =  '|'
    NE = 'L'
    WE = '-'
    SE = 'F'
    NW = 'J'
    SW = '7'
    START = 'S'
    GROUND = '.'
    OUTSIDE = 'O'
    INSIDE = 'I'

class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    WEST = 2
    EAST = 3

# Define the puzzle solver.
class Solver:
    grid : Grid
    start = (None,None)
    start_pipe : Pipe = None

    def __init__(self, input = []):
        self.input = input

    def parse_input(self, input : "list(str)" = None):
        input_to_parse = input or self.input
        self.grid = Grid()
        self.grid.initialize_from_strings(input_to_parse)
        start = next(self.grid.find_tokens_in_rows('S'))
        self.start = (start['row'],start['start'])

    def find_tiles_inside_path(self, path):
        # Start and finish 1 space in from the edge to leave room for the path.
        for row in range(1,self.grid.height - 1):
            logging.debug(f"Scanning row {row} for inside tiles.")
            for column in range(1, self.grid.width - 1):
                # Ignore if the tile is on the path.
                if (row,column) in path:
                    continue
                # Count the number of path intersections to one (i.e. right) edge.
                intersections = 0
                bend = None
                for x in range(column+1,self.grid.width):
                    pipe_x = Pipe(self.grid.get_element(row,x)['value'])
                    # Replace the start tile with its actual pipe.
                    if pipe_x == Pipe.START:
                        pipe_x = self.start_pipe
                    if (row,x) in path:
                        # Vertical pipe segments are always an intersection.
                        if pipe_x in [Pipe.NS]:
                            intersections += 1
                        # Ignore horizontal pipe segments when counting intersections.
                        elif pipe_x in [Pipe.WE]:
                            continue
                        # Bends could be an intersection if the continue crossing vertically.
                        elif bend == None and [Pipe.NE, Pipe.SE]:
                            bend = pipe_x
                            # Do not increment until we know if the path crosses.
                        elif (bend == Pipe.SE and pipe_x == Pipe.NW) or (bend == Pipe.NE and pipe_x == Pipe.SW):
                            bend = None
                            # The path did cross, so it counts.
                            intersections += 1
                        elif (bend == Pipe.SE and pipe_x == Pipe.SW) or (bend == Pipe.NE and pipe_x == Pipe.NW):
                            bend = None
                            # Do not increment on a tangent.
                if intersections % 2 == 1:
                    yield (row,column)

    def find_length(self) -> int:
        path = self.find_path()
        return len([*path])

    def find_path(self):
        current = self.start
        direction = None
        # Walk the whole pipe.
        while current != self.start or direction == None:
            current_pipe = Pipe(self.grid.get_element(current[0],current[1])['value'])
            
            # Figure out what the starting pipe is.
            if current_pipe == Pipe.START:
                # Be sure to include the start tile in the path.
                yield current
                # Determine in which directions a pipe opens to the start tile.
                north_pipe = Pipe(self.grid.get_element(current[0]-1,current[1])['value']) in [Pipe.SW, Pipe.NS, Pipe.SE] if current[0] > 0 else False
                east_pipe = Pipe(self.grid.get_element(current[0],current[1]+1)['value']) in [Pipe.NW, Pipe.WE, Pipe.SW] if current[1] < self.grid.width else False
                south_pipe = Pipe(self.grid.get_element(current[0]+1,current[1])['value']) in [Pipe.NW, Pipe.NS, Pipe.NE] if current[0] < self.grid.height else False
                west_pipe = Pipe(self.grid.get_element(current[0],current[1]-1)['value']) in [Pipe.NE, Pipe.WE, Pipe.SE] if current[1] > 0 else False
                if north_pipe and south_pipe:
                    current_pipe = Pipe.NS
                    direction = Direction.SOUTH
                elif north_pipe and east_pipe:
                    current_pipe = Pipe.NE
                    direction = Direction.SOUTH
                elif west_pipe and east_pipe:
                    current_pipe = Pipe.WE
                    direction = Direction.EAST
                elif south_pipe and east_pipe:
                    current_pipe = Pipe.SE
                    direction = Direction.NORTH
                elif north_pipe and west_pipe:
                    current_pipe = Pipe.NW
                    direction = Direction.SOUTH
                elif south_pipe and west_pipe:
                    current_pipe = Pipe.SW
                    direction = Direction.NORTH
                self.start_pipe = current_pipe
                
            # Figure out where you can go from here, without backtracking.
            if current_pipe == Pipe.WE:
                if direction == Direction.EAST:
                    direction = Direction.EAST
                elif direction == Direction.WEST:
                    direction = Direction.WEST
            elif current_pipe == Pipe.NW:
                if direction == Direction.EAST:
                    direction = Direction.NORTH
                elif direction == Direction.SOUTH:
                    direction = Direction.WEST
            elif current_pipe == Pipe.NS:
                if direction == Direction.NORTH:
                    direction = Direction.NORTH
                elif direction == Direction.SOUTH:
                    direction = Direction.SOUTH
            elif current_pipe == Pipe.NE:
                if direction == Direction.SOUTH:
                    direction = Direction.EAST
                elif direction == Direction.WEST:
                    direction = Direction.NORTH
            elif current_pipe == Pipe.SE:
                if direction == Direction.WEST:
                    direction = Direction.SOUTH
                elif direction == Direction.NORTH:
                    direction = Direction.EAST
            elif current_pipe == Pipe.SW:
                if direction == Direction.EAST:
                    direction = Direction.SOUTH
                elif direction == Direction.NORTH:
                    direction = Direction.WEST
            
            # Go that direction.
            if direction == Direction.NORTH:
                current = (current[0]-1,current[1])
            elif direction == Direction.EAST:
                current = (current[0],current[1]+1)
            elif direction == Direction.SOUTH:
                current = (current[0]+1,current[1])
            elif direction == Direction.WEST:
                current = (current[0],current[1]-1)
            
            # Add the next pipe to the path.
            yield current
    
    def part_1(self):
        length = self.find_length()
        result = math.ceil(length / 2)
        print(f"Part 1: {result}")

    def part_2(self):
        path = [*self.find_path()]
        tiles_inside_path = self.find_tiles_inside_path(path)
        result = len([*tiles_inside_path])
        print(f"Part 2: {result}")

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")
# Instantiate the puzzle solver with the parsed input.
solver = Solver(input)
solver.parse_input()
# Solve the puzzles.
solver.part_1()
solver.part_2()