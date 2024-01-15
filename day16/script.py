# Setup the environment.
import sys,os,logging
logging.basicConfig(level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# Import helper modules.
from common.input_parser import InputParser
import re
from common.grid import Grid
from enum import Enum

class Direction(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4

# Parse the input file.
input = InputParser.parse_lines(__file__, "input.txt")

# A grid to store the mirrors and splitters.
maze = Grid()
maze.initialize_from_strings(input)
# A grid to store the energization state.
energized = Grid()
energized.initialize_from_strings([['.'] * maze.width] * maze.height)
# A grid to break beam loops.
passing = Grid()
passing.elements = [[[] for _ in range(maze.width)] for _ in range(maze.height)]

def shine_beam(row : int, column : int, direction : Direction):
    # Beam has exited the maze.
    if row < 0 or column < 0 or row == maze.height or column == maze.width:
        return
    # Mark this element in the maze as having been energized.
    energized.set_value(row, column, '#')
    # Break out of beam loops.
    element = passing.get_element(row, column)['value']
    if direction in element:
        return
    else:
        element.append(direction)
        passing.set_value(row, column, element)
    # Fetch the element in the maze at this location.
    element = maze.get_element(row, column)['value']
    # Return the resulting beam(s) after passing through this location.
    if direction == Direction.UP:
        if element == '.':
            yield (row - 1, column, Direction.UP)
        elif element == '/':
            yield (row, column + 1, Direction.RIGHT)
        elif element == '\\':
            yield (row, column - 1, Direction.LEFT)
        elif element == '|':
            yield (row - 1, column, Direction.UP)
        elif element == '-':
            yield (row, column - 1, Direction.LEFT)
            yield (row, column + 1, Direction.RIGHT)
    elif direction == Direction.LEFT:
        if element == '.':
            yield (row, column - 1, Direction.LEFT)
        elif element == '/':
            yield (row + 1, column, Direction.DOWN)
        elif element == '\\':
            yield (row - 1, column, Direction.UP)
        elif element == '|':
            yield (row - 1, column, Direction.UP)
            yield (row + 1, column, Direction.DOWN)
        elif element == '-':
            yield (row, column - 1, Direction.LEFT)
    elif direction == Direction.DOWN:
        if element == '.':
            yield (row + 1, column, Direction.DOWN)
        elif element == '/':
            yield (row, column - 1, Direction.LEFT)
        elif element == '\\':
            yield (row, column + 1, Direction.RIGHT)
        elif element == '|':
            yield (row + 1, column, Direction.DOWN)
        elif element == '-':
            yield (row, column - 1, Direction.LEFT)
            yield (row, column + 1, Direction.RIGHT)
    elif direction == Direction.RIGHT:
        if element == '.':
            yield (row, column + 1, Direction.RIGHT)
        elif element == '/':
            yield (row - 1, column, Direction.UP)
        elif element == '\\':
            yield (row + 1, column, Direction.DOWN)
        elif element == '|':
            yield (row - 1, column, Direction.UP)
            yield (row + 1, column, Direction.DOWN)
        elif element == '-':
            yield (row, column + 1, Direction.RIGHT)

# The beam enters the maze from the top left, going right.
beams = [*shine_beam(row=0, column=0, direction=Direction.RIGHT)]
while beams:
    next_beams = []
    for beam in beams:
        next_beams.extend(shine_beam(beam[0], beam[1], beam[2]))
    beams = next_beams

result = len([*energized.find_tokens_in_rows('#')])
print(f"Part 1: {result}")